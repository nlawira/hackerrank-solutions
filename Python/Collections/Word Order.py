# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
word_dict = {}
for _ in range(n):
    word = str(input())
    word_dict[word] = word_dict.get(word, 0) + 1
values = list(map(str, word_dict.values()))
print(len(values))
print(' '.join(values))f