from homework_8 import *
from pprint import pprint


users = generate_users_list(1000) 
    
test_users = [{"name": str((datetime.now() + timedelta(days=i)).day), "birthday": datetime.now() + timedelta(days=i)} for i in range(-5, 10)]
# pprint(test_users)

print('users')
generate_users_birthday_list(users)
print()
print('test_users')
generate_users_birthday_list(test_users, datetime(year=2023, month=6, day=12))