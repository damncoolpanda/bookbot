def get_num_words(contents):
    words = contents.split()
    num_words = len(words)
    return num_words

def get_num_characters(contents):
    characters = {}
    for char in contents.lower():
        if char not in characters:
            characters.setdefault(char,1)
        else:
            characters[char] += 1
    return characters

def sorted_characters(origin_dict):
    def sort_on(origin_dict):
        return origin_dict['count']

    char_list = []
    for key, value in origin_dict.items():
        if key.isalpha():
            char_dict = {}
            char_dict['name'] = key
            char_dict['count'] = value
            char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list