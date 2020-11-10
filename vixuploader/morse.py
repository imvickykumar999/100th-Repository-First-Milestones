
def solve(test, printing = False):
    
    decrypted = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '0', ',', '?', '(', ')', '!']

    encrypted = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                 '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
                 '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                 '-..-', '-.--', '--..', '.----', '..---', '...--', '....-',
                 '.....', '-....', '--...', '---..', '----.', '-----', '--..--',
                 '..--..', '-.--.', '-.--.-', '-.-.--']

    morse_enc = dict(zip(decrypted, encrypted))
    morse_dec = dict([(encrypted, decrypted) for decrypted,
                      encrypted in morse_enc.items()])

    if test == '':
        test = '-.. . -.- .... / .-.. .. -.-- .- / -.-. .... .- .-.. / -. .. -.- .- .-..'

    test = test.replace("_", "-").upper()
    test_list = test.split(' ')

    decrypt = []
    def convert(j):
        for i in j:
            try:
                decrypt.append((morse_enc[i]))
            except:
                try:
                    decrypt.append((morse_dec[i]))
                except:
                    pass

    if not any(ele in encrypted for ele in test_list):
        box=[]
        for i in test_list:
            box.append(i+' ')
        test_list = box

        for j in test_list:
            convert(j)
            text = ' '.join(decrypt)
    else:
        convert(test_list)
        text = ''.join(decrypt)

    if printing == True:
        print('\nInput : ', test)
        print('Output : ', text)

    return text

# test = input('Enter Morse Text (or, just Press Enter for default entry) : ')
# solve(test, True) # use either True, printing=True, or 1
