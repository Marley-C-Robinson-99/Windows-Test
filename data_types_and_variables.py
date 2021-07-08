# Number 1
movies = {"The Little Mermaid": 3, "Brother Bear": 5, 'Hercules': 1}
print(sum([y for x,y in movies.items()]))

jobs = {"Google": 400, "Amazon": 380, 'Facebook': 350}
print(( jobs['Google'] * 6 ) + ( jobs['Amazon'] * 4 ) + ( jobs["Facebook"] * 10 ))

# Number 2
import re
username = 'codeup'
password = 'notastrongpassword'
pass5 = len(password) > 5
user20 = len(username) <= 20
pass_user_con = password != username
passblank = password[0] != ' '
usrblank = username[0] != ' '
compare_usr_pass = passblank & usrblank
print(pass5, user20, pass_user_con, compare_usr_pass)
