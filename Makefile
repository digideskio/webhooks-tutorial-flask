build:
	heroku create
	git push heroku master
	heroku config:set PUSHER_APP_ID=98647
	heroku config:set PUSHER_KEY=1f597f3b1f4a81f0ea23
	heroku config:set PUSHER_SECRET=06abb2fe0cded47d9c63
	heroku config:set EVENTBRITE_EVENT_ID=14797885875
	heroku config:set EVENTBRITE_OAUTH_TOKEN=MEKFYTPEY7E3HFXNWX2X
	heroku config:set SECRET_WEBHOOK_URL=dream