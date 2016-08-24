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

if __name__ == "__main__":
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	if slack_client.rtm_connect():
		print("StarterBot connected and running!")
		while True:
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel:
				handle_comand(command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID")