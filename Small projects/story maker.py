import random

def generate_story():
    print("Let's create your own story!")

    adjectives = [input("Enter an adjective: ") for _ in range(3)]
    nouns = [input("Enter a noun: ") for _ in range(3)]
    verbs = [input("Enter a verb: ") for _ in range(3)]
    places = [input("Enter a place: ") for _ in range(3)]
    adjective2 = input("Enter another adjective: ")
    items = [input("Enter an item: ") for _ in range(3)]

    story_templates = [
        "Once upon a time, in a {adj1} land, there was a {noun1} who loved to {verb1}. One day, they decided to visit {place1}. It was a {adj2} place, filled with {item1}. The {noun1} spent the day exploring and enjoying the beauty of {place1}. And so, the {noun1} lived happily ever after with their beloved {item1}.",

        "In a {adj1} {place1}, there lived a {adj2} {noun1}. This {noun1} loved to {verb1} and owned a magical {item1}. One day, they decided to {verb2} to {place2}. Along the way, they encountered a {adj3} {noun2} who offered to join their adventure. Together, they journeyed to {place2} and discovered the true power of the magical {item1}.",

        "Long ago in the {adj1} kingdom of {place1}, a {noun1} with a {adj2} {item1} embarked on a quest to {verb1}. Along the way, they met a {adj3} {noun2} who shared tales of a mystical {place2}. Intrigued, they decided to change their course and explore the wonders of {place2}. Little did they know, the journey would bring unexpected {item2} and unforgettable memories."
    ]

    selected_template = random.choice(story_templates)
    story = selected_template.format(
        adj1=random.choice(adjectives),
        noun1=random.choice(nouns),
        verb1=random.choice(verbs),
        place1=random.choice(places),
        adj2=adjective2,
        item1=random.choice(items),
        verb2=random.choice(verbs),
        place2=random.choice(places),
        adj3=random.choice(adjectives),
        noun2=random.choice(nouns),
        item2=random.choice(items)
    )

    print("\nYour Story:")
    print(story)

if __name__ == "__main__":
    generate_story()
