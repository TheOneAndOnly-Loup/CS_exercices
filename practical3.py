def parse_and_format():
    try:
        word=input()
        print(word.upper(), len(word), word[0], word[-1])
    except:
        print("Wrong input")

parse_and_format()