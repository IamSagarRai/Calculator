# A simple calculator program which performs basic functions!

while True:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    
    print(num_1, "+", num_2, "=", num_1+num_2)
    print(num_1, "-", num_2, "=", num_1-num_2)
    print(num_1, "/", num_2, "=", num_1/num_2)
    print(num_1, "*", num_2, "=", num_1*num_2)
    print(num_1, "%", num_2, "=", num_1%num_2)
