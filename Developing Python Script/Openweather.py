import requests
a = 'https://api.openweathermap.org/data/2.5/weather?q=Chennai,IN&appid=6d13d12f9cd34a07871a5795d01e2c47'
r = requests.get(url = a)
data =r.json()
print(r)
print(data)
temp = data["main"]["temp"]
hum = data["main"]["humidity"]
print("Temprature is :", temp)
print("Humidity is :",hum)