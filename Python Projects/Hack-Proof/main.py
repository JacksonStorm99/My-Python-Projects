input("This is a very important and secure text file. In order to access it, please provide your username and password")
username = str(input("Enter a username: "))
password = str(input("Enter a password: "))
def check_credentials(username, password):
    if username == "hello" and password == "helloagain":
        print("Access granted")
        print("Opening file...")
        with open("C:\\Siddarth\\Dev\\Python Projects\\Hack-Proof\\hello.txt", "r") as f:
            print(f.read())
    else:
        print("Access denied")

check_credentials(username, password)
