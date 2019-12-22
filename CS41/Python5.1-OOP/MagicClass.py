class MagicClass:
    def	__init__(self): pass
    def __contains__(self, key): pass
    def __add__(self, other): pass
    def __iter__(self): pass
    def __next__(self): pass
    def __getitem__(self, key): pass
    def __len__(self): pass
    def __lt__(self, other): pass
    def __eq__(self, other): pass
    def __str__(self): return 'My String'
    def __repr__(self): pass

x = MagicClass()
y = MagicClass()
str(x)
x == y
