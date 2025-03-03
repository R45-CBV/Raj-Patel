roman = input("Enter a Roman numeral: ")
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'XX':20, 'L': 50, 'XC':60, 'C': 100, 'D': 500, 'M': 1000}

total = 0
prev_value = 0

for num in reversed(roman):
    current_value = roman_dict[num]
    
    if current_value < prev_value:
        total -= current_value
    else:
        total += current_value
    
    prev_value = current_value

print(f"The integer value of {roman} is {total}")
print
