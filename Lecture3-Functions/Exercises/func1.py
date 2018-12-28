def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
        ok = input(prompt)
        if ok == 'Y':
            return True
        if ok == 'N':
            return False
        print(complaint)
    return False

ask_yn("Are you ok?")    