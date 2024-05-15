while True:
    user_name = input("What is your name? (Please input below:)\n")
    the_reason = input("Why do you love programing? (Please input below:)\n")
    the_record = "The reason why " + user_name + " loves programing is: \"" + the_reason + "\"\n"

    with open("guestbook.txt", "a") as f:
        f.write(the_record)