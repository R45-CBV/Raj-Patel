dict = int(input("Enter an integer: "))
roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 20: 'XX',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

for i in roman_numerals:
    for value, numeral in roman_numerals.items():
        while dict >= value:
            print(numeral, end='')  
            dict -= value            
            