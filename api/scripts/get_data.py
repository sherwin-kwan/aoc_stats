from bs4 import BeautifulSoup
from urllib.request import urlopen
from api.models import Puzzle, Record
from datetime import datetime, timedelta

def parse_entry(entry, puzzle, part):
  position = entry.find_all("span")[0].string.split("  ")[-1]
  finished_at = entry.find_all("span")[1].string.split("  ")[-1]
  time = datetime.strptime(finished_at, "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")
  return Record(position=int(position.replace(")", "")), seconds=time.seconds, puzzle=puzzle, part=part)

def get_data(year, day):
  raw = urlopen(f"https://adventofcode.com/{year}/leaderboard/day/{day}")
  soup = BeautifulSoup(raw, "html.parser")
  entries = soup.find_all("div", class_="leaderboard-entry")
  if len(entries) != 200:
    return false
  puz = Puzzle(year=year, day=day)
  puz.save()
  for ind, entry in enumerate(entries):
    part = 2 if ind < 100 else 1
    rec = parse_entry(entry, puz, part)
    if ind == 0: puz.first_gold = rec.seconds 
    if ind == 99: puz.hundredth_gold = rec.seconds
    if ind == 100: puz.first_silver = rec.seconds
    if ind == 199: puz.hundredth_silver = rec.seconds
    rec.save()
  puz.save()

for year in range(2015, 2022):
  for day in range(1, 26):
    get_data(year, day)