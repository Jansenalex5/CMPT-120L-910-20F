
##Question_1
def addRange(num):
    sum=0
    for x in range(num):
        sum=sum+x
    sum= sum + num
    return sum

#Question2

def main():
    myNum = int(input("Please enter a number: "))
    print(addRange(myNum))

main()