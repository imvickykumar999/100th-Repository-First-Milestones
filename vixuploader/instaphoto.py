from instabot import Bot
bot = Bot()

def upload():
    user = input('Enter Username : ')
    passwd = input('Enter Password : ')

    bot.login(username = user, password = passwd)

    path = input('Enter Path, or Photo name : ')
    cap = input('Enter Caption : ')

    bot.upload_photo(path, caption = cap)
    print("\n Congratulations, Photo is Uploaded... ") # photo.png.REMOVE_ME

# upload()
