def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(filepath):
    return len(read_file(filepath).split())

def count_character_recurrance(filepath):
    character_count = {}
    for c in read_file(filepath).lower():
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_character_recurrance(filepath):
    input = count_character_recurrance(filepath)
    output = []
    for item in input:
        output.append({"char": item, "num": input[item]})
    output.sort(reverse=True, key=sort_on)
    return output