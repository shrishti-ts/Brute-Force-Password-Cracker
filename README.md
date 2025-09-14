# 🔐 Office File Password Cracker

A lightweight Python tool to **brute-force and decrypt password-protected**
&#x20;/  files using a wordlist of possible passwords.
Built using  and .

---

## 🚀 Features

* 📝 Supports encrypted ** (.docx)** and ** (.xlsx)** files
* ⚡ Brute-force password attempts using a wordlist
* 📁 Automatically saves the **decrypted file** if the correct password is found
* 📊 Real-time progress bar to track attempts
* 🧩 Clean, modular code ready for extension (GUI / CLI / threading)

---

## ⚙️ Installation

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/shrishti-ts/Office_File_Cracker.git
   cd Office_File_Cracker
   ```

2. Install dependencies:

   ```bash
   pip install msoffcrypto-tool tqdm
   ```

---

## 💻 Usage

1. Prepare a wordlist file (`passwords.txt`) with one password per line.
2. Run the script:

   ```bash
   python office_file_cracker.py
   ```
3. Provide:

   * Path to the protected `.docx` or `.xlsx` file
   * Path to the wordlist

✅ If successful, the decrypted file will be saved as:

```
originalname_decrypted.docx
```

or

```
originalname_decrypted.xlsx
```

---

## 📌 Example

```bash
Enter the path to the protected file (.docx/.xlsx): secret.docx
Enter the path to the password list file: passwords.txt

🔍 Starting brute-force on secret.docx with 5000 passwords...
Trying passwords:  85%|█████████████████████▊   | 4250/5000
✅ Access granted!
🔑 Password is: lifeison
📁 Decrypted file saved as: secret_decrypted.docx
```

---

## ⚠️ Disclaimer

This tool is intended **only for ethical use** — to recover passwords from files you **own or are authorized to access**.
Unauthorized use on files without permission may violate laws and regulations.

---

## 🧠 Future Enhancements

* Add **multithreading** for faster cracking
* Add **GUI interface** using  or&#x20;
* Support additional formats (, , etc.)

---

## 👩‍💻 Author

#*Shrishti Singh*
Cybersecurity & Data Science Enthusiast
🔗 [LinkedIn](#https://www.linkedin.com/in/shrishti-singh-t)
---
