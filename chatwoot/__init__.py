from enum import Enum

import requests

chatwoot_url = "http://chat.vecinos.com.ar"
chatwoot_api_token = "cy7mNSLUH6uyJ5wEAcrrDe5e"
chatwoot_bot_token = ""


class MessageType(Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"


def send_to_chatwoot(account, conversation, message, message_type=MessageType.OUTGOING):
    data = {
        'content': message,
        'message_type': message_type.value
    }
    url = f"{chatwoot_url}/api/v1/accounts/{account}/conversations/{conversation}/messages"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_access_token": f"{chatwoot_api_token}"
    }
    r = requests.post(url, json=data, headers=headers)
    return r.json()


if __name__ == '__main__':
    r = send_to_chatwoot(
        account=2,
        conversation=1,
        message='Hola mundo'
    )
    print(r)
