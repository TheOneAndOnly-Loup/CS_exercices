def replaceText(ogtext, target, new_word):
    content = ""
    with open(ogtext, "r") as file:
        content = file.read()
    
    replaced = content.replace(target, new_word)

    with open("modified.txt", "w") as file2:
        file2.write(replaced)
    
    return 0

replaceText("example.txt", "Europe", "Asia")
