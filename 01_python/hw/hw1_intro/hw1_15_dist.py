cat = {}
info = {"status": "vaccinated", "breed": True}
cat.update({"nick":"Simon", "age":7, "characteristics":["лагіний", "кусається"]})

age = cat.get("age")
cat.update(info)

print(cat)
print(age)