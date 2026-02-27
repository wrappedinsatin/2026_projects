story_list = []

while True:

    next_word = input("Please type in a word: ")

    if next_word == "end":
        break
    
    if len(story_list) == 0 or story_list[-1] != next_word:
        story_list.append(next_word)

story_string = ' '.join(story_list)
print(story_string)