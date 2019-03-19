def write_to_disk(filename):
    # if write successfully, return true
    status = True
    # else return false
    status = False
    if status == False:
        raise Exception("Writing disk error!")

    return status

def save_text_to_file(filename):
    return write_to_disk(filename)

def save_prefs_to_file(filename):
    return write_to_disk(filename)

def save_to_file(filename):
    try:
        save_text_to_file(filename) 
        save_prefs_to_file(filename)
    except Exception as e:
        print("Got an exception: {0}".format(str(e)))

save_to_file('word.txt')