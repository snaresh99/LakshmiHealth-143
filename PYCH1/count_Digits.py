def count_digits(number):
    count = 0
    remaining_value = number
    while remaining_value > 0:
        remaining_value = remaining_value // 10
        count += 1
    return count

if __name__ == "__main__":
    count = count_digits(999999999999999999999999)
    print("Number of digits in given number are %d", count)