import random
import string

def generate_password(length, use_numbers=True, use_special=True):
    chars = string.ascii_letters 
    
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "Error: No characters selected!"

    password = "".join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    
    try:
        length = int(input("Enter password length (e.g., 12): "))
        if length < 4:
            print("For security, length should be at least 4. Setting to 4.")
            length = 4
    except ValueError:
        print("❌ Invalid number. Defaulting to length 12.")
        length = 12

    include_num = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_spec = input("Include special characters? (y/n): ").strip().lower() == 'y'

    generated_password = generate_password(length, include_num, include_spec)
    
    print("\n" + "="*30)
    print(f"YOUR PASSWORD: {generated_password}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()