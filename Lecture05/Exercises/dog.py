class Dog:
    kind = 'Canine'       # class variable shared by all instances
    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

a = Dog('Astro')
pb = Dog('Mr. Peanut Butter')

print(a.kind)          # 'Canine' (shared by all dogs)
print(pb.kind)         # 'Canine' (shared by all dogs)

print(a.name)          # 'Astro' (unique to a)
print(pb.name)         # 'Mr. Peanut Butter' (unique to pb)

