import re


def is_strong_password(password):
    # Define the regular expressions for various password rules
    length_regex = r".{8,}"  # At least 8 characters
    uppercase_regex = r"[A-Z]"  # At least one uppercase letter
    lowercase_regex = r"[a-z]"  # At least one lowercase letter
    digit_regex = r"[0-9]"  # At least one digit
    special_char_regex = r"[@#$%^&+=]"  # At least one special character

    # Check if the password meets all the rules
    if (
        re.search(length_regex, password)
        and re.search(uppercase_regex, password)
        and re.search(lowercase_regex, password)
        and re.search(digit_regex, password)
        and re.search(special_char_regex, password)
    ):
        return True
    else:
        return False


def is_valid_email(email):
    # Define a regular expression pattern to match email addresses
    pattern = r"^[\w\.-]+@(gmail\.com|yahoo\.com|outlook\.com)$"

    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
