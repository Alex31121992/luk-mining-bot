
import os
import time
import requests

TOKEN = os.environ["BOT_TOKEN"]
URL = f"https://api.telegram.org/bot{TOKEN}/"

offset = 0

while True:
    try:
        data = requests.get(
            URL + "getUpdates",
            params={"offset": offset, "timeout": 30},
            timeout=40
        ).json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message", {})
            chat = msg.get("chat", {})
            chat_id = chat.get("id")
            command = msg.get("text", "")

            if chat_id and command == "/start":
                requests.post(URL + "sendMessage", data={
                    "chat_id": chat_id,
                    "text": "⛏ Вітаємо у LUK Mining!\n\n"
                            "Монета LUK чекає на тебе!\n"
                            "Скоро тут запрацює майнінг 🚀"
                })

    except Exception as e:
        print(e)
        time.sleep(5)
      
