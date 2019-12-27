studentList = {'danish', 'jason', 'sarah', 'mike', 'arthur', 'jack'}
placedStudList = {'mike', 'danish', 'arthur'}

notPlacedStudList = set(studentList) - set(placedStudList)
print("Students yet to get job", notPlacedStudList)