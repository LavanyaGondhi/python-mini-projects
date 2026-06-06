def clean_input(text):
    text=text.strip()
    text=text.lower()
    return text
    
def validate_email(email):
    if '@' in email:
        if email.endswith('.com') or email.endswith('.in'):
            return True
    return False
    
def validate_password(password):
    if len(password)>=8:
        for x in password:
            if x.isdigit():
                return True
    return False
    
def format_name(full_name):
    full_name=clean_input(full_name)
    full_name=full_name.title()
    return full_name.split()

def generate_username(full_name,birth_year):
    username=full_name.split()[0] + str(birth_year)[-2:]
    return username.lower()

def print_profile(full_name,email,password,birth_year):
    print("\n===============================================")
    print("                 USER PROFILE                     ")
    print("===============================================")
    name_parts=format_name(full_name)
    print("Name     :"," ".join(name_parts))
    print("Username :",generate_username(full_name,birth_year))
    print("Email     :",email)
    print("Password :✅  Strong")
    print("=================================================")
    if validate_email(email):
        print("Email valid  :✅")
    if validate_password(password):
        print("Password valid:  ✅")
    print("Status   :Registration successful!")
    if not validate_email(email) or not validate_password(password):
        print("❌")
        print("Status: Registration Failed!")
full_name="Lavanya Gondhi"
email="lavanyagondhi@gmail.com"
password="lavanya2006"
birth_year=2006
print_profile(full_name,email,password,birth_year)
    
    
    
    
    