#given a list of words determine if two words in list are the same
def contains_duplicate(words):
    for n in range(len(words)):
        if words[n] in words[:n] or words[n] in words[n+1:]:
            return True
    return False