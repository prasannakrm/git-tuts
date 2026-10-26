```python
ones = [
    "zero", "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen"
]
tens = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

def number_in_words(number):
    if number < 20:
        return ones[number]
    if number < 100:
        return tens[number // 10] + (
            "-" + ones[number % 10] if number % 10 else ""
        )
    return "one hundred"

for number in range(1, 101):
    print(number, number_in_words(number))
```