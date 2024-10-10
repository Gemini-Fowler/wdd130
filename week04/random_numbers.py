import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(words)
    print(words)
    append_random_words(words, 3)
    print(words)

def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        random_number = float(random.uniform(1,100))
        round_number = round(random_number, 1)
        numbers_list.append(round_number)

def append_random_words(words_list, quantity = 1):
    starting_list = ['Team', 'Michael', 'Jonas', 'Victor', 'Joseph']
    for _ in range(quantity):
        random_word = random.choice(starting_list)
        words_list.append(random_word)

if __name__ == '__main__':
    main()






















