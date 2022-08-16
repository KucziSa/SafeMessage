from json import encoder
import string,os
from time import sleep
lang = 2

def logo():
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
'#',
'ä',
'ö',
'Ü',
'ü',
'Ä',
'Ö',
'Ę',
'ę',
'ó',
'Ą',
'ą',
'Ó',
'Ś',
'ś',
'Ź',
'ź',
'ż',
'Ż',
'Ć',
'ć',
'Ń',
'ń'];
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




#Options
def optionssde():
   #German
          logo()
          print('1) Textverschlüsselung')
          print('2) Textentschlüsselung')
          print('3) Exit')
          try: 
            opt= int(input("Options: "))
          except:
            print('Versuchen Sie eine Zahl zu schreiben.')
            sleep(2)
            optionssde()

          if opt == 1:
            encoderde()
          elif opt == 2:
            decoderde()
          else:
            print("Auf Wiedersehen!")
            sleep(2)
            exit()

def optionssen():
      #English
      logo()
      print('1) Code Text')
      print('2) Encode Text')
      print('3) Exit')
      try: 
            opt= int(input("Options: "))
      except:
         print('Try with a number.')
         sleep(2)
         optionssde()
      if opt == 1:
         encoderen()
      elif opt == 2:
         decoderen()
      else:
         print("Goodbye!")
         sleep(2)
         exit()

def optionsspl():
   #Polish
      logo()
      print('1) Zaszyfruj tekst')
      print('2) Odszyfruj tekst')
      print('3) Exit')
      try: 
            opt= int(input("Options: "))
      except:
         print('Spróbuj wpisać cyfrę')
         sleep(2)
         optionssde()
      if opt == 1:
         encoderpl()
      elif opt == 2:
         decoderpl()
      else:
         print("Goodbye!")
         sleep(2)
         exit()

   






#German encoder
def encoderde():
    keyinput = input('Schreiben Sie ihre Nachricht: ')
    try: 
      keyinput2 = eval(input('Passwort (nur alphanumeric Passwort): '))
    except:
      print('Error: Passwort muss nur aus Zahlen bestehen.')
      sleep(2)
      encoderde()    
    sleep(2)
    code = ''
    def encoder2de(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2de(k)
         code += list[l]
    print('***Verarbeitung***')
    print("\n"+ "Ihre verschlüsselte Nachricht ist:  " + code)
    print("\n")
    optionssde()


def decoderde():
    keyinput = input('Code: ')
    try:
      keyinput2 = eval(input('Passwort (nur alphanumeric Passwort): '))
    except:
      print('Error: Passwort muss nur aus Zahlen bestehen.')
      sleep(2)
      decoderde()

    sleep(2)
    message = ''
    for k in keyinput:
      if k == ' ':
         message += ' '
      else:
         r = list.index(k)
         l = (r - keyinput2)%(len(list) - 1)
         message += list[l]
    print('***Verarbeitung***')

    print("\n"+ "Ihre entschlüsselte Nachricht ist:  " + message)
    print("\n")
    optionssde()


#English
def encoderen():
    keyinput = input('Write your message: ')
    keyinput2 = eval(input('PassCode (alphanumeric passcode only): '))
    sleep(2)
    code = ''
    def encoder2en(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2en(k)
         code += list[l]
    print('***processing***')
    print("\n"+ "Your encrypted message is: " + code)
    print("\n")
    optionssen()

def decoderen():
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
    optionssen()

#Polish
def encoderpl():
    keyinput = input('Wpisz wiadomość: ')
    keyinput2 = eval(input('Hasło (Tylko hasło alfanumeryczne): '))
    sleep(2)
    code = ''
    def encoder2pl(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2pl(k)
         code += list[l]
    print('***przetwarzam***')
    print("\n"+ "Twoja zaszyfrowana wiadomość to: " + code)
    print("\n")
    optionsspl()

def decoderpl():
    keyinput = input('Code: ')
    keyinput2 = eval(input('Hasło (tylko hasło alfanumeryczne): '))
    sleep(2)
    message = ''
    for k in keyinput:
      if k == ' ':
         message += ' '
      else:
         r = list.index(k)
         l = (r - keyinput2)%(len(list) - 1)
         message += list[l]
    print('***przetwarzam***')

    print("\n"+ "Twoja odszyfrowana wiadomość to: " + message)
    print("\n")
    optionsspl()





#Choose language
def language():
   logo()
   print('1) German')
   print('2) English')
   print('3) Polish')
   try:
      opt = int(input("Options: "))
   except:
      print('\n')
      print('Please type a number.')
   if opt == 1:
      optionssde()
   elif opt == 3:
      optionsspl()
   else:
      optionssen()

language()
