# filepath: c:\Users\vital\skillfactory\Messenger_Project\messenger\consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['text']

        self.send(text_data=json.dumps({
            'text': message
        }))