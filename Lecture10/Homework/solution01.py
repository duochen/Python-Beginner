ids=["B3","\nB4","\nB5","\nB6"]

with open("testing.txt", "w") as file:
    for item in ids:
        file.write(item)