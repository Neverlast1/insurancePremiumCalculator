import math

# TO DO
# Implement lists to track total premiums of each type (P/C)
# Implement error checking


# using functions to calculate premiums and no claim bonus
def privateHousing():

    # I have made use of Zero initializing multiple variables.
    # This allows me to re-assign their values when needed and where appropriate.

    premiumRate = 0  # The rate (%) at which the premium is calculated.
    premiumCharged = 0  # The premium amount ($).
    amountInsured = int(input("Amount Insured ($) ? "))  # Asking user for input of Amount insured.
    proCharge = 50  # Static Processing charge.
    numClaims = int(input("Number of claims ? "))  # Asking user for input of the Number of Claims.
    noClaimBonusRate = 0.1  # Static rate if the client has No Claims.
    noClaimBonus = 0  # The Amount($) to reduce the premiumCharged if client is eligible.

    # This if/elif statement checks the insured amount and applies the correct premium rate
    if amountInsured < 100000:
        premiumRate = 0.003

        premiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 100000:
        premiumRate = 0.0025

        premiumCharged = (amountInsured * premiumRate) + proCharge

    # this if/elif statement checks the number of claims and applies the correct No Claim Bonus Rate
    if numClaims == 0:
        noClaimBonus = premiumCharged * noClaimBonusRate

        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("No Claim Bonus = " + "$" + str(noClaimBonus))
        print("Premium = " + "$" + str(premiumCharged - noClaimBonus))


    elif numClaims >= 1:
        print("\nPremium Summary")
        print("Amount Insured = " + "$" + str(amountInsured))
        print("Number of Claims = " + str(numClaims))
        print("Premium = " + "$" + str(premiumCharged + noClaimBonus))

    return premiumCharged

    # We always return the premiumCharged variable to calculate the total $ collected of each user type (P/C)



def commercialProperty():

    # I have made use of Zero initializing multiple variables.
    # This allows me to re-assign their values when needed and where appropriate.

    premiumRate = 0  # The rate (%) at which the premium is calculated.
    premiumCharged = 0  # The premium amount ($).
    amountInsured = int(input("Amount Insured ($) ? "))  # Asking user for input of Amount insured.
    proCharge = 80  # Static Processing charge.
    numClaims = int(input("Number of claims ? "))  # Asking user for input of the Number of Claims.
    noClaimBonusRate = 0.15  # Static rate if the client has No Claims.
    noClaimBonus = 0  # The Amount($) to reduce the premiumCharged if client is eligible.

    # This if/elif statement checks the insured amount and applies the correct premium rate
    if amountInsured < 250000:
        premiumRate = 0.005

        premiumCharged = (amountInsured * premiumRate) + proCharge

    elif amountInsured >= 250000:
        premiumRate = 0.0075

        premiumCharged = (amountInsured * premiumRate) + proCharge

    # this if/elif statement checks the number of claims and applies the correct No Claim Bonus Rate
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

    # We always return the premiumCharged variable to calculate the total $ collected of each user type (P/C)


# use of a main() function to keep code a little more clean.


def main():
    try:
        i = bool(0)
        while i == 0:
            usrType = input("User type(P/C)? ")  # Ask's user to input client type, Private or Commercial.
            numPriv = 0
            numCom = 0
            privTotal = 0
            comTotal = 0

            # This if/elif statement checks the User type.
            # If anything other than P,p,C,c is input, it throws an error.
            # I have also specifically allowed both upper and lower case.
            if usrType == "P" or usrType == "p":
                privateHousing()
                numPriv += 1

            elif usrType == "C" or usrType == "c":
                commercialProperty()
                numCom += 1

            else:
                print("Invalid User type")

            if i == 0:
                cont = input("\nAnother client y/n? ")
                if cont == "n" or cont == "N":
                    i = 1

            print(privTotal)

    except:
        print("An Error has occurred")


if __name__ == "__main__":  # This calls the main() function
    main()

