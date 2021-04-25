def vowels(word):
    for letter in word:
        if (letter in "AaEeIiOoUu"):
            print(letter,end=" ")

vowels("I like tomatoes")