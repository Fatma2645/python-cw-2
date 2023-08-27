my_name = input('enter your name')
my_age =input('enter your age')
print(f'my name is {my_name}and i am {my_age} years old')


first_number=int(input('enter first number'))
second_number=int(input('enter second number'))
operator= input("what would you like to do?")

if operator=="+":
     print(first__num + second_num)
elif operator=="-":
        print(first_num-second_num)
elif operator=="*":
        print(first_num * second_num)
elif operator=="/":
        prinr(first_num/second_num)


bus_capacity=80
people_in=int(input("how many passegngers inside the bus?"))
people_out=int(input("how many new passengers?"))
empty_seats = bus_capacity - people_in 

if empty_seats>people_out:
    print(f"there are {empty_seats}available seasts")
elif empty_seats<=people_out:
    print("sorry the bus is full")
    