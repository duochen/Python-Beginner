def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))  
    for k, v in speaker_info.items():
        print(k, v, sep=': ')

speaker_info = {  
    'act': 1,
    'scene': 1,
    'speaker': "Duke Orsino",  
    'playwright': "Shakespeare"
}

if __name__ == '__main__':
    speaker_info = {  
        'act': 1,
        'scene': 1,
        'speaker': "Duke Orsino",  
        'playwright': "Shakespeare"
    }    
    authorize("This is a test", **speaker_info)

    info = {
        'sonnet': 18,
        'line': 1,
        'author': "Shakespeare"
    }
    authorize("Shall I compare thee to a summer's day", **info)
    


