class Member:
    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Phone: {self.phone}"
    