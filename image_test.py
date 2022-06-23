import requests

url = "http://127.0.0.1:8000/api/v1/places/place/1/reviews/"

payload={
    'content' : '재밌겠다'
}
files=[
#   ('image',('algorithm.png',open('db.png','rb'),'image/png')),
#   ('image',('db.png',open('db.png','rb'),'image/png'))
]
headers = {
  'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjU2MDUzNTQ4LCJlbWFpbCI6IiJ9.jGSig6gbM6sa_eYNHkFMQvmWpLTcMsaE2kH-l5PcaJk',
  'Cookie': 'csrftoken=aJwZVZk14fpYLENlVbq7gHPJ1WaiOuOjLBMRdtFWBpK9RN6TdlCPYpqS4E9SRfTJ'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)