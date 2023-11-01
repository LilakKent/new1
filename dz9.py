import requests as rs

url = 'http://api.open-notify.org/astros.json'

response = rs.get(url)

data = response.json()

astronauts = data.get('people', [])

for astronaut in astronauts:
    print(f"Космонавт: {astronaut['name']}, Корабель: {astronaut['craft']}")
