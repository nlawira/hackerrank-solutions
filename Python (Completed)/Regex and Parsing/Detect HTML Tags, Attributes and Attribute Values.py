# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)
    def print_attrs(self, attrs):
        for item in attrs:
            name , value = item
            print(f'-> {name} > {value}')

my_parser  = MyHTMLParser()
html = "".join(input() for _ in range(int(input())))
my_parser.feed(html)