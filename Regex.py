import re

text = """The quick brown fox jumps over the lazy dog. 
Email: example.user123@mail.com, another.email@domain.org
Phone: +1-800-555-0199, (123) 456-7890
Address: 1234 Elm Street, Apt 567, Springfield, IL 62704

Date: 12/31/2024, 2024-12-31, 31-12-2024
Time: 14:30, 02:30 PM, 23:59

Usernames:
- user_001
- Admin_99
- regexMaster_123

Sentences with numbers: 
- There are 42 apples in the basket.
- The price of the laptop is $999.99.
- My ID is A1234567.

Special characters: @#$%^&*()_+={}[]|;:'",.<>?/~`

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Suspendisse potenti. Sed euismod, nisi ac venenatis luctus, velit felis posuere lacus, at venenatis justo neque sed lorem.

John's email is john.doe@example.com, and his backup is johndoe123@work.net.  
Call him at +1-555-123-4567 or his office line (555) 765-4321.  
His website is https://www.johndoe.dev, and his IP address is 192.168.0.1.  
The price of the item is $19.99, but with a discount, it’s now $14.99.  
Today's date is 17/02/2025, and another format is 2025-02-17.  
Here’s some HTML: <div class="container">Hello, World!</div>  
Watch out for special characters like !@#$%^&*()_+={}[]|:;"'<>,.?/

A regular expression (or RE) specifies a set of strings that matches it; 
the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing). 
Regular expressions can be concatenated to form new regular expressions; 
if A and B are both regular expressions, then AB is also a regular expression. 
In general, if a string p matches A and another string q matches B, the string pq will match AB. 
This holds unless A or B contain low precedence operations; boundary conditions between A and B; 
or have numbered group references. 
Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. 
For details of the theory and implementation of regular expressions, consult the Friedl book [Frie09], or almost any textbook about compiler construction. 
A brief explanation of the format of regular expressions follows. 
For further information and a gentler presentation, consult the Regular Expression HOWTO. 
Regular expressions can contain both special and ordinary characters. 
Most ordinary characters, like 'A', 'a', or '0', are the simplest regular expressions; 
they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'.
"""

def ab_zero_or_more(t):
    return bool(re.search(r"^ab*$", t))

def ab_two_to_three(t):
    return bool(re.search(r"^ab{2,3}$", t))

def lowercase_with_underscore(t):
    return re.findall(r"[a-z]+_[a-z]+", t)

def uppercase_followed_by_lowercase(t):
    return re.findall(r"[A-Z][a-z]+", t)

def match_a_anything_b(t):
    return bool(re.search(r"^a.*b$", t))

def replace_space_comma(t):
    return re.sub(r"[ ,.]", ":", t)

def snake_to_camel(t):
    parts = t.split('_')
    return parts[0].lower() + "".join(x.capitalize() for x in parts[1:])

def split_at_uppercase(t):
    return [p for p in re.split(r'(?=[A-Z])', t) if p]

def spaces_before_capitals(t):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', t)

def camel_to_snake(t):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', t).lower()

if __name__ == "__main__":
    print("1)", ab_zero_or_more(text))
    print("2)", ab_two_to_three(text))
    print("3)", lowercase_with_underscore(text))
    print("4)", uppercase_followed_by_lowercase(text))
    print("5)", match_a_anything_b(text))
    print("6)", replace_space_comma(text))
    print("7)", snake_to_camel("this_is_snake_case"))
    print("8)", split_at_uppercase("HelloWorldTest"))
    print("9)", spaces_before_capitals("HelloWorldTest"))
    print("10)", camel_to_snake("helloWorldTest"))
