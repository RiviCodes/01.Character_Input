"""
Exercise 1

- Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.

Extras:

- Add on to the previous program by asking the user for another number and printing out that many
copies of the previous message. (Hint: order of operations exists in Python)
- Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)

"""

user_name = input('Please, type your name: ')
user_age = int(input('Now, type your age: '))
current_year = int(input('Finally, what year is it currently?: '))
years_left = 100 - user_age
years_old = years_left + current_year

# Here is the extra step

print_attempts = int(input('EXTRA: How many times do you want to print the answer? (1,2,5,etc): \n'))

for i in range(print_attempts):

    print(f'Your name is {user_name}, your current age is {user_age}')
    print(f'And in {years_old} you will (or would) be 100 years old!\n')