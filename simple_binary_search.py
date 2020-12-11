number_list = [x*2 for x in range(1, 51)]

while True:
    try:
        user_input = int(input("Give me a number to quickly find in the list: "))
        break
    except ValueError:
        print("That's not a number, try again!")

iteration = 0
while True:
    if user_input == number_list[0]:
        print(f"Found the number! The number is: {number_list[0]}")
        break
    elif len(number_list) == 1 and number_list[0] != user_input:
        print("Couldn't find the number in the list.")
        break

    if user_input >= number_list[len(number_list)//2]:
        number_list = number_list[len(number_list)//2:]
        print(number_list)
    else:
        number_list = number_list[:len(number_list)//2]
        print(number_list)
    iteration += 1
print(f"Number found in {iteration} iterations.")