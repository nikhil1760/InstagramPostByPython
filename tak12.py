from instabot import Bot


bot = Bot()

bot.login(username = "Username",
		password = "Password")

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("1.jpg",
				caption ="Technical Scripter Event 2019")
