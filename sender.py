#!/usr/bin/env python
from mailjet_rest import Client
import os


API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

data = {
  'Messages': [
                {
                        "From": {
                                "Email": "bombaylviv@gmail.com",
                                "Name": "Бомбей"
                        },
                        "To": [
                                {
                                        "Email": "pryima@stryi.com.ua",
                                        "Name": "Роман"
                                }
                        ],
                        "Subject": "Тест!",
                        "TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
                        "HTMLPart": "<h3>Dear passenger 1, welcome to Mailjet!</h3><br />May the delivery force be with you!",
                        "Attachments": [
                                {
                                        "ContentType": "text/plain",
                                        "Filename": "test.txt",
                                        "Base64Content": "VGhpcyBpcyB5b3VyIGF0dGFjaGVkIGZpbGUhISEK"
                                }
                        ]
                }
        ]
}
print(mailjet.send.create(data=data).text)
