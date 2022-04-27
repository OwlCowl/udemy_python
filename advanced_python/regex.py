import re

# email = 'yana@spacex.com'
# expression = '[a-z]+'
#
# matches = re.findall(expression, email)
# print(matches)
# name = matches[0]
# domain = matches[1]
# print(name, domain)
# #without
# parts = email.split('@')
# print(parts)

price = 'Price: $189.50'
expression1 = 'Price: (\$189.50)'
expression= 'Price: \$([0-9]*\.[0-9]*)'
matches = re.search(expression, price)
price_number = float(matches.group(1))
print(price_number)
