def prime_or_composite(n):
    # prime numbers are greater than 1
    if n==1:
        return False
    for z in range(2,int(n/2)):
        if n%z==0:
            return False
            break
    else:
        return True
    pass

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))

    for x in range(12):
        if answers[x] == True:
            print(numbers[x], " is a Prime Number")
        else:
            print(numbers[x], "is not a Prime Number")


    print(answers)