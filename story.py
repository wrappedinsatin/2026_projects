story_list = []

while True:
    next_word = input("Please type in a word: ")

    if next_word == "end":
        break
    elif len(story_list) < 1:
        story_list.append(next_word)
    else:
        for i in range(1, len(story_list)):
            if story_list[i] != story_list[i + 1]:
                story_list.append(next_word)

story_string = ' '.join(story_list)
print(story_string)