class Party:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        self.people.append(name)

    def get_party_info(self):
        return f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}"


party = Party()

while True:
    name = input()
    if name == 'End':
        break

    party.add_person(name)

print(party.get_party_info())
