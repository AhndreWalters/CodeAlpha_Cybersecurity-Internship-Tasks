"""
Vulnerable Application - CodeAlpha Security Audit
This contains security flaws for educational purposes.
"""

import sqlite3
import subprocess

# VULNERABILITY 1: Hardcoded password
ADMIN_PASSWORD = "admin123"

# VULNERABILITY 2: SQL Injection
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

# VULNERABILITY 3: Command Injection
def ping_host(host):
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
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
