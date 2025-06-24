# 2. Demonstrate use of advanced regular expressions for data validation.
 
import re
def check(email):
    pattern = r'[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
    print("Valid Email" if re.fullmatch(pattern, email) else "Invalid Email")

emails=["amazing3260@gmail.com",
    "my.ownsite@our-earth.com",
    "amazed326.com"]
for e in emails: check(e)