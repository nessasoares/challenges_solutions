import re
import ipdb

def fun(s):
    ipdb.set_trace()
    # return True if s is a valid email, else return False
    if '@' in s:
        email = s.split('@')
        username = email[0]
        if '.' in email[1]:
            websitename, extension = email[1].split('.')
        else: 
            return False
        # Checking username
        if len(username) > 0:
            string_check= re.compile('[@.!#$%^&*()<>?/\|}{~:]') 
            if(string_check.search(username) != None): 
                return False
        else:
            return False

        # Checking website name
        if len(websitename) > 0:
            string_check = re.compile(r'^[a-zA-Z0-9]*$') 
            if(string_check.search(websitename) == None): 
                return False
        else:
            return False        
        # Checking extension
        if len(extension) > 3:
            return False
    else:
        return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)