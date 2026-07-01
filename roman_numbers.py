class RomanConverter:

    def convert(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        roman = ""

        for i in range(len(values)):
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]

        return roman


number = int(input("Enter an integer (1-3999): "))

if number < 1 or number > 3999:
    print("Please enter a number between 1 and 3999.")
else:
    obj = RomanConverter()
    result = obj.convert(number)
    print("Roman Numeral:", result)