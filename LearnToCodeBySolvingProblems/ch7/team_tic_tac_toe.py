LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cow_wins(grid, letter):
    """
    grid is a game grid.
    letter is a string of one uppercase letter.

    Return True if letter wins, False otherwise.
    """
    if grid[0][0] == letter and grid[0][1] == letter and grid[0][2] == letter:
        return True
    if grid[1][0] == letter and grid[1][1] == letter and grid[1][2] == letter:
        return True
    if grid[2][0] == letter and grid[2][1] == letter and grid[2][2] == letter:
        return True
    if grid[0][0] == letter and grid[1][0] == letter and grid[2][0] == letter:
        return True
    if grid[0][1] == letter and grid[1][1] == letter and grid[2][1] == letter:
        return True
    if grid[0][2] == letter and grid[1][2] == letter and grid[2][2] == letter:
        return True
    if grid[0][0] == letter and grid[1][1] == letter and grid[2][2] == letter:
        return True
    if grid[0][2] == letter and grid[1][1] == letter and grid[2][0] == letter:
        return True
    return False


def team_wins_one(team, letter1, letter2, letter3):
    """
    team is a string of two uppercase letters.
    letter1, letter2, and letter3 are strings of one lowercase letter.

    Return a bool: True if team wins using letter1, letter2, and letter3,
    False otherwise.
    """
    if not letter1 in team or not letter2 in team or not letter3 in team:
        return False
    if letter1 == letter2 and letter2 == letter3:
        return False
    return True


def team_wins(grid, team):
    """
    grid is a game grid.
    letter is a string of two uppercase letters.

    Return a bool: True if team wins, False otherwise.
    """
    if team_wins_one(team, grid[0][0], grid[0][1], grid[0][2]):
        return True
    if team_wins_one(team, grid[1][0], grid[1][1], grid[1][2]):
        return True
    if team_wins_one(team, grid[2][0], grid[2][1], grid[2][2]):
        return True
    if team_wins_one(team, grid[0][0], grid[1][0], grid[2][0]):
        return True
    if team_wins_one(team, grid[0][1], grid[1][1], grid[2][1]):
        return True
    if team_wins_one(team, grid[0][2], grid[1][2], grid[2][2]):
        return True
    if team_wins_one(team, grid[0][0], grid[1][1], grid[2][2]):
        return True
    if team_wins_one(team, grid[0][2], grid[1][1], grid[2][0]):
        return True
    return False


input_file = open('tttt.in', 'r')
output_file = open('tttt.out', 'w')

grid = []

for i in range(3):
    grid.append(input_file.readline().rstrip())

individual_winners = 0
for letter in LETTERS:
    if cow_wins(grid, letter):
        individual_winners = individual_winners + 1

output_file.write(f'{individual_winners}\n')

team_winners = 0
for i in range(len(LETTERS)):
    for j in range(i + 1, len(LETTERS)):
        team = LETTERS[i] + LETTERS[j]
        if team_wins(grid, team):
            team_winners = team_winners + 1

output_file.write(f'{team_winners}\n')

input_file.close()
output_file.close()
