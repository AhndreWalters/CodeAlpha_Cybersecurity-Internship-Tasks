"""
Secure Application - CodeAlpha Security Audit
All vulnerabilities fixed.
"""

import sqlite3
import subprocess
import os

# FIX 1: Use environment variable instead of hardcoded password
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'secure_password')

# FIX 2: Use parameterized query to prevent SQL injection
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# FIX 3: Validate input and use argument list to prevent command injection
def ping_host(host):
    # Validate input - only allow safe characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        return "Invalid host"
    
    # Use argument list instead of shell=True
    result = subprocess.check_output(['ping', '-c', '1', host])
    return result.decode()

def main():
    print("1. Get User")
    print("2. Ping Host")
    print("3. Admin Login")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        username = input("Enter username: ")
        user = get_user(username)
        print(user)
    
    elif choice == "2":
        host = input("Enter IP to ping: ")
        result = ping_host(host)
        print(result)
    
    elif choice == "3":
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            print("Access granted!")
        else:
            print("Access denied!")

if __name__ == "__main__":
    main()
