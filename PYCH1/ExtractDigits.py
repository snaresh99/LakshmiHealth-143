# Extraction of Digits

def extracting_digits(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        remaining_value = remaining_value // 10
        print(digit, end=' ')
    print()

if __name__ == "__main__":
    extracting_digits(12345)
    