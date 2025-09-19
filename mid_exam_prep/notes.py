class Cat:
    def __init__(self, name = str, color = str):
        self.name = name
        self.color = color
    def meow(self):
        return f"Miauuu! Аз съм {self.name} и съм {self.color}."

cat1 = Cat("Лина", "оранжева")
cat2 = Cat("Бела", "черна")

print(cat1.meow())
print(cat2.meow())