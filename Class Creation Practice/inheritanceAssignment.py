

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
            print("\nWelcome back, {}! \nLet's get you signed into your Instagram account.".format(entry_name))
        else:
            print("The password or email is incorrect.")

child class
class Instagram(Artist):
    username = "Loren_Nero"
    email = "loren@gmail.com"
    auth = "helloW0rld!"

    def getLoginInfo(self):
        entry_username = input("\nEnter your username: ")
        entry_email = input("Please confirm your email: ")
        entry_auth = input("Enter Instagram Password: ")
        if (entry_username == self.username and entry_auth == self.auth):
            print("\nWelcome back, {}!".format(entry_username))
            print("\nNow, let's sign you into your Facebook.")
        else:
            print("\nThe password or username is incorrect.")

#child class
class Facebook(Artist):
    username = "LorenNero"
    phoneNum = "803-966-8696"
    auth = "helloF4cebook!"
    authPin = "9686"

    def getLoginInfo(self):
        entry_username = input("\nEnter your username: ")
        entry_phoneNum = input("Enter the phone number associated with your account: ")
        entry_auth = input("Enter Facebook Password: ")
        entry_authPin = input("\nOops! It looks like there's been some suspicious activity on your account. \nTo confirm your identity please input your personalized pin number: ")
        if (entry_username == self.username and entry_phoneNum == self.phoneNum and entry_auth == self.auth and entry_authPin == self.authPin):
            print("\nWelcome back, {}! Since your last login, \nseveral attempts to login to your account were made from Portand, Oregon. \nPlease go to settings -> security to confirm if this was you.\
            \nIf it was not, we suggest you change your password!".format(entry_username))
        else:
            print("The phone number, password, or pin is incorrect.")

#Invoking the methods inside each class for Artist and SocialMedia

customer = Artist()
customer.getLoginInfo()

customerPage = Instagram()
customerPage.getLoginInfo()

customerFB = Facebook()
customerFB.getLoginInfo()
