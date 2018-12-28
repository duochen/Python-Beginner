def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))
    for k, v in speaker_info.items():
        print(k, v, sep=": ")


info = {
    'sonnet': 18,
    'line': 1,
    'author': "Shakespeare"
}

authorize("Shall I compare thee to a summer's day", **info)