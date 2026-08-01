# Security Code Review Report

### Application: Vulnerable Application
### Language: Python
### Date: July 2026
### Reviewer: Ahndre Walters

---

### Tools Used

- Manual code inspection
- Static analysis: Bandit (Python security linter)

---

### Vulnerabilities Found

#### 1. Hardcoded Password
**Location:** `ADMIN_PASSWORD = "admin123"`
**Risk:** Password is visible in source code. Anyone with code access can see it.
**Fix:** Use environment variables or a secure configuration file.

#### 2. SQL Injection
**Location:** `f"SELECT * FROM users WHERE username = '{username}'"`
**Risk:** Attackers can manipulate the query to access all data.
**Fix:** Use parameterized queries.

#### 3. Command Injection
**Location:** `subprocess.check_output(f"ping -c 1 {host}", shell=True)`
**Risk:** Attackers can execute system commands.
**Fix:** Use argument list and validate input.

---

### Remediation Steps

| Vulnerability | Fix Applied |
|--------------|-------------|
| Hardcoded Password | Used environment variable |
| SQL Injection | Used parameterized queries |
| Command Injection | Used argument list + input validation |

---

### Secure Coding Recommendations

1. **Never hardcode credentials** - Use environment variables
2. **Use parameterized queries** - Prevents SQL injection
3. **Validate all user input** - Never trust user input
4. **Use safe system calls** - Avoid shell=True with user input
5. **Keep dependencies updated** - Regular security patches

---

### Summary

All vulnerabilities have been identified and addressed in the secure version. Regular code reviews and static analysis should be part of the development process.
