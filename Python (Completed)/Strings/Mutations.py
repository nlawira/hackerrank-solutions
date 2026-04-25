def mutate_string(string, position, character):
    alt_string = string[:position] + character + string[position+1:]
    return alt_string
