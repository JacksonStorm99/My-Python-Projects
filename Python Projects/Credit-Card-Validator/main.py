def is_valid_credit_card(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    # Check if the card number is all digits
    if not card_number.isdigit():
        return False
    # Check if the card number is the correct length
    if len(card_number) != 16:
        return False
    # Check if the card number passes the Luhn algorithm
    return luhn_check(card_number)

def luhn_check(card_number):
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Double every second digit
            n *= 2
            if n > 9:  # Subtract 9 if the result is greater than 9
                n -= 9
        total += n
    return total % 10 == 0
