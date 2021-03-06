from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        usr = self.scope['user']
        username = usr.username
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print (message)
        self.send(text_data=json.dumps({
            'message': message  + ' ' + "-" + str(usr)
        }))
