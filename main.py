import requests
from bs4 import BeautifulSoup
import time

# તમારી વિગતો
BOT_TOKEN = "8523307430:AAFFDRMDmIgUIEBTUi2dRwX0JI09irLClP8"
GP_API = "577fb05dfe3fdcb4845e77cad707e3d57b1c4ac5"
CHANNEL_ID = "@NightBoxOffice"
URL = "https://vegamovies.careers/"

def shorten(link):
    try:
        r = requests.get(f"https://gplinks.in/api?api={GP_API}&url={link}")
        res = r.json()
        return res.get("shortenedUrl", link)
    except:
        return link

last_post_url = ""
print("Bot Started without RSS...")

while True:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # પહેલી મૂવીની પોસ્ટ શોધવા માટે (વેબસાઈટના સ્ટ્રક્ચર મુજબ)
        first_post = soup.find('h3', class_='entry-title') or soup.find('h2', class_='entry-title')
        if first_post:
            post_title = first_post.text.strip()
            post_url = first_post.find('a')['href']

            if post_url != last_post_url:
                print(f"New Movie Found: {post_title}")
                short_link = shorten(post_url)
                
                text = f"<b>🎬 {post_title}</b>\n\n🔗 <b>Download Link:</b> {short_link}\n\n📢 Join: {CHANNEL_ID}"
                msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                requests.get(msg_url, params={"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"})
                
                last_post_url = post_url
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(600) # દર ૧૦ મિનિટે ચેક કરશે
