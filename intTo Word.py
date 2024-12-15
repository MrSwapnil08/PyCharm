def number_to_words(num):
    if num == 0:
        return "zero"

    # Define words for ones, tens, and teens
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
             "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion",
                 "trillion", "quadrillion", "quintillion",
                 "sextillion", "septillion", "octillion",
                 "nonillion", "decillion"]

    def three_digit_to_words(n):
        """Convert a number up to 999 into words."""
        word = ""
        if n >= 100:
            word += ones[n // 100] + " hundred"
            n %= 100
            if n > 0:
                word += " and "
        if 10 < n < 20:
            word += teens[n - 10]
        else:
            if n >= 20:
                word += tens[n // 10]
                n %= 10
                if n > 0:
                    word += "-"
            if n > 0:
                word += ones[n]
        return word

    # Handle negative numbers
    is_negative = num < 0
    num = abs(num)

    # Split number into groups of three digits
    num_str = str(num)
    num_groups = []
    while num_str:
        num_groups.insert(0, int(num_str[-3:]))
        num_str = num_str[:-3]

    # Convert each group into words
    result = ""
    for i, group in enumerate(num_groups):
        if group > 0:
            if result:
                result += ", "
            result += three_digit_to_words(group)
            if i < len(thousands):
                result += " " + thousands[len(num_groups) - i - 1]

    if is_negative:
        result = "negative " + result

    return result.strip()

# Input from the user
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        print(f"{user_input} in words: {number_to_words(user_input)}")
    except ValueError:
        print("Please enter a valid integer.")
