unordered_words_and_meanings = {
    'watermelon': 'A Large fruit',
    'nectarine': 'Similar to a peach.',
    'mango': 'Tropical fruit.',
    'kiwi': 'Small fruit.',
    'vanilla': 'Used in baking.',
    'fig': 'Chewy skin.',
    'pear': 'Sweet fruit.',
    'cherry': 'Red fruit.',
    'strawberry': 'Tiny seeds.',
    'quince': 'Tart flavor.',
    'ugli fruit': 'Hybrid citrus.'
}

default_meaning = '(Default) A fruit.'

def tranpose_search(words):
    global unordered_words_and_meanings
    word_list = list(unordered_words_and_meanings.keys())
    count = 1
    time = 0
    processed_words = []
    init_list = {}
    for word in words:
        word = word.lower().strip()
        if word in word_list:
            index = word_list.index(word)
            time = (index + 2)
            meaning = unordered_words_and_meanings[word]
            print(f"({count}) Word '{word}' found ({time} seconds): {meaning}")

            if word not in processed_words :
                    init_list[word] = index
            if index > 0:
                word_list[index], word_list[index - 1] = word_list[index - 1], word_list[index]
        else:
            time = len(word_list) + 2
            print(f"({count}) Word '{word}' added ({time} seconds): {default_meaning}")
            unordered_words_and_meanings[word] = default_meaning
            word_list.append(word)

        count += 1
        if word not in processed_words:
            processed_words.append(word)
            
    print("(END) Updated dictionary:")
    format = [f"{i}: {word}" for i, word in enumerate(word_list)]
    print(', '.join(format))
    
    print("(SUMMARY OF INDEX CHANGES):")
    for word in processed_words:
        if word in unordered_words_and_meanings:
            new_index = word_list.index(word)
            old_index = init_list.get(word, 'None')
            print(f"{word}: {old_index} -> {new_index}")


tranpose_search(input('Enter a word to search for: ').split(','))

