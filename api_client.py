import os
import requests
from dotenv import load_dotenv
from models import User
from db_loader import save_users_to_db

load_dotenv()

def fetch_users() -> list[dict]:
    url = os.environ.get("API_URL")
    if not url:
        print("Error: API_URL not found in environment variables.")
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

if __name__ == "__main__":
    raw_users = fetch_users()
    user_objects = []
    for user in raw_users:
        city = user["address"]["city"]

        obj = User(
            user_id=user["id"],
            name=user["name"],
            email=user["email"],
            city=city
        )
        user_objects.append(obj)

    print(f"Successfully created {len(user_objects)} User objects.")
    print(user_objects[0].get_summary())

    save_users_to_db(user_objects, "users.db")