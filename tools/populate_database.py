import json
import random
import requests

url = 'http://localhost:8000/api/v2/readings.json'

headers = { 
    'Content-Type': 'application/json',  
    'Authorization': 'jwt xxx'
}

def main():
    while True:
        payload = {
            'device_id': 'aabbccddeeff',
            'temperature': random.uniform(20.0, 35.9)
        }

        r = requests.post(url, data=json.dumps(payload), headers=headers)
        # print('status_code: {}'.format(r.status_code))
        # print('text: {}'.format(r.text))


if __name__ == '__main__':
    main()