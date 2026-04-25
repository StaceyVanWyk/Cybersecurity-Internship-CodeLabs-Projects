
#Step 1: This is the INPUT stage
password = input("Enter your password: ")

#Step 2: Analysis - Create variable

length = len(password)
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# #Step 3: Scoring logic
score = 0

# if length >= 8:
#     score += 1
# if has_upper:
#     score += 1
# if has_digit:
#     score += 1
# if has_symbol:
#     score += 1

#Step 4: Output
if length < 8:
    print("Weak password")
else:
    if score <=2:
        print("Medium")
    else:
        print("Strong password")
# if score <= 1:
#     print("Weak password")
# elif score <=3:
#     print("Medium password")
# else:
#     print("Strong password")
    

