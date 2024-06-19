# Find proper divisor
def find_proper_divisors(value):
    print("To find the proper divisors for a number %d", value)
    divisors = [1]
    limit = value//2+1
    print("The limit value to run for loop is %d", limit)
    for i in range(2, limit):
        print("This is the i value %d and if condition is %d", i, (value%i))
        if value % i == 0:
            divisors.append(i)
            print("find_proper_divisors each number %d", divisors)
        return divisors
    
def find_pd(value):
    print("To find the proper divisors for a number %d", value)
    div = [1]
    limit = value//2 + 1
    for j in range(2, limit):
        #print("the vlaue of j is %d", j)
        if value % j == 0:
            div.append(j)
    return div

    
if __name__ == "__main__":
    divisor = find_proper_divisors(99)
    print("The divisors of the number  are %d", divisor)

    test = find_pd(99)
    print(test)
