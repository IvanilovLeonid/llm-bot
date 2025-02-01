import csv


def save_to_csv(user_id, name, interests, registration_date):
    file_path = "data/users.csv"

    header = ["user_id", "name", "interests", "registration_date"]
    try:
        with open(file_path, "x", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
    except FileExistsError:
        pass

    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, name, interests, registration_date])


def get_user_interests(csv_path="data/users.csv"):
    users = []
    try:
        with open(csv_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append({
                    "user_id": int(row["user_id"]),
                    "interests": row["interests"]
                })
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
    return users


def get_one_user_interests(user_id: int) -> str:
    try:
        with open("data/users.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["user_id"]) == user_id:
                    return row["interests"]
    except Exception as e:
        print(f"Ошибка при чтении интересов пользователя {user_id}: {e}")
    return "не указаны"
