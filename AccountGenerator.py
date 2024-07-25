import random
import string

def generate_random_email(domain="gmail.com", length=12):
    characters = string.ascii_lowercase + string.digits
    random_email = ''.join(random.choice(characters) for _ in range(length)) + "@" + domain
    return random_email

def generate_random_username(length=10):
    characters = string.ascii_lowercase + string.digits
    random_username = ''.join(random.choice(characters) for _ in range(length))
    return random_username

# Generate 100 random emails and usernames
emails = [generate_random_email() for _ in range(64)]
usernames = [generate_random_username() for _ in range(64)]

# Save emails to email.txt
with open("email.txt", "w") as email_file:
    for email in emails:
        email_file.write(email + "\n")

# Save usernames to username.txt
with open("username.txt", "w") as username_file:
    for username in usernames:
        username_file.write(username + "\n")
