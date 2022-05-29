import re

string = 'search inside of this text please!'

# print('search' in string)

result = re.search('this', string)
print(result.group())