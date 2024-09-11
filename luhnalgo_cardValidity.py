class Card:
    def __init__(self, card_number: str):
        self.card_number = card_number

    def isvalid(self) -> bool:
        """ Return True if card number is valid. """

        # Split digits, multiply by 2 every other number (start from the beginning)
        # Add the result to sum_cn_list, add directly the digit that was not doubled
        cn_list = [digit for digit in self.card_number]
        sum_cn_list = 0

        for i in range(len(cn_list)):
            if (i % 2) == 1:
                sum_cn_list += int(cn_list[i])
                continue
            else:
                doubled_digit = int(cn_list[i]) * 2

                if doubled_digit <= 9:
                    sum_cn_list += doubled_digit
                else:
                    sum_split_digits = sum([int(j) for j in str(doubled_digit)])
                    sum_cn_list += sum_split_digits

        if (sum_cn_list % 10) != 0:
            return False
        return True


while True:
    user_card = str(input("Enter your 16-digit card number: "))

    if len(user_card) > 16:
        print("Your card number exceeds limit.")
    else:
        card1 = Card(user_card)
        print(card1.isvalid())

        retry = str(input("One more try? y/n: "))

        if retry.lower() == 'y':
            continue
        elif retry.lower() == 'n':
            exit()
        else:
            print("Invalid input.")
            exit()
