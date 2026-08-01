# Secure Coding Review

A security code review conducted as Task 3 for the CodeAlpha Cyber Security Internship. This project identifies and fixes vulnerabilities in a Python application including hardcoded credentials, SQL injection, and command injection.

<img width="1366" height="768" title="Vulnerable and Secure Codes in Editor" alt="image" src="https://github.com/user-attachments/assets/b5abfce5-2c34-4d57-9d51-fbd522bff75a" />

### Vulnerabilities Identified

1. **Hardcoded Password** - Password stored in plain text in source code
2. **SQL Injection** - User input directly inserted into SQL queries
3. **Command Injection** - User input executed as system commands

### Files Included

- **vulnerable_app.py** - Original application with security flaws
- **secure_app.py** - Remediated version with all vulnerabilities fixed
- **SECURITY_REVIEW.md** - Detailed security review report

### How to Use

#### Vulnerable Version
```bash
python3 vulnerable_app.py
```

#### Secure Version
```bash
python3 secure_app.py
```

---

<b>[&copy; Ahndre Walters](https://github.com/AhndreWalters/CodeAlpha_Cybersecurity-Internship-Tasks/blob/main/LICENSE) | CodeAlpha Cyber Security Intern</b>
