import os
import google.generativeai as palm

palm.configure(api_key=os.getenv('PALM_KEY'))

message = ''

while message != 'quit':
    message = input("User: ")
    if(message != 'quit'):
        response = palm.chat(messages=message)
        print("Bot: ",response.last)
    else:
        print("Bot: Bye!")