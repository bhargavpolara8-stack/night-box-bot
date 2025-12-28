import requests
import feedparser
import time

# તમારી વિગતો
BOT_TOKEN = "8523307430:AAFFDRMDmIgUIEBTUi2dRwX0JI09irLClP8"
GP_API = "577fb05dfe3fdcb4845e77cad707e3d57b1c4ac5"
CHANNEL_ID = "@NightBoxOffice" # તમારી ચેનલનું સાચું નામ ચેક કરી લેજો
RSS_URL = "https://vegamovies.ngo/feed/" 

def shorten(link):
    try:
        r = requests.get(f"https://gplinks.in/api?api={GP_API}&url={link}")
        return r.json().get("shortenedUrl", link)
    except:
        return link

last_entry_link = ""
print("Bot Started...")

while True:
    try:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            latest = feed.entries[0]
            if latest.link != last_entry_link:
                short_link = shorten(latest.link)
                text = f"<b>🎬 {latest.title}</b>\n\n🔗 <b>Download Link:</b> {short_link}\n\n📢 Join: {CHANNEL_ID}"
                msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                requests.get(msg_url, params={"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"})
                last_entry_link = latest.link
                print(f"Posted: {latest.title}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(600) # દર ૧૦ મિનિટે નવી મૂવી ચેક કરશે
