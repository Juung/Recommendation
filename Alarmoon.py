from slacker import Slacker

def send_message(message):
	api_token = 'xoxp-182904866199-182886388694-184850559360-c273252a26df82bb34c870297471391d'
	slacker = Slacker(api_token)
	slacker.chat.post_message('general', message)