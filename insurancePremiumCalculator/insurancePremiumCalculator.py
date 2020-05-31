import math

def privateHousing():
    premiumRate = 0
    premiumCharged = 0
    amountInsured = int(input("How much are you getting insured? "))

    if amountInsured < 100000:
        premiumRate = 0.003

        premiumCharged = amountInsured * premiumRate

    elif amountInsured >= 100000:
        premiumRate = 0.0025

        premiumCharged = amountInsured * premiumRate

    return premiumCharged

#use of a main() function to keep code a little more clean.
#I am not considering the main() function as one of the 2 defined and called functions.
def main():
    print(privateHousing())

if __name__ == "__main__":
    main()