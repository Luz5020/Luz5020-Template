# Construct Cat
class Cat:
    name = ""
    kind = "cat"
    color = ""
    value = ""

    def description(self):
        desc_str = "%s is a %s %s worth %s." % (self.name, self.kind, self.color, self.value)
        return desc_str


# The cats live here
Cat1 = Cat()
Cat1.name = "Zelda"
Cat1.color = "black"
Cat1.value = "infinity"
Cat2 = Cat()
Cat2.name = "Sternchen"
Cat2.color = "brown"
Cat2.value = "infinity"
# Introduction of the Cats
print(Cat1.description())
print(Cat2.description())
