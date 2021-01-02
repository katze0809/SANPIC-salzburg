
import requests
import datetime 
#API request URL
url='https://www.salzburg-airport.com/en/thecompany/environment/noise-events/?getNoiseJSON=1&day={0}&from=00%3A00&to=23%3A59&location=5&no_cache=1'

#variable to change the date
tod = datetime.datetime.now()
d = datetime.timedelta(days = 5)
a = tod - d
yesterday=a.strftime("%Y-%m-%d")

date=yesterday
newUrl=url.format(yesterday,5)
newUrl


jsonObj=requests.get(newUrl).json()
print(jsonObj)





