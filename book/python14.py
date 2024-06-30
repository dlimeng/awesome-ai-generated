email = input("Please enter your Email address: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your email username: '{username}' , Your email domain: '{domain_name}'")
print(format_)
input()  # This last line is just waiting for user input and does not produce any output.