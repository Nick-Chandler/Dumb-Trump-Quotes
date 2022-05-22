import os
from flask import  Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from quotes import give_rand_quote

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message('Dumb Donald Trump Quote Generator: ' + '\n' + '\n' + "Trump: " + "\n" + "\n" '"' + give_rand_quote() + '"')

    return "" + str(resp) + ""

if __name__ == "__main__":
    app.run(debug=True)
