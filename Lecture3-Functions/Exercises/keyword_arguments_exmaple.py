def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))  
    for k, v in speaker_info.items():
        print(k, v, sep=': ')

authorize(
    "If music be the food of love, play on.",  
    playwright="Shakespeare",
    act=1,
    scene=1,  
    speaker="Duke Orsino"
)

# > If music be the food of love, play on.   
# # ----------------------------------------
# act: 1
# scene: 1
# speaker: Duke Orsino
# playwright: Shakespeare

info = {
'sonnet': 18,
'line': 1,
'author': "Shakespeare"
}

authorize("Shall I compare thee to a summer's day", **info)   # > Shall I compare thee to a summer's day

# ----------------------------------------
# line: 1
# sonnet: 18
# author: Shakespeare


