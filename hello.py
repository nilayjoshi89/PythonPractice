number: int = int(input("Enter Number:\n"))
print("Number is :" + str(number))

answer = 1

while number > 0:
    answer = answer * number
    number -= 1

print(answer)
