userInput1 = input("Enter a binary input: ")
userInput2 = input("Enter a second binary input: ")
userOutput = ""

for i in range(0, len(userInput1)):
    if userInput1[i] == "1" and userInput2[i] == "1":
        userOutput += "1"
    else:
        userOutput += "0"

print(userOutput)
