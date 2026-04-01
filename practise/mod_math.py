def check_luhn(card_no):
    s = 0
    double = False
    
    # Loop from rightmost digit to left
    for digit_char in reversed(card_no):
        digit = int(digit_char)
        
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        s += digit
        double = not double  # flip True/False each iteration
    
    return s % 10 == 0

# Example usage:
if __name__ == "__main__":
    card_number = "8567092850987305"
    if check_luhn(card_number):
        print(f"{card_number} is valid.")
    else:
        print(f"{card_number} is invalid.")


  # Example 2:
    card_number2 = "1234567812345670"
    if check_luhn(card_number2):
        print(f"{card_number2} is valid.")
    else:
        print(f"{card_number2} is invalid.")

  # Example 3:
    card_number3 = "4539148803436467"
    if check_luhn(card_number3):
        print(f"{card_number3} is valid.")
    else:
        print(f"{card_number3} is invalid.")