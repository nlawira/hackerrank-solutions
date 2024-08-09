start = "^"
thousands = "(?P<thousands>M{0,3})"
hundreds = "(?P<hundreds>C[DM]|D?C{0,3})"
tens = "(?P<tens>X[LC]|L?X{0,3})"
ones = "(?P<ones>I[VX]|V?I{0,3})"
end = "$"
regex_pattern = rf"{start}{thousands}{hundreds}{tens}{ones}{end}"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))