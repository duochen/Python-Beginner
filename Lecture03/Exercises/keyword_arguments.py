def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):  
    for i in range(retries):
        ok = input(prompt)  
        if ok == 'Y':
            return True  
        if ok == 'N':
            return False
        print(complaint)  
    return False

# Call with only the mandatory argument  
ask_yn('Really quit?')

# Call with one keyword argument
ask_yn('OK to overwrite the file?', retries=2)

# Call with one keyword argument - in any order!  
ask_yn('Update status?', complaint='Just Y/N')

# Call with all of the keyword arguments
ask_yn('Send text?', retries=2, complaint='Y/N please!')