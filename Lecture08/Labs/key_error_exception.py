mydict = {}
print(mydict)  # => {}
print(mydict.get("foo", "bar"))  # => bar
print(mydict)  # => {}
print(mydict.setdefault("foo", "bar"))  # => bar
print(mydict)  # => {'foo': 'bar'}

default_value = "par"
try:
    value = mydict["doo"]
except KeyError:
    value = default_value
print(value)  # => par

if "doo" in mydict:
    value = mydict["doo"]
else:
    value = default_value

print(value)