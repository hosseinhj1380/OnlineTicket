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
    
def is_valid_number_cinema(numbers):
    pattern = re.compile(r'\d{3}-\d{8}')

    

    for number in numbers:
        if pattern.match(number):
            pass
        else:
            return False
        return True


def is_valid_format(input_text):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+03:30$')
    return bool(pattern.match(input_text))

def is_valid_time_format(input_text):
    pattern = re.compile(r'^(0[7-9]|1\d|2[0-4]):([0-5]\d):00\+03:30$')

    return(bool(pattern.match(input_text)))