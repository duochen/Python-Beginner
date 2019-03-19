def write_to_disk(filename):
    # if write successfully, return true
    status = True
    # else return false
    status = False

    return status

def save_text_to_file(filename):
    return write_to_disk(filename)

def save_prefs_to_file(filename):
    return write_to_disk(filename)

def save_to_file(filename):
    status = save_text_to_file(filename) 
    if status == False:
        print("saving to file failed!")
    else:
        print("saving to file succeeded!")

    status = save_prefs_to_file(filename)
    if status == False:
        print("saving preferences to file failed!")
    else:
        print("saving preferences to file succeeded!")

save_to_file('word.txt')