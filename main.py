import requests

# તમારી ફાઈનલ વિગતો
TOKEN = "8523307430:AAFFDRMDmIgUIEBTUi2dRwX0JI09irLClP8"
CHAT_ID = "7768160549"

def get_forex_data():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        data = response.json()
        # USD થી INR નો ભાવ
        return data['rates']['INR']
    except Exception as e:
        return None

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

# રન કરો
price = get_forex_data()
if price:
    msg = f"✅ Forex Bot Active!\n\n💵 1 USD = ₹{price} INR\n📊 Update: Live"
    send_telegram_msg(msg)
