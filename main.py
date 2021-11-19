MORSE_ALPHABET = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
}


def get_text():
    text_data: str = input('Enter text to convert:\n').lower()
    return text_data


def lookup_morse_alphabet(letter):
    code_letter = ''
    if letter in MORSE_ALPHABET:
        code_letter = MORSE_ALPHABET[letter]
    elif letter == ' ':
        code_letter = ' / '
    else:
        pass
    return code_letter


def convert_to_morse(input_text):
    converted_text = ''
    for letter in input_text:
        converted_text += f'{lookup_morse_alphabet(letter)} '
    return converted_text


def output_morse(morse_code):
    print('Converted code (\' / \' as a word separator):')
    print(morse_code)


if __name__ == '__main__':
    text = get_text()
    converted_code = convert_to_morse(text)
    output_morse(converted_code)
