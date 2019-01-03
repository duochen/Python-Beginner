try:
    d = {}
    a = d[1]
    b = d.non_existin_field
except KeyError as e:
    print("A KeyError has occurred. Exception message:", e)
except AttributeError as e:
    print("An AttributeError has occurred. Exception message:", e)

# A KeyError has occurred. Exception message: 1    