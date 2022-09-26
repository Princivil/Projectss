# http://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com"


def scrape_quotes():
    # create list to append quotes
    url = "/page/1"
    all_quotes = []
    # Web Scraping portion
    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Now Scraping: {base_url}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),  # want inner text not span
                "author": quote.find(class_="author").get_text(),
                "bio": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(2)
    return all_quotes


# print(all_quotes)

# Guessing Game Portion
def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print(f"Here's a quote: \n {quote['text']}")
    print(quote["author"])  # check if loop works
    guess = ""
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who do you think I am? Guesses remaining: {remaining_guesses}\n")
        res = requests.get(f"{base_url}{quote['bio']}")
        soup = BeautifulSoup(res.text, "html.parser")
        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
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
            sentence = choice(sentences).removeprefix(
                quote["author"].split(' ')[1])  # more likely to see last name in bio, so removes it
            print(f"Last hint! Here's a sample from their bio:\n{sentence}.")
        else:
            print(f"Sorry you ran out of guesses. The author was {quote['author']}.")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again? (y/n)")
    if again.lower() in ('y', 'yes'):
        print("Okay, let's play again")
        return start_game(quotes)
    else:
        print("Okay, goodbye!")


start_game(quotes)
