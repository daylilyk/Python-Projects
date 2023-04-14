

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
class SocialMedia(Artist):
    platform = "Instagram"
    followers = 10000
    auth = "helloW0rld!"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_auth = input("Enter Instagram Password: ")
        if (entry_email == self.email and entry_auth == self.auth):
            print("Welcome back, {}! Happy posting!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Invoking the methods inside each class for Artist and SocialMedia

customer = Artist()
customer.getLoginInfo()

customerPage = SocialMedia()
customerPage.getLoginInfo()
    
