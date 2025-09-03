# Dependency Inversion Principle
# High-level modules should not depend on low-level modules. 
# Both should depend on abstraction (interface or base class)

# avoid directly creating object inside a class

from abc import ABC, abstractmethod
class Notifier(ABC):
    def send(self, message):
        pass
    
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"email sent : {message}")
        
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"SMS sent: {message}")
        
class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier
        
    def notify(self, message):
        self.notifier.send(message)
        
        
        
email_service = NotificationService(EmailNotifier())
email_service.notify("Hello!")

sms_service = NotificationService(SMSNotifier())
sms_service.notify("Hi!")
        

    
