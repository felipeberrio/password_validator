from validator import is_strong_password

def main():
    password = input("Enter your password: ")
    if is_strong_password(password):
        print("✅ Your password is strong.")
    else:
        print("❌ Your password is weak. Try again.")

if __name__ == "__main__":
    main()
