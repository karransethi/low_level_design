from abc import ABC, abstractmethod 

class NotificationService:
    def __init__(self, channel):
        self.channel = channel
        
    def send_message(self, message):
        self.channel.send(message)
        
        
class NotificationChannel(ABC):
        
    @abstractmethod
    def send(self, msg):
        pass
    
class Email(NotificationChannel):
        
    def send(self, msg):
        print(f'Sending email : {msg}')
        
class SMS(NotificationChannel):
        
    def send(self, msg):
        print(f'Sending SMS : {msg}')
        
sms = SMS()

noti = NotificationService(sms)
noti.send_message("Heyy")