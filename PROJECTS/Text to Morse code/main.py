morse_code = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.' , ' ': '/',

    #punctuations
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', ':': '---...', ';': '-.-.-.',
    '(': '-.--.-', ')': '-.--.-', '"': '.-..-.',
    "'": '.----.', '@': '.--.-.', '/': '-..-.',
    '-': '-....-', '=': '-...-'
}



def text_to_morse(sentence):
    sentence=sentence.upper().split(' ')
    sentence=[word for word in sentence if word]
    if len(sentence)==0:
        return f"Error: Empty input. Please enter text to convert."
    sentence=' '.join(sentence)
    morsed_sentence=''
    
    for i in sentence:
        if i in morse_code:
            morsed_sentence+=morse_code[i]+' '   
        else:
            return (f"Error: Unsupported character {i} found") 
        
    return (f'The morse code is : {morsed_sentence[:-1]}')

ask=input("Enter the text you want to convert to the morse code : ")

morphed_sentence=text_to_morse(ask)

print(morphed_sentence)


