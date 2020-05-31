import math

# TO DO
# Implement Loop to allow multiple claim/user input
# Implement lists to track number of each client type input (P/C)
# Implement lists to track total premiums of each type (P/C)
# Implement error checking

def privateHousing():
    premiumRate = 0
    premiumCharged = 0
    amountInsured = int(input("Amount Insured ($) ? "))
    proCharge = 50
    numClaims = int(input("Number of claims ? "))
    noClaimBonusRate = 0.1
    noClaimBonus = 0

    if amountInsured < 100000:
        premiumRate = 0.003

        premiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 100000:
        premiumRate = 0.0025

        premiumCharged = (amountInsured * premiumRate) + proCharge

    if numClaims == 0:
        noClaimBonus = premiumCharged * noClaimBonusRate

        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("No Claim Bonus = " + "$" + str(noClaimBonus))
        print("Premium = " + "$" + str(premiumCharged - noClaimBonus))
        return premiumCharged

    elif numClaims >= 1:
        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("Premium = " + "$" + str(premiumCharged + noClaimBonus))
        return premiumCharged




def commercialProperty():
    premiumRate = 0
    premiumCharged = 0
    amountInsured = int(input("Amount Insured ($) ? "))
    proCharge = 80
    numClaims = int(input("Number of claims ? "))
    noClaimBonusRate = 0.15
    noClaimBonus = 0

    if amountInsured < 250000:
        premiumRate = 0.005

        premiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 250000:
        premiumRate = 0.0075

        premiumCharged = (amountInsured * premiumRate) + proCharge

    if numClaims == 0:
        noClaimBonus = premiumCharged * noClaimBonusRate

        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("No Claim Bonus = " + "$" + str(noClaimBonus))
        print("Premium = " + "$" + str(premiumCharged - noClaimBonus))
        return premiumCharged

    elif numClaims >= 1:
        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("Premium = " + "$" + str(premiumCharged + noClaimBonus))
        return premiumCharged

# use of a main() function to keep code a little more clean.
# I am not considering the main() function as one of the 2 defined and called functions.


def main():
    try:
        usrType = input("User type(P/C)? ")

        if usrType == "P" or usrType == "p":
            privateHousing()

        elif usrType == "C" or usrType == "c":
            commercialProperty()

        else:
            print("Please enter a valid user type")
    except:
        print("An Error has occurred")


if __name__ == "__main__":
    main()

