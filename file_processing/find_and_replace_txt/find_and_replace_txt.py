def replaceText(ogtext, target, new_word):
    with open(ogtext, "r") as file:
        content = file.read()

    words = content.split()
    replaced = " ".join(new_word if word == target else word for word in words)

    with open("modified.txt", "w") as file2:
        file2.write(replaced)

replaceText("example.txt", "Europe", "Asia")