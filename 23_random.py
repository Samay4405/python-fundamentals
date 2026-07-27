import random

# number = random.randint(1, 8)     # to get random no. between 1 and 8 .

# print(number)                      # printing the generated random number.

low = 1
high = 100
options = ("rock", "papers", "sissors")
cards = ["2", "3", "4", "5", "6", "7","8","9","10","J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()          # will print any random no.


# option = random.choice(options)
random.shuffle(cards)
print(cards)
