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
            "Subject": "Літо близько!",
            "HTMLPart": '<h1 style="background-color: rgba(200, 159, 45, 0.52); text-align: center;"><em><span style="color: #00ffff;">Всі на море!</span></em><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s15.postimg.cc/oqjgnf0e3/mock_image.jpg" width="824" height="549" /></h1>',

        }
    ]
}
print(mailjet.send.create(data=data).text)

'https://postimages.org/'
