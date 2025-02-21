# Each class and module should focus on a single task/ responsibility at a time. 
# Everything in the class should be related to the Single purpose only.open

# A class should have only one reason to change

class Message:                   # Message class → Only stores and returns text.
    def __init__(self, text):
        self.text = text
                                 
    def get_text(self):
        return self.text 
    
class MessageSaver:              # MessageSaver class → Only saves the text to a file.
    def save_to_file(self, message, filename):
        with open(filename, 'w') as file:
            file.write(message.get_text())
            

msg = Message("Hello world")
saver = MessageSaver()
saver.save_to_file(msg, "message.txt")


     
# This keeps the responsibilities separate and clear, making the code easy to understand and maintain