# Inlezen
with open("Presidents", "r") as file:
    content = file.read()

# Aanpassen
content = content.replace("Lincoln", "")

# Terugschrijven
with open("Presidents", "w") as file:
    file.write(content)
