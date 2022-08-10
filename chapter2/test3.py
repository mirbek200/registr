import re

print('Давайте зарегистрируемся')
password = input('Введите пароль: ')

l, u, n, znack, trash = 0, 0, 0, 0,0

pattern_u = r"[A-Z]"
res_u = re.findall(pattern_u, password)

pattern_n = r"[0-9]"
res_n =  re.findall(pattern_n, password)

pattern_l = r"[a-z]"
res_l =  re.findall(pattern_l, password)

for i in password:
    if i in res_u:
        u+=1
    elif i in res_n:
        n+=1
    elif i in res_l:
        l+=1
    elif i in '$%!@#^&*':
        znack+=1
    else:
        trash+=1

if len(password) < 8:
    print('Пароль должен быть длинее восьми символов')
elif n == 0:
    print('Пароль должен содержать цифры')
elif u == 0:
    print('Пароль должен содержать заглавные буквы')
elif l == 0:
    print('Пароль должен содержать маленькие буквы')
elif znack == 0:
    print('Пароль должен содержать специальные символы как $%!@#^&*')
elif trash != 0:
    print('ERROR')
else:
    print('Вы успешно зарегистрированы')