build:
	heroku create
	git push heroku master
	heroku config:set PUSHER_APP_ID=XXXXXXXXXX
	heroku config:set PUSHER_KEY=XXXXXXXXXX
	heroku config:set PUSHER_SECRET=XXXXXXXXXX
	heroku config:set EVENTBRITE_EVENT_ID=XXXXXXXXXX
	heroku config:set EVENTBRITE_OAUTH_TOKEN=MEKFYTPEY7XXXXXXXXXX
	heroku config:set SECRET_WEBHOOK_URL=XXXXXXXXXX
