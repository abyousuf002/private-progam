list1 = ['shifa loves aydin zarif']
list2 = ['zarif shifa']
list3 = [ 'jarif loves shifa']


user_input = int(input('Enter number (1, 2, or 3): '))


if user_input == 1:
    print(list1)
elif user_input == 2:
    print(list2)
elif user_input == 3:
    print(list3)
else:
    print("Invalid input. Please enter 1, 2, or 3.")