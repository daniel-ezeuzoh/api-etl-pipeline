class User:
    def __init__(self, user_id: int, name: str, email: str, city: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.city = city

    def get_summary(self) -> str:
        return f"User {self.user_id}: {self.name} ({self.email}) lives in {self.city}"