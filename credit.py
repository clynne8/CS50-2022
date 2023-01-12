from cs50 import get_int


def main():
    while True:
        credit_card = get_int("Number: ")
        if credit_card >= 0:
            # look for the vaild case here and break
            break
    if check_validity(credit_card):
        print_card_brand(credit_card)
    else:
        print("INVALID")


def check_validity(ccn):
    return checksum(ccn)


def checksum(ccn):

    sum = 0
    # trying to convert ccn into a string
    for i in range(len(str(ccn))):
        if (i % 2 == 0):
            sum += ccn % 10
        else:
            # 2 * 9 = 18
            digit = 2 * (ccn % 10)
            # now we need to take 18 and break it
            # as 1 + 8
            sum += digit // 10 + digit % 10

        ccn //= 10

    return sum % 10 == 0


def print_card_brand(ccn):
    # ccn begins with either 34 or 37
    if (ccn >= 34e13 and ccn < 35e13) or (ccn >= 37e13 and ccn < 38e13):
        print("AMEX")
    # ccn begins with either 51,52,53,54, or 55
    elif ccn >= 51e14 and ccn < 56e14:
        print("MASTERCARD")
    elif (ccn >= 4e12 and ccn < 5e12) or (ccn >= 4e15 and ccn < 5e15):
        print("VISA")
    else:
        print("INVALID")


# python's way of running the main function
if __name__ == "__main__":
    main()
