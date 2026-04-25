k = int(input())
room_list = input().split(" ")
dictionary = dict()
for room_id in room_list:
    dictionary[room_id] = dictionary.get(room_id,0)+1
print(list(dictionary.keys())[list(dictionary.values()).index(1)])