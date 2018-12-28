# You can use C-style specifiers too!  
print("{:06.2f}".format(3.14159))	# => 003.14

# Padding is just another specifier  
print('{:10}'.format('hi'))     # => 'hi	'  
print('{:^12}'.format('TEST'))  # => '    TEST    '

# You can even look up values!  
captains = ['Kirk', 'Picard']
print("{caps[0]} > {caps[1]}".format(caps=captains)) # => ‘Kirk > Picard'
