import os
from twilio.rest import Client
from phoneNumbers import *


account_sid = 'ACac21973947167e58325d664926800444'
auth_token = '0559bb38a0efe0e86a09657bb8a53a78'

client = Client(account_sid, auth_token)
message = 'Damn you lost on {Champ Name}? You kinda ass bruh'


def create_message(client, to, message):
    client.messages.create(
        to = to,
        from_='+19593359894',
        body= message
    )

create_message(client, numbers['Nick'], message)