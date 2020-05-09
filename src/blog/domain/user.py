from datetime import date


class User:
    def __init__(
        self, user_id: str, first_name: str, last_name: str, role: str, created_at: date
    ):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.created_at = created_at

    def __repr__(self):
        return f"<User {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)
