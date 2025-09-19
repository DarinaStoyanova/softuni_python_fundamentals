class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
index = 0
command = input()
while command != "Stop":
    information = command.split(" ")
    email = Email(information[0],information[1],information[2])
    indices = input().split(", ")
    while len(indices)>0:
        index += 1
        if indices[index]
