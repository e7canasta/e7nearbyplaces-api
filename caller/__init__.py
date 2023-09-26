import os
from twilio.rest import Client


account_sid = 'ACfd290673ba69ccb1748912b28521ab8d'
auth_token = '5936912be4757f8e5812caa08c96d843'
client = Client(account_sid, auth_token)

# url = 'http://cdn.vecinos.com.ar/voices/alerta1.xml',
call = client.calls.create(
                        url='https://demo.twilio.com/docs/voice.xml',
                        to='+5491128835917',
                        from_='+5491128835917'
                    )

print(call.sid)