def check_password_strength(password):
    """
    Evaluate the strength of a password based on length and character variety.

    Rules:
    - Passwords shorter than 8 characters are considered weak
    - Presence of uppercase letters, digits, and symbols increases strength
    """

    # Handle empty input
    if not password:
        return "Password cannot be empty"

    # Analyze password characteristics
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Calculate strength score based on character variety
    score = 0
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Determine final classification
    # Length acts as a minimum security requirement (gatekeeper rule)
    if length < 8:
        return "Weak password"
    elif score <= 1:
        return "Medium password"
    else:
        return "Strong password"


if __name__ == "__main__":
    # Get password input from user
    password = input("Enter your password: ")

    # Evaluate and display result
    result = check_password_strength(password)
    print(result)