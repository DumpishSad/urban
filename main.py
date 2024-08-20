first = input('input first number: ')
second = input('input second number: ')
third = input('input third number: ')

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

