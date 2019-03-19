def cell_value(string):
    try:
        return float(string)
    except:
        if string == "":
            return 0
        else:
            return None

result = cell_value("3.14") 
print(result)           # => 3.14
result = cell_value("") 
print(result)           # => 0
result = cell_value("ab3.14") 
print(result)           # => None