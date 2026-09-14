s="A man, a plan, a canal: Panama"

lowered=s.lower()

cleaned_text = ''.join([char for char in lowered if char.isalnum()])

reversed_str = cleaned_text[::-1]

if cleaned_text == reversed_str:
    print("True")
else:
    print("False")