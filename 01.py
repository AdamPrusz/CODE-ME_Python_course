# Napisz kod funkcji, która sprawdzi czy email znajduje się na liście i zwróci wartość True/False

def search_email(my_email, emails):
    for email in emails:
        if email == my_email:
            return True
    return False