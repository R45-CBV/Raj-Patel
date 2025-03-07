roman_numerals = {
    3000: "MMM", 2000: "MM", 1000: "M", 900: "CM", 700: "DCC", 600: "DC", 
    500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
    10: "X", 9: "IX", 7: "VII", 5: "V", 4: "IV", 1: "I"
}

while True:
    user_input = input("Enter an integer between 1 and 3999: ")
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        continue
    
    user_input = int(user_input)
    
    if not (1 <= user_input <= 3999):
        print("Out of range. Please enter a number between 1 and 3999.")
        continue
    
    roman_string = ""
    for value, symbol in roman_numerals.items():
        while user_input >= value:
            roman_string += symbol
            user_input -= value
    
    print(f"Roman numeral: {roman_string}")
    break