import re

def validate_email(email):
    # Regex pattern for validating an email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")
        
emails = [
    "test@example.com",
    "user.name+tag+sorting@example.com",
    "user@sub.example.com",
    "user@123.123.123.123",
    "user@[IPv6:2001:db8::1]",
    "invalid-email@",
    "invalid-email@.com",
    "no-at-sign.com",
    "user@.com",
    "@no-username.com"
    "odhjustin@gmail.com"
    "johndoe.com"
]

for email in emails:
    validate_email(email)