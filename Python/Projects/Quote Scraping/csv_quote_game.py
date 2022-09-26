# http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print(f"Here's a quote: \n {quote['text']}")
    # print(quote["author"]) check if loop works
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who do you think I am? Guesses remaining: {remaining_guesses}\n")
        res = requests.get(f"{base_url}{quote['bio']}")
        soup = BeautifulSoup(res.text, "html.parser")
        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        print_hint(quote, remaining_guesses)

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)")
    if again.lower() in ('y', 'yes'):
        print("Okay, let's play again")
        return start_game(quotes)
    else:
        print("Okay, goodbye!")


def print_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        birth_date = soup.find(class_='author-born-date').get_text()
        birth_place = soup.find(class_='author-born-location').get_text()
        print(f"Here's a hint: The author was born on {birth_date} {birth_place}.")
    elif remaining_guesses == 2:
        last_initial = quote["author"].split(" ")[1][0]
        print(f'Here"s another hint: Their initials are {quote["author"][0]}.{last_initial}..')
    elif remaining_guesses == 1:
        paragraph = soup.find(class_="author-description").get_text()
        sentences = [p for p in map(str.strip, paragraph.split('.')) if p]
        # More likely to reveal last name in bio so removes it
        # Need to figure out how to remove first, last, and whole name in sentence
        sentence = choice(sentences).removeprefix(quote["author"].split(' ')[1])
        print(f"Last hint! Here's a sample from their bio:\n{sentence}.")
    else:
        print(f"Sorry you ran out of guesses. The author was {quote['author']}.")


quotes = read_quotes('quotes.csv')
start_game(quotes)
