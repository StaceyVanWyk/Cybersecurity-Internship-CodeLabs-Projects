
# STEP 1: INPUT
# =========================
password = input("Enter your password: ")

# STEP 2: ANALYSIS
# =========================
length = len(password)
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)


# STEP 3: SCORING
# =========================
score = 0

if has_upper:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1


# STEP 4: OUTPUT
# =========================
if length < 8:
    print("Weak password")
elif score == 1:
    print("Medium password")
else:
    print("Strong password")
    

