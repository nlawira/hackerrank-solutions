# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

tag_pattern = re.compile(r'(<([^/\s>]+).*?/?>)')
att_pattern = re.compile(r'(([a-z]+)=[\'"])')
tags_dict = {}

N = int(input())
for i in range(N):
    tags = tag_pattern.findall(str(input()))
    for tag in tags:
        if tag[1] not in tags_dict:
            tags_dict[tag[1]] = set()   
        atts = att_pattern.findall(tag[0])
        for att in atts:
            tags_dict[tag[1]].add(att[1])
for tag in sorted(tags_dict.keys()):
    attributes = ','.join(sorted(tags_dict[tag]))
    print(f'{tag}:{attributes}')