email = "stud.ent@example.com"
atPos = email.find("@")
dotPos = email.find(".", atPos+1)
user = email[0:atPos]
domain = email[atPos+1:dotPos]
print(user, domain)