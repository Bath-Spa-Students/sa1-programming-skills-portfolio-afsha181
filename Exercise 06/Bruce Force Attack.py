# WE chose this as our passcode
passcode = "54321"

# the player will have minimum attempts
tottal_atemps = 5

# the number of attempts in the start
attempts = 0

# using While loop so it keeps asking about the passcode
while attempts < tottal_atemps:
    # asking the player to enter the passcode
    entered_passcode = input("Enter the passcode: ")
   
    # checking if the entered password is correct
    if entered_passcode == passcode:
        print("PASSCODE IS CORRECT, YOU MAY ENTER.")
        break
    else:
        # plus 1 to the attempts counter
        attempts += 1
        # Inform the player how many attempts they have left.
        remainingattempts = tottal_atemps - attempts
        if remainingattempts > 0:
            print(f"THE PASSCODE IS INCORRECT. You have {remainingattempts} attemps left.")
        else:
            print("YOUR ACCESS WAS DENIED PASSWORD IS INCORRECT, SYSTEM IS ALERTED NOW.")