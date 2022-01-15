n = int(input())

# List starts with dummy index 0 that we don't use
# (because villagers are numbered from 1)
villager_songs = [set()]

for i in range(n):
    villager_songs.append(set())

num_evenings = int(input())

song_number = 0

for i in range(num_evenings):
    lst = input().split()
    lst.pop(0)
    for j in range(len(lst)):
        lst[j] = int(lst[j])

    today = set(lst)

    if 1 in today:  # Bard is there; villagers learn new song
        for villager in today:
            villager_songs[villager].add(song_number)
        song_number = song_number + 1
    else:  # Bard isn't there; villagers learn union of songs
        songs_known = set()
        for villager in today:
            songs_known.update(villager_songs[villager])
        for villager in today:
            villager_songs[villager].update(songs_known)

for i in range(1, n + 1):
    if len(villager_songs[i]) == song_number:
        print(i)
