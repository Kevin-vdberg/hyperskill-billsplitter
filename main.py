import random

#init constants and variables
WELCOME_MESSAGE: str = 'Enter the number of friends joining (including you): '
NO_ONE_JOINING_MESSAGE: str = 'No one is joining for the party'
PEOPLE_JOINING_MESSAGE: str = 'Enter the name of every friend joining (including you), each on a new line: '
LUCKY_FUNCTION_MESSAGE: str = 'Do you want to use the "Who is lucky?" feature? Write Yes/No: '
NO_LUCKY_PERSON_MESSAGE: str = 'No one is going to be lucky'
LUCKY_PERSON_MESSAGE: str = ' is the lucky one!'

people_names = []

#Program
number_of_people = int(input(WELCOME_MESSAGE))

def calculate_price_per_person(total_amount: float, people: int) -> float:
    return round((total_amount/people),2)


if number_of_people > 0:
    print(PEOPLE_JOINING_MESSAGE)

    for n in range(number_of_people):
        people_names.append(input())

    people_joining = dict.fromkeys(people_names,0)

    #Ask for the bill amount and calculate price per person
    bill_amount = float(input('Enter the total bill value'))
    split_amount = calculate_price_per_person(bill_amount,number_of_people)

    people_joining = {key: split_amount for key in people_joining.keys()}

    use_lucky_function = input(LUCKY_FUNCTION_MESSAGE) == 'Yes'

    if use_lucky_function:
        lucky_person = random.choice(people_names)
        print(lucky_person + LUCKY_PERSON_MESSAGE)

        if number_of_people != 2:
            new_price = calculate_price_per_person(bill_amount,number_of_people - 1)
        else:
            new_price = bill_amount

        for key in people_joining.keys():
            if key == lucky_person:
                people_joining[key] = 0
            else:
                people_joining[key] = new_price


    else:
        print(NO_LUCKY_PERSON_MESSAGE)


    print(people_joining)

else:
    print (NO_ONE_JOINING_MESSAGE)


