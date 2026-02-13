def addTwo():
    num = int(input("Enter a number"))
    result1 = num + 2 
    # print(result) 
    return result1

def multiplyByFive(num):
    result2 = num * 5 
    # print(result2)
    return result2

continue_game = "YES"
while continue_game == "YES":
    num = addTwo()
    print(multiplyByFive(num))
    continue_game = input("do you want to play again?").upper() 

print("Thanks for playing!")

