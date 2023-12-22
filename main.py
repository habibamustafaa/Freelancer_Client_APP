import Client
import Freelancer

print("--------------------------------")
print("| welcome on Freelancer System |")
print("--------------------------------")
while True:
    a = input("If you are a freelancer choose (1) or a client choose (2) choose (3) to exit\n")
    if a == "1":
        while True:

            b = input("choose (1) to register or (2) to login  or (3) to exit\n")
            if b == "1":
                Freelancer.register_freelancer()
            elif b == "2":
                if Freelancer.login_freelancer():
                    print("login successfully")
                    Freelancer.freelancer_menu()
            elif b == "3":
                break
            else:
                print("invalid choice please try again")
    elif a == "2":
        while True:
            c = input("choose 1 to register or 2 to login  or 3 to exit\n")
            if c == "1":
                Client.register_client()
            elif c == "2":
                if Client.login_client():
                    Client.client_menu()
            elif c == "3":
                break
    elif a == "3":
        break
    else:
        print("invalid choice please choose again")
