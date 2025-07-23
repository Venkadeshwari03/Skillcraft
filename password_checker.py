import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("❌ Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("❌ Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("❌ Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks.append("❌ Add at least one digit (0-9).")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        remarks.append("❌ Add at least one special character (e.g., @, #, $, !).")

    # Strength message
    print("\n🔍 Password Analysis:")
    if strength == 5:
        print("✅ Strong password!")
    elif strength >= 3:
        print("⚠ Moderate password. Consider improving it:")
    else:
        print("❌ Weak password. Needs improvement:")

    # Display suggestions if any
    for remark in remarks:
        print(remark)

# === Main Program ===
print("=== Password Strength Checker ===")
user_password = input("Enter your password: ")
check_password_strength(user_password)