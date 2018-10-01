import re
def check_password(p):
    # print errors if any
    num = pwd.isdigit() or type(pwd) is float;
    length = len(pwd) < 8;
    digits = re.search(r"[0-9]", pwd);
    upper = re.search(r"[A-Z]", pwd);
    lower = re.search(r"[a-z]", pwd);
    error = False;
    if num:
        print("error: {0} is not string".format(pwd));
        return False;
    if not digits:
        print("error: should contain at least one digit");
        error = True;
    if not upper:
        print("error: should contain at least one uppercase letter");
        error = True;
    if not lower:
        print("error: should contain at least one lowercase letter");
        error = True;
    if length:
        print("error: too short, min length is 8");
        error = True;
    if error:
        return False
    else:
        print ("Looks good!")
        return True;

pwd = input("enter password:");
check_password(pwd);



