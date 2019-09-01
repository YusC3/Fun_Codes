"""
This is a code created for random fun based on ideas
discussed @ an Interview.

Pig-Latin Ver. 1.01

Info: Performs Pig Latin translation based on pig latin rules based on
http://www.piglatin.org/pig_latin_rules.
"""
#Libraries used:

print("Turn your text into Pig Latin!")
print("Type in a word or a sentence to see what happens!")
print("\n")
print(" - - - - - - - - - - - - - - - - -")
print("\n")
print("RULES: ")
print("\n")
print("""
1. NO NUMBERS \n
2. NO PUNCTUATION \n
3. NO UNSUAL CHARACTERS (english only please :) )
""")
print("\n")

print("""
For more information on Pig Latin, visit:
http://www.piglatin.org/pig_latin_rules
""")

def pig_latin(word):
    """
    This function takes a word and Pig-Latin-afies's it.
    fun.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    pig_phrase_1 = "ay"
    pig_phrase_2 = "way"
    word_len = len(word)

    i = 1
    #check if first character is a vowel
    if word[0] in vowels:
        pig_latin_word = word + pig_phrase_2
        
    elif word[0] not in vowels:
    #creation of pig latin word
        letters = word[:i]
        new_word = word[i:]
        pig_latin_word = new_word + letters + pig_phrase_1

    return pig_latin_word

def pig_sentence(string):

    """
    This function takes a user input string and uses
    the pig_latin function to turn each word into a Pig-latin
    version of itself. Out put is either a single word
    or a sentence (minus puctuation).
    """

    if " " in string:
        pig_words = []
        my_words = string.split(" ")

        for word in my_words:
            transfrormed_word = pig_latin(word)
            pig_words.append(transfrormed_word)

        pig_phrase = " ".join(str(word) for word in pig_words)
    else:
        transformed_word = pig_latin(string)
        pig_phrase = transformed_word

    return pig_phrase


some_string = input("Input some text: ")
my_phrase = pig_sentence(some_string)
print(my_phrase)
