# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())
valid = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(":")
for _ in range(N):
    api_id, request = str(input()).split()
    if (re.search(r'[1-9]\d{3}', api_id)) and (request in valid):
        print('VALID')
    else:
        print('INVALID')