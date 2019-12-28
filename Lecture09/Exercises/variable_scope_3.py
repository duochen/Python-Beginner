score = 0
def update_score(new_score):
    global score
    score = new_score
    print(score)

update_score(100)
print(score)