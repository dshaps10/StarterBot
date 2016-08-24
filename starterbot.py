import os
import time
import slackclient from SlackClient 

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

#constraints
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"

#instantiate Slack and Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))