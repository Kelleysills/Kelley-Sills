
print ("Messaging System")
username = input("Username : ")
print ("")
password = input("Password : ")

print ("")


def main():
    if username == "User1" and password == "m89jklmo6":
        print ("*****Access Granted****")
        print ("")
        print ("*****Welcome User1*****")
        print ("Connected with User2")
        print ("")

    elif username == "User2" and password == "password123":
        print ("*****Access Granted****")
        print ("")
        print ("*****Welcome User2*****")
        print ("Connected with User1")
        print ("")

    else:
        print ("*****Access Denied*****")
        import time
        time.sleep(4)
        import os
        os.system("clear")
        quit()


    sender1 = input("Enter message here : ")
    print("")
    name1 = input("Enter your contact : ")
    print("")
    send = input("Would you like to send? : ")

    if send == "yes" or "Yes" and username == "User1" and password == "m89jklmo6":
            print ("User1 : Message Sent to : ", name1, sender1)



    elif send == "yes" or "Yes" and username == "User2" and password == "password123":
            print ("User2 : Message Sent to : ", name1, sender1)




    if username == "User1" and password == "m89jklmo6" or username == "User2" and password == "password123":
        Continue = input("Quit or New message? 1/2 : ")
        if Continue == "1" and username == "User1" and password == "m89jklmo6":
            import os
            os.system("clear")
            quit()
        if Continue == "2" and username == "User1" and password == "m89jklmo6":
            import time
            time.sleep(2)
            main()
        elif Continue == "1" and username == "User2" and password == "password123":
            import os
            os.system("clear")
            quit()
        elif Continue == "2" and username == "User2" and password == "password123":
            import time
            time.sleep(2)
            main()
        else:
            print ("You are being logged out for invalid user info")
            import time
            time.sleep(2)
            import os
            os.system("clear")
            quit()

if __name__ == "__main__":
    main()
