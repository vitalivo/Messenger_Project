# filepath: c:\Users\vital\skillfactory\Messenger_Project\messenger\consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("WebSocket connected")

    def disconnect(self, close_code):
        print("WebSocket disconnected")

    def receive(self, text_data):
        print(f"Message received: {text_data}")
        text_data_json = json.loads(text_data)
        message = text_data_json['text']

        self.send(text_data=json.dumps({
            'text': message
        }))
        print(f"Message sent: {message}")