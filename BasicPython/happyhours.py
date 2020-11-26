import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you kicked out of game",
          "Kanye West",
          "Samuel L. Jackson",
          "Locisco"]



random_bar = random.choice(bars)
random_person1 = random.choice(people)
random_person2 = random.choice(people)

print("How about you go to {0} with {1} and {2}".format(random_bar,random_person1,random_person2))


