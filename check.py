import requests
import schedule
import time

url = 'https://yiyan.bobocdn.tk/api/yiyan'

def check_website():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Website is up and running!')
        else:
            print('Website is not responding.')
    except requests.exceptions.RequestException as e:
        print('Website is not responding.')

schedule.every(1).minutes.do(check_website)

while True:
    schedule.run_pending()
    time.sleep(60)
