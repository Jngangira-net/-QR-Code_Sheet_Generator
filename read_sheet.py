
import csv
from io import StringIO

import requests

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQlRdk54GxfVtp0HYSztZdB8o3j721ehAK91JTFlITAsYI21_mMc4xpaRHi32aQwv7GYPD_KqUQ5coR/pub?gid=247654418&single=true&output=csv"



response = requests.get(sheet_url)

data = StringIO(response.text)

reader = csv.DictReader(data)

students = [row for row in reader]

for student in students:
    print(student)