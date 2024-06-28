import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()

usd_rate = data['Valute']['USD']['Value']

print(f"Курс доллара: {usd_rate} рублей")