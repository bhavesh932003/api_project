
import requests
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')
raw_TS = datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")
curr_time = raw_TS.strftime("%H:%M:%S")

telegram_auth_token = "5523830697:AAESAt_13U94r7jfcy4jC9eZmlbvTkpUBcE"
telegram_group_id = "personaltimemanager"

msg = f" Message received on {curr_date} at {curr_time}"

def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_resp = requests.get(telegram_api_url)

    if tel_resp.status_code:
        print("INFO : Notification has been sent on Telegram")
    else:
        print("ERROR: Could not send Message")


send_msg_on_telegram(msg)