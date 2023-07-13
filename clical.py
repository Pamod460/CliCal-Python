print("---------------Calculator---------------")
while True:
    num1 = float(input("Enter first Number :"))
    num2 = float(input("Enter second Number :"))
    opt = input("Enter 1 for the Addition 2 for the Subtraction 3 for the multiplication 4 for the Division 5 For Exit : ")
    answer = ""
    match opt:
        case "1":
            answer = num1+num2
        case "2":
            answer = num1-num2
        case "3":
            answer = num1*num2 
        case "4":
            answer = num1/num2
        case "5":
            break
    print(answer)


