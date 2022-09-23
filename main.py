import re
data = open('MOCK_DATA.txt', 'r')
content = data.read()
data.close()
while True:
    print('1)Count email')
    print('2)Count file name')
    print('3)Count fullname')
    print('4)Count color')
    print('5)Exit')
    commanda = input('Choose the function:')
    if commanda == '3':
        with open('full_name.txt', 'w') as file:
            names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+[ \s]+[a-zA-Z\'\-\. ]+\b', content)
            for name in names_list:
                file.write(name+'\n')
    elif commanda == '1':
        with open('email.txt', 'w') as file:
            emails_list = re.findall(r'(\b[\w\-]+[ @][\w\-]+(\.[\w\-]+)+)', content)
            for email in emails_list:
                file.write(email[0]+'\n')
    elif commanda == '2':
        with open('file_name.txt', 'w') as file:
            files_list = re.findall(r'[\t\s][ \w]+\.[ \w]+\b', content)
            for files in files_list:
                file.write(files[1:]+'\n')
    elif commanda == '4':
        with open('color.txt', 'w') as file:
            color_list = re.findall(r'#[a-f0-9]{6}\n', content)
            for color in color_list:
                file.write(color)
    elif commanda == '5':
        break
    else:
        print('')