import json
import os

DB_PATH = "database/users.json"

async def users_load():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump([], f)
        return []


async def user_save(users):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2)


async def user_search(id_telegram:int, username=None):
    users = await users_load()

    for user in users:
        if user['id_telegram'] == id_telegram:
            return user

    new_id = max((user['id'] for user in users), default=0) + 1
    new_user = {
        "id": new_id,
        "id_telegram": id_telegram,
        "username": username,
        
        "price": 0,
        "configs_count": 0,
        "subscription_start": None,
        "subscription_end": None,
        
        "preliminary_price": 0,
        "preliminary_configs_count": 0,
        "preliminary_subscription_start": None,
        "preliminary_subscription_end": None,
        "preliminary_type_pay": None,
        
        "payment_status": None,
        "blacklist": None
    }

    users.append(new_user)
    await user_save(users)
    return new_user


async def user_update(id_telegram, field, value):
    users = await users_load()

    for user in users:
        if user['id_telegram'] == id_telegram and field in user:
            user[field] = value
            await user_save(users)
            return True

    return False


async def user_clear_cache(id_telegram: int):
    await user_update(id_telegram, "preliminary_price", 0)
    await user_update(id_telegram, "preliminary_configs_count", 0)
    await user_update(id_telegram, "preliminary_subscription_start",None)
    await user_update(id_telegram, "preliminary_subscription_end", None)
    await user_update(id_telegram, "preliminary_type_pay", None)

