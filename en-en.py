import string,os
from time import sleep

print("""
    __ __                        _      __           ______                                            __                
   / //_/  __  __  _____ ____   (_)   _/ /          / ____/   ____   _____   _____   __  __    ____   / /_  ____    _____
  / ,<    / / / / / ___//_  /  / /   / __/         / __/     / __ \ / ___/  / ___/  / / / /   / __ \ / __/ / __ \  / ___/
 / /| |  / /_/ / / /__   / /_ / /   (_  )         / /___    / / / // /__   / /     / /_/ /   / /_/ // /_  / /_/ / / /    
/_/ |_|  \__,_/  \___/  /___//_/   /  _/         /_____/   /_/ /_/ \___/  /_/      \__, /   / .___/ \__/  \____/ /_/     
                                   /_/                                            /____/   /_/                           
                                                     Kuczi$ - Hipolit Płatek
""")

special = [
'ł',
'€',
'¶',
'ŧ',
'←',
'↓',
'→',
'ø',
'þ',
'æ',
'ß',
'ð',
'đ',
'ŋ',
'ħ',
'ĸ',
'ł',
'~',
'«',
'»',
'¢',
'“',
"'",
'µ',
'ñ',
'!',
'@',
'$', 
'%', 
'^', 
'&', 
'*', 
'(',
')', 
'-', 
'.', 
'+', 
'=', 
'_', 
',', 
'|', 
'?', 
'>', 
'<', 
'/',
'º',
'ª',
'"',
'¬',
'~',
'Ñ',
'·',
'Ł',
'{',
'}',
']',
'm',
'[',
" \ ",
'½',
'',
'\\',
'#']
numbers = [
'0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9']

list = list(string.ascii_letters) + numbers + special 

def encoder():
    keyinput = input('Write your message: ')
    keyinput2 = eval(input('PassCode (alphanumeric passcode only): '))
    sleep(2)
    code = ''
    def encoder2(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2(k)
         code += list[l]
    print('***processing***')
    print("\n"+ "Your encrypted message is: " + code)
    print("\n")
    optionss()

def decoder():
    keyinput = input('Code: ')
    keyinput2 = eval(input('PassCode (alphanumeric passcode only): '))
    sleep(2)
    message = ''
    for k in keyinput:
      if k == ' ':
         message += ' '
      else:
         r = list.index(k)
         l = (r - keyinput2)%(len(list) - 1)
         message += list[l]
    print('***processing***')

    print("\n"+ "Your decrypted message is: " + message)
    print("\n")
    optionss()
def optionss():
   
    print('1) Code Text')
    print('2) Encode Text')
    print('3) Exit')
    opt= int(input("Options: "))
    if opt == 1:
       encoder()
    elif opt == 2:
       decoder()
    else:
       exit()
optionss()
