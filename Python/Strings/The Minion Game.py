def minion_game(string):
    # your code goes here
    letters = ['A', 'E', 'I', 'O', 'U']
    kevin_p, stuart_p = 0, 0
    for i in range(len(string)):
        if string[i] in letters:
            kevin_p = kevin_p + len(string) - i
        else:
            stuart_p = stuart_p + len(string) - i    
    if kevin_p > stuart_p:
        print('Kevin', kevin_p)
    elif kevin_p < stuart_p:
        print('Stuart', stuart_p)
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)