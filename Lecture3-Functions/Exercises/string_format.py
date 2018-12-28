# {n} refers to the nth positional argument in 'args'
"First, thou shalt count to {0}".format(3)

"{0} shalt thou not count, neither count thou {1}, "
"excepting that thou then proceed to {2}".format(4, 2, 3)

# {key} refers to the optional argument bound by key  
"lobbest thou thy {weapon} towards thy foe".format(
    weapon="Holy Hand Grenade of Antioch")

"{0}{b}{1}{a}{0}{2}".format(5, 8, 9, a='z', b='x')  
# => 5x8z59

args = (5, 8, 9)
kwargs = {'a':'z', 'b':'x'}


