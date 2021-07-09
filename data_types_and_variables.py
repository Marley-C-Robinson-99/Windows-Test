# Number 1
cost = 3
rentals = {"The Little Mermaid": 3, "Brother Bear": 5, 'Hercules': 1}
print('The price is $' + str(sum([y for x,y in rentals.items()]) * cost))

jobs = {"Google": 400, "Amazon": 380, 'Facebook': 350}
print(( jobs['Google'] * 6 ) + ( jobs['Amazon'] * 4 ) + ( jobs["Facebook"] * 10 ))

# Number 2
username = 'codeup'
password = 'notastrongpassword'
pass5 = len(password) > 5
user20 = len(username) <= 20
pass_user_con = password != username
passblank = password[0] != ' '
usrblank = username[0] != ' '
compare_usr_pass = passblank & usrblank
print(pass5, user20, pass_user_con, compare_usr_pass)
