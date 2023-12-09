import os
from twilio.rest import Client

ACCOUNT_SID = "ACfd290673ba69ccb1748912b28521ab8d"

AUTH_TOKEN = "ebc1eeedbe254848ba0284d38a3482f5"

account_sid = ACCOUNT_SID # os.environ['TWILIO_ACCOUNT_SID']
auth_token = AUTH_TOKEN # os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say language="es-MX" voice="man" loop="1">'
                              'Buenas. <Pause length="3"/>   Ernesto.'
                              '<Pause length="3"/>  Juan ha alertado desde el comercio "La Anónima" '
                              '<Pause length="3"/>  ubicado enn Av. Independencia 2581.'
                              '<Pause length="2"/>  Ya estamos informando a las autoridades.'
                              '<Pause length="3"/> Te mantendremos informado.'
                              '<Pause length="3"/> Gracias por utilizar nuestro servicio de alerta.'
                              '</Say></Response>',
    to='+5491136206603',
    from_='+5491128835917'
                        )
# to = '+5491162954760',

print(call.sid)