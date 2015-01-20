import os
# import traceback

from flask import Flask, render_template, request
import pusher
import eventbrite

PUSHER_APP_ID = os.environ['PUSHER_APP_ID']
PUSHER_KEY = os.environ['PUSHER_KEY']
PUSHER_SECRET = os.environ['PUSHER_SECRET']
EVENTBRITE_EVENT_ID = os.environ['EVENTBRITE_EVENT_ID']
EVENTBRITE_OAUTH_TOKEN= os.environ['EVENTBRITE_OAUTH_TOKEN']

API_URL = "https://www.eventbriteapi.com/v3"

p = pusher.Pusher(app_id=PUSHER_APP_ID, key=PUSHER_KEY, secret=PUSHER_SECRET)

app = Flask(__name__)
app.debug = True

eventbrite = eventbrite.Eventbrite(EVENTBRITE_OAUTH_TOKEN)


@app.route('/')
def index():

    # Get the event details
    event = eventbrite.get_event(EVENTBRITE_EVENT_ID)

    # Get the attendee list
    attendees = eventbrite.get_event_attendees(EVENTBRITE_EVENT_ID)

    return render_template(
        'index.html',
        settings={'PUSHER_KEY': PUSHER_KEY},
        event=event,
        attendees=attendees
    )

@app.route('/add-danny')
def add_danny():
    user = eventbrite.get_user()
    p['webhooks'].trigger("User", user)
    return "Danny added"


@app.route('/webhook', methods=['POST'])
def webhook():
    """
        Webhooks simply provide API endpoints that the user can use to gather
        more information. They are sent as HTTP POSTS with the JSON mimetype
        specified in the header.

        A sample webhook:
            {
              "api_url": "https://www.eventbriteapi.com/v3/orders/1234567890/",
              "config": {
                "endpoint_url": "https://myawesomeapp.com/webhook",
                "insecure_ssl": "0"
              }
            }
    """
    # Get the webhook data out of flask.
    # hook_data = request.get_json()

    # Use the API client to convert from a webhook to an API object
    api_object = eventbrite.webhook_to_object(request)
    p['webhooks'].trigger("Attendee", api_object)
    return ""



if __name__ == '__main__':
    app.run()