import re
import random
import string

# Function to analyze password strength
def analyze_password(password):

    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should contain at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Strength Rating
    if score <= 2:
        strength = "Weak Password"
    elif score == 3 or score == 4:
        strength = "Medium Password"
    else:
        strength = "Strong Password"

    return strength, suggestions


# Function to Generate Strong Password
def generate_password(length=12):

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    generated_password = ''.join(random.choice(characters) for i in range(length))

    return generated_password


# Main Program
print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter Password: ")

strength, suggestions = analyze_password(password)

print("\nPassword Strength:", strength)

# Suggestions
if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)

# Strong Password Suggestion
print("\nSuggested Strong Password:")
print(generate_password())