
# Parent class

class Artist:
    name = "Loren"
    email = "loren@gmail.com"
    password = "artMakesTheW0rldGoRound"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}! Let's get you signed into your Instagram account.".format(entry_name))
        else:
            print("The password or email is incorrect.")

#child class
class Instagram(Artist):
    username = "Loren_Nero"
    followers = 10000
    auth = "helloW0rld!"

    def getLoginInfo(self):
        entry_username = input("Enter your username: ")
        entry_email = input("Enter your email: ")
        entry_auth = input("Enter Instagram Password: ")
        if (entry_username == self.username and entry_auth == self.auth):
            print("Welcome back, {}! Let's sign you into your Facebook.".format(entry_username))
        else:
            print("The password or username is incorrect.")

#child class
class Facebook(Artist):
    username = "Loren Nero"
    friends = 351
    auth = "helloF4cebook!"

    def getLoginInfo(self):
        entry_username = input("Enter your first and last name: ")
        entry_email = input("Enter your email: ")
        entry_auth = input("Enter Facebook Password: ")
        if (entry_username == self.username and entry_auth == self.auth):
            print("Welcome back, {}! Happy posting!".format(entry_username))
        else:
            print("The password or username is incorrect.")

#Invoking the methods inside each class for Artist and SocialMedia

customer = Artist()
customer.getLoginInfo()

customerPage = Instagram()
customerPage.getLoginInfo()

customerFB = Facebook()
customerFB.getLoginInfo()
