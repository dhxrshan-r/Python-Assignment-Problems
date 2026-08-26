import random

def make_birthdays(num_people):
    birthdays = []
    for person in range(num_people):
        birthdays = birthdays + [random.randint(1, 365)]
    return birthdays

def duplicate_exists(birthdays):
    for i in range(len(birthdays)):
        for j in range(i+1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False

print(duplicate_exists([3, 100, 45])) 
print(duplicate_exists([44, 1, 237, 198, 44]))

def calculate_birthday_odds(num_people):
    trials = 10000
    duplicate_count = 0
    for trial in range(trials):
        birthdays = make_birthdays(num_people)
        if duplicate_exists(birthdays):
            duplicate_count += 1
    return duplicate_count / trials
print(calculate_birthday_odds(23))
