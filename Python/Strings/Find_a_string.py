def count_substring(string, sub_string):
    ss_len = len(sub_string)
    count = 0
    for i in range(0, len(string)-ss_len+1):
        if string[i:i+ss_len] == sub_string:
            count += 1
        else:
            pass
    return count