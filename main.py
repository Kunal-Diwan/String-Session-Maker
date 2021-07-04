import pyrogram
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

opt = input("""
[p] Pyrogram
[t] Telethon

Choose your option: """)

if opt == "p":
	print("You've selected pyrogram\n")
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	with pyrogram.Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
		session_str = app.export_session_string()
		if app.get_me().is_bot:
			user_name = input("Enter the username: ")
			msg = app.send_message(user_name, session_str)
		else:
			msg = app.send_message("me", session_str)
		msg.reply_text(
		    "This session is maded by @kunaldiwan . Join @DevelopedBots for more ",
		    quote=True,
		)
		print(
		    "please check your Telegram Saved Messages in Telegram for the StringSession "
		)

elif opt == "t":
	print("You've selected Telethon\n")
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
		session_str = client.session.save()
		if client.is_bot():
			user_name = input("Enter the username: ")
			msg = client.send_message(user_name, session_str)
		else:
			msg = client.send_message("me", session_str)
		msg.reply(
		    "This string session is maded by @kunaldiwan. Join @DevelopedBots for more ",
		)
		print(
		    "please check your Telegram Saved Messages/User's PM for the StringSession "
		)
else:
	print("Only p/t is accepted")
