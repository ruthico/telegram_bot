from flask import Flask, request, Response
import requests

app = Flask(__name__)


TOKEN = '1824419890:AAFj3p4DAmOKKLDmUvQ_e-Hp5WI7gqmkzk0'
TELEGRAM_INIT_WEBHOOK_URL = \
    ''.format(TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/')
def sanity():
    return "Server is running"


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    message = request.get_json("message")
    message_text = message['message']['text']
    response = ''
    #if message_text.startswith('/start'):
     #           response = "Let's create a new poll. First, select the type of poll."
      #          #צריך להפוך את הסקר לציבורי
    if message_text.startswith('/start'):
         response ="send me the question."
    elif message_text.andswith('?'):
        add_question(message_text)
        response = "Creating a new poll:" + message_text+"\n"+"Please send me the first answer option."
    elif  sum_anser()==0:
        update_question(message_text)
        response = "Good. Now send me another answer option."
    elif sum_anser()>1:
        update_question(message_text)
        response = "Good. Feel free to add more answer options\n. When you've added enough\n, simply send /done or press the button below to finish creating the poll."
    elif message_text == "/done":
        response =







