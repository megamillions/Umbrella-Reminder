#! python3
# umbrellaReminder.py - Scrape data from the web and
# sends text message if umbrella will be needed today.

from twilio.rest import Client
import bs4, requests

# Hard-code these values as the script will be run automatically.
account_sid = 'xxxx'
auth_token = 'xxxx'
twilio_number = '+xxxx'
to_number = '+xxxx'

# In addition to the above, edit url to match your own and uncomment out line.
#url = 'https://www.wunderground.com/weather/xxxx'

print('Accessing %s...' % url)

res = requests.get(url)
res.raise_for_status()

# Check if raining today.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
precip_elem = soup.select('.hook')
precip_chance = int(precip_elem[0].getText().split('%')[0])

# Text a reminder if it is.
threshold = 20

if precip_chance >= threshold:
	print('Bring an umbrella. Sending alert to %s.' % to_number)
	
	message = 'Bring an umbrella today. There is a %s percent chance of rain.' % precip_chance
	
	twilio_client = Client(account_sid, auth_token)
	twilio_client.messages.create(body=message, from_=twilio_number, to=to_number)
	
	print('Alert successfully sent!')
	
else:
	print('Do not bring an umbrella. Chance of precipitation stands at %s percent.' % precip_chance)