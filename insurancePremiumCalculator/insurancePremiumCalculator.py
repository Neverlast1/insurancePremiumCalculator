
# This Program was written by Joel Busch
# This Program accepts user input, calculates premium on a given amount insured, prints each individual clients priemium
# And then prints a summary of all the premiums collected.

# using functions to calculate premiums and no claim bonus
def privateHousing():

    # I have made use of Zero initializing multiple variables.
    # This allows me to re-assign their values when needed and where appropriate.

    premiumRate = 0  # The rate (%) at which the premium is calculated.
    global privPremiumCharged  # The premium amount ($). Global to allow use in the main() function (Note: This is bad)
    amountInsured = int(input("Amount Insured ($) ? "))  # Asking user for input of Amount insured.
    proCharge = 50  # Static Processing charge./
    numClaims = int(input("Number of claims ? "))  # Asking user for input of the Number of Claims.
    noClaimBonusRate = 0.1  # Static rate if the client has No Claims.
    noClaimBonus = 0  # The Amount($) to reduce the premiumCharged if client is eligible.

    # This if/elif statement checks the insured amount and applies the correct premium rate
    if amountInsured < 100000:
        premiumRate = 0.003

        privPremiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 100000:
        premiumRate = 0.0025

        privPremiumCharged = (amountInsured * premiumRate) + proCharge

    # this if/elif statement checks the number of claims and applies the correct No Claim Bonus Rate
    if numClaims == 0:
        noClaimBonus = privPremiumCharged * noClaimBonusRate

        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("No Claim Bonus = " + "$" + str(noClaimBonus))
        print("Premium = " + "$" + str(privPremiumCharged - noClaimBonus))
        privPremiumCharged = privPremiumCharged - noClaimBonus


    elif numClaims >= 1:
        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("Premium = " + "$" + str(privPremiumCharged + noClaimBonus))


def commercialProperty():

    # I have made use of Zero initializing multiple variables.
    # This allows me to re-assign their values when needed and where appropriate.

    premiumRate = 0  # The rate (%) at which the premium is calculated.
    global comPremiumCharged  # The premium amount ($). Global to allow use in the main() function
    amountInsured = int(input("Amount Insured ($) ? "))  # Asking user for input of Amount insured.
    proCharge = 80  # Static Processing charge.
    numClaims = int(input("Number of claims ? "))  # Asking user for input of the Number of Claims.
    noClaimBonusRate = 0.15  # Static rate if the client has No Claims.
    noClaimBonus = 0  # The Amount($) to reduce the premiumCharged if client is eligible.

    # This if/elif statement checks the insured amount and applies the correct premium rate
    if amountInsured < 250000:
        premiumRate = 0.005

        comPremiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 250000:
        premiumRate = 0.0075

        comPremiumCharged = (amountInsured * premiumRate) + proCharge

    # this if/elif statement checks the number of claims and applies the correct No Claim Bonus Rate
    if numClaims == 0:
        noClaimBonus = comPremiumCharged * noClaimBonusRate

        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("No Claim Bonus = " + "$" + str(noClaimBonus))
        print("Premium = " + "$" + str(comPremiumCharged - noClaimBonus))
        comPremiumCharged = comPremiumCharged - noClaimBonus

    elif numClaims >= 1:
        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("Premium = " + "$" + str(comPremiumCharged + noClaimBonus))


try:
    # I have made use of Zero initializing multiple variables.
    # This allows me to re-assign their values when needed and where appropriate.

    cont = "y"  # "continue" variable used to break while loop.
    privTotal = 0  # Adds the together each iteration of the privPremiumCharged
    comTotal = 0  # Adds the together each iteration of the comPremiumCharged
    numPriv = 0  # Counts the number of Private Clients Processed.
    numCom = 0  # Counts the number of Commercial clients Processed.

    while cont == "y":  # This while statement loops through the main process while i =

        usrType = input("User type(P/C)? ")  # Ask's user to input client type, Private or Commercial.

        # This if/elif statement checks the User type.
        # If anything other than P,p,C,c is input, it throws an error.
        # I have also specifically allowed both upper and lower case.
        if usrType == "P" or usrType == "p":
            privateHousing()
            privTotal = privTotal + privPremiumCharged
            numPriv += 1

        elif usrType == "C" or usrType == "c":
            commercialProperty()
            comTotal = comTotal + comPremiumCharged
            numCom += 1

        else:
            print("Invalid User type")

        # This if statement checks to see if the program is still in the loop.
        # And ask's the user if they want to input another client.
        if cont == "y":
            askCont = input("\nAnother client y/n? ")  # used to ask input if they want to continue.
            # This if statement checks the user input, and checks if it's a valid entry.
            # and changes cont to to either n (to break loop) or y (to continue loop)
            if askCont == "n" or askCont == "N":
                cont = "n"
            elif askCont == "y" or askCont == "Y":
                cont = "y"
            else:
                raise TypeError

    print("Session Summary:\n")
    print("Number of Private Clients: " + str(numPriv))
    print("Total Private client Premiums collected = " + "$" + str(privTotal))
    print("Number of Commercial Clients = " + str(numCom))
    print("Total Commercial client Premiums collected = " + "$" + str(comTotal))

except TypeError:
    print("Invalid Input Type")
finally:
    print("\nProgram Ended")
    exit()
