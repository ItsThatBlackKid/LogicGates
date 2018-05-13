userInput = input("Enter a binary input: ")
userOutput = ""

for i in range(0, len(userInput)):
    if userInput[i] == "0":
        userOutput += "1"
    else:
        userOutput += "0"

print(userOutput)
