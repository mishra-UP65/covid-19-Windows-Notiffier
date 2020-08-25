import requests
import json
from win10toast import ToastNotifier
import time

r = requests.get('https://coronavirus-19-api.herokuapp.com/countries/india')
data = r.json()
text = f'Confirmed Cases: {data["cases"]}\nToday Case:{data["todayCases"]}\nActive:{data["active"]}\n#Stay home, #Stay safe'

while True:
    toast = ToastNotifier()
    toast.show_toast( "COVID-19 Updates",
                     text, 
                     icon_path='covid19.ico',
                     duration=20)
    time.sleep(30)
