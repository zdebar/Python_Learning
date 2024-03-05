def linear_search(cards, query):
    position = 0
    length = len(cards)
    while position < length:
        if cards[position] == query:
            return position
        position += 1
    #Returning -1 for not found in the list
    return -1

