morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}


def morse_to_text(morse_message):
    # Split the morse message into words and then into letters
    words = morse_message.split('   ')  # Words are separated by three spaces
    decoded_message = []

    for word in words:
        letters = word.split(' ')  # Letters are separated by a space
        decoded_word = ''.join([morse_code_dict[letter] for letter in letters])
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)


# Your Morse code message
morse_message = "-.- --.- .- ...- -.. ..- .-- .-. .--- ...- -..- ..- .... -.. -..- -.-- --.. --. -.-- .-- -.- .-- --.. .-- -.- .-. --.- .- -.- ..- .... ..-. ...- -.- -.-- -..- .--. ..-. .-- .... .-. . .-. .. ..-. --.- .- ...- -.. ..- .-- -.- --.- .--- -.- --.- ... .... -.- .- .... --.. --.- -.- .-- -.-- .-. .. ..- -. -..- -.- --.- .-- ..-. --- .-- -..- ...- ..-. ...- ..-. ..- -. -..- .- ..-. . ... -.- .-- .... .-- .... ..-. .- -.- ..- .... ..-. ...- .-- ..-. --- .-- -.- --.- -..- . ..-. .. -.- --.- ..-. . .--. -..- --.- --.- ..-. ...- ... -.- .-- .... .-- .... ..-. .... ..-. -. ..- .-. .. -..- -- ..-. -.. .-- .... ..-. --.. --.- -.- .-- -.-- .--. -..- -.. --. ..-. -.-- -.- --.- .--- -. ..-. -. ..-. .-- .-- ..-. ...- -.-- .-- .... ..-. .--. .-. -.-- .-- .- .-. .--. .--. .-. --.- ..- -..- -.- ...- -.-- .-. .. -. ..-. .-- .-- ..-. ...- -.-- .-- ...- -.- ..- -. ..-. .-- -.-- .-. .. -. ..-. .-- .-- ..-. ...- -.-- .--. -.- --- .-- --.. ...- ..-. -.-- .-. .. .-- .... ..-. -..- --. .-. -... ..-. -..- --.- . -.-- .-. .. .-. ...- .-- .... .-- .... ..-. ...- ..-. .- ..-. -.- -... ..-. ...- . ..-. .- -.- ..- .... ..-. ...- -.-- .-- .... ..-. .-- ..-. --- .-- --. -.. ..- ..-. ...- .. .-. ...- .--. -.- --.- .--- .-- .... ..-. -.- --.- -... ..-. ...- -.-- ..-. -.-- --.. --. -.-- .-- -.- .-- --.. .-- -.- .-. --.- ..- ...- .-. .- ..-. -.-- -.-- .-- .-. ..-. --- .-- ...- -..- .- .-- .-- .... ..-. .-. ...- -.- .--- -.- --.- -..- -. .--. ..-. -.-- -.-- -..- .--- ..-. -.-- --.. --. -.-- .-- -.- .-- --.. .-- -.- .-. --.- .- -.- ..- .... ..-. ...- -.-- .- -..- --.- --. ..-. .- .-. .--. ..- -..- ...- ..-. . ... -.- .-- .... .-- ...- -..- --.- -.-- ..- .-. -.-- -.- .-- -.- .-. --.- .- -.- ..- .... ..-. ...- -.-- -.- --.- -..- .-- ...- -..- --.- -.-- ..- .-. -.-- -.- .-- -.- .-. --.- .- -.- ..- .... ..-. ...- .-- .... ..-. --.. --.- -.- .-- -.-- .-. .. .-- .... ..-. ..- -. -..- -.- --.- .-- ..-. --- .-- -..- ...- ..-. ...- ..-. -..- ...- ...- -..- --.- .--- ..-. . -.- --.- -..- . -.- .. .. ..-. ...- ..-. --.- .-- -..- --.- . --.. -.-- --.. -..- -. -. -.. -.-. --.. -.- .-- ..-. .- .-. .--. ..- -. ..-. --- .-. ...- . ..-. ...- --. --.. .-- .-- .... ..-. --.. --.- -.- .-- -.-- .-- .... ..-. .--. -.-- ..-. -. -... ..-. -.-- -..- ...- ..-. -. ..-. .. .-- --.. --.- .- .... -..- --.- .--- ..-. . --. -.. .- .-. --.- .-- ...- -..- -.-- .-- -.- --.- -..- -.-- --.. --. -.-- .-- -.- .-- --.. .-- -.- .-. --.- .- -.- ..- .... ..-. ...- .-- .... ..-. --.. --.- -.- .-- -.-- .-. .. .-- .... ..-. ..- -. -..- -.- --.- .-- ..-. --- .-- -..- ...- ..-. ...- ..-. .-- -..- -.- --.- ..-. . -.- --.- .-- .... ..-. -.-- -..- .--. ..-. -.-- ..-. -.-. --.. ..-. --.- .- ..-. -.- --.- .-- .... ..-. .- -.- ..- .... ..-. ...- .-- ..-. --- .-- --. --.. .-- .-- .... ..-. --.. --.- -.- .-- -.-- .-- .... ..-. .--. -.-- ..-. -. -... ..-. -.-- -..- ...- ..-. -..- -. .-- ..-. ...- ..-. . ..- -. ..-. -..- -.-- ..-. . ..-. .- .-. . ..-. .-- .... -.- -.-- .-- ..-. --- .-- --.. -.-- -.- --.- .--- -..- --.- -.. .--. ..-. .-- .... .-. . -.. .-. --.. .. -.- --.- . -..- . ..-. -.-. --.. -..- .-- ..-. -.. .-. --.. ... -.- -. -. .. -.- .--- --.. ...- ..-. .-. --.. .-- .-- .... -..- .-- .-- .... ..-. .-- ..-. --- .-- ... -..- -.-- ..-. --.- .- ...- -.. ..- .-- ..-. . --.. -.-- -.- --.- .--- .-- .... ..-. -.-- --.. --. -.-- .-- -.- .-- --.. .-- -.- .-. --.- .- -.- ..- .... ..-. ...- -..- .. .-- ..-. ...- -.. .-. --.. .. .-. --.. --.- . -..- -.-- .-. -. --.. .-- -.- .-. --.- ..- -. ..-. -..- -.-- ..-. . ..-. -.-- .- ...- -.- --. ..-. .... .-. ... -.. .-. --.. -..- --.- -..- -. -.. - ..-. . .-- .... ..-. .-- ..-. --- .-- .... -.- --.- .-- -.. .-. --.. .--. -..- -.. --.. -.-- ..-. -..- --.- -.. ..- ...- .-. .--- ...- -..- .--. .-. ...- -.-- -.- .--. ..- -. -.. .- .-. --.. --.- .-- .-- .... ..-. .. ...- ..-. -.-. --.. ..-. --.- .- -.- ..-. -.-- .-. .. -..- -. -. .-- .... ..-. ..- -.- .- .-- --.. ...- ..-. -.-- .-- .... -..- .-- -..- ..- ..- ..-. -..- ...- ... -.- .-- .... -.- --.- .-- .... ..-. .-- ..-. --- .-- .... -..- -... ..-. .. --.. --.-"

# Decrypt and print the message
decoded_message = morse_to_text(morse_message)
print("Decoded Message:", decoded_message)