# A school uses the first three characters of a student's name and the last three characters of a student's name along with @567 to develop an initial password. 
# Construct an algorithm that takes a student's name and outputs their initial password. For example:
# Input: "Boris Laurent"
# Output: "Borent@567"


name = str(input("What is your name + last name? "))
password = name[:3] + name[-3:] + "@567"

print(f"Here is your password: {password}")