import requests

link = "https://adventofcode.com/2021/day/1/input"
f = requests.get(link)
print(f.text)