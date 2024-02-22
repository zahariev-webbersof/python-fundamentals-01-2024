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


emails = []

while True:
    data = input().split()

    if data[0] == 'Stop':
        break

    sender, receiver, content = data
    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(i) for i in input().split(', ')]

for index in indices:
    if 0 <= index < len(emails):
        emails[index].send()

for email in emails:
    print(email.get_info())

