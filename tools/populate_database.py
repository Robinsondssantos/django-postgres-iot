import json
import random
import requests

url = 'http://localhost:8000/api/v2/readings.json'

headers = { 
    'Content-Type': 'application/json',  
    'Authorization': 'jwt eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ5YWQ5YmM1ZThlNDQ3OTNhMjEwOWI1NmUzNjFhMjNiNDE4ODA4NzUiLCJ0eXAiOiJKV1QifQ.eyJyb2xlIjp7InZpZXdlciI6dHJ1ZX0sImdyb3VwIjpudWxsLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaW5vYnJhbS1wbGF0Zm9ybSIsImF1ZCI6Imlub2JyYW0tcGxhdGZvcm0iLCJhdXRoX3RpbWUiOjE1OTk3NjAwMDMsInVzZXJfaWQiOiI3RDluVHRZNUNjZkp5QjJISTZDWkxLMjhTRjQzIiwic3ViIjoiN0Q5blR0WTVDY2ZKeUIySEk2Q1pMSzI4U0Y0MyIsImlhdCI6MTU5OTc2MDAwMywiZXhwIjoxNTk5NzYzNjAzLCJlbWFpbCI6ImRhbmllbGJhdHRpc3RpbkBpbm9icmFtLmNvbS5iciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImRhbmllbGJhdHRpc3RpbkBpbm9icmFtLmNvbS5iciJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.WAodI3OP-zIw8oRYS5fqrwEgmiAfB9pUbDD-swCESd1_7XOoH3i-iwHKXt-irP8eXjxLk83LCYD8DLlIrjvWkfbZsT8DyVVOud0iuKtBW6cIOmG7zE7OFdnHMXCukZPbJ6JRKjrq6eXX60nbc8nVBFXnDzdeBt60Px2HM2KWMpQr7J-ff93EJiA5dGexkQBACa6-HpVk2ZuHYGOrcYSvscKh3PZapKfxuUVQShpyamSFRj6F8xhb4ENgo91DsHaRKLZByt1iL3hGrtJVrrAeVatFQwIAzgh7KQBJHud4PtZNJvd8rQH8OmUasbmjxb3S3sqb_mAlgaQgQNHDhyX09Q'
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