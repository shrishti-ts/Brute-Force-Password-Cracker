import msoffcrypto
import os
from tqdm import tqdm

def try_password_and_decrypt(file_path, password, output_path):
    try:
        with open(file_path, "rb") as f_in:
            office_file = msoffcrypto.OfficeFile(f_in)
            office_file.load_key(password=password)
            with open(output_path, "wb") as f_out:
                office_file.decrypt(f_out)
        return True
    except Exception:
        return False

def brute_force_office_file(file_path, wordlist_path):
    if not os.path.exists(file_path):
        print("❌ Error: File not found.")
        return

    if not os.path.exists(wordlist_path):
        print("❌ Error: Password list not found.")
        return

    # Prepare output filename
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_decrypted{ext}"

    # Read all passwords
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(f"🔍 Starting brute-force on {file_path} with {len(passwords)} passwords...")

    for pwd in tqdm(passwords, desc="Trying passwords"):
        if try_password_and_decrypt(file_path, pwd, output_path):
            print("\n✅ Access granted!")
            print("🔑 Password is:", pwd)
            print(f"📁 Decrypted file saved as: {output_path}")
            return

    print("\n❌ Access denied. Password not found.")

if __name__ == "__main__":
    file_path = input("Enter the path to the protected file (.docx/.xlsx): ").strip()
    wordlist_path = input("Enter the path to the password list file: ").strip()
    brute_force_office_file(file_path, wordlist_path)
