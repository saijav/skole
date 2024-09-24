# Define the Unicode to numeric mapping
unicode_map = {
    '𝟣': 1, '𝟤': 2, '𝟥': 3, '𝟦': 4, '𝟧': 5, '𝟨': 6, '𝟩': 7, '𝟪': 8, '𝟫': 9,
    '𝟢': 0,
    '𝖠': 10, '𝖡': 11, '𝖢': 12, '𝖣': 13, '𝖤': 14, '𝖥': 15
}

# Create a reverse mapping from numbers to Unicode characters
reverse_unicode_map = {v: k for k, v in unicode_map.items()}

# Input: message and ciphertext as stylized digits
message = "𝟦𝖢𝟦𝟫𝟦𝟨𝟦𝟧𝟦𝟫𝟧𝟥𝟦𝖢𝟦𝟫𝟦𝖡𝟦𝟧𝟦𝟣𝟦𝟤𝟦𝖥𝟧𝟪𝟦𝖥𝟦𝟨𝟦𝟥𝟦𝟪𝟦𝖥𝟦𝟥𝟦𝖥𝟦𝖢𝟦𝟣𝟧𝟦𝟦𝟧𝟧𝟥"
cipher = "𝟣𝖤𝟣𝟫𝟢𝟦𝟣𝖥𝟣𝟫𝟢𝟧𝟣𝟦𝟢𝟣𝟢𝟨𝟣𝟣𝟣𝟪𝟣𝟧𝟢𝟫𝟢𝖠𝟣𝟧𝟣𝟦𝟢𝖢𝟢𝟧𝟢𝟢𝟣𝟩𝟢𝟢𝟣𝟫𝟣𝟫𝟢𝟨𝟣𝖢𝟣𝟦"

# Convert the message and cipher into their numeric forms
message_digits = [unicode_map[ch] for ch in message]
cipher_digits = [unicode_map[ch] for ch in cipher]

# Compute the OTP key
otp_key_digits = [m ^ c for m, c in zip(message_digits, cipher_digits)]

# Convert the OTP key back to stylized characters
otp_key = ''.join(reverse_unicode_map[d] for d in otp_key_digits)

print("OTP Key:", otp_key)
# Define the Unicode to numeric mapping
"""unicode_map = {
    '𝟣': 1, '𝟤': 2, '𝟥': 3, '𝟦': 4, '𝟧': 5, '𝟨': 6, '𝟩': 7, '𝟪': 8, '𝟫': 9,
    '𝟢': 0,
    '𝖠': 10, '𝖡': 11, '𝖢': 12, '𝖣': 13, '𝖤': 14, '𝖥': 15
}

# Create a reverse mapping from numbers to Unicode characters
reverse_unicode_map = {v: k for k, v in unicode_map.items()}

# Input: cipher text and OTP key as stylized digits
cipher_text = "𝟢𝖡𝟣𝖥𝟣𝟩𝟣𝟦𝟣𝟧𝟢𝟢𝟣𝖣𝟣𝖠𝟢𝟨𝟣𝖠𝟣𝟨𝟢𝟢𝟣𝟣𝟣𝖠𝟣𝖡𝟢𝟨𝟣𝟨𝟢𝟤𝟣𝖠𝟢𝟥𝟢𝟨𝟣𝟫𝟣𝟦𝟣𝟧𝟣𝖢𝟣𝟥"
otp_key = "𝟧𝟤𝟧𝟢𝟦𝟤𝟧𝖠𝟧𝟢𝟧𝟨𝟧𝟪𝟦𝟪𝟦𝖣𝟧𝟦𝟧𝟫𝟧𝟩𝟦𝟨𝟧𝟤𝟧𝖠𝟧𝟤𝟦𝖥𝟦𝖣𝟦𝖥𝟧𝟦𝟦𝖥𝟧𝟧𝟧𝟪𝟧𝟤𝟧𝟫𝟦𝟩"

# Convert the cipher text and OTP key into their numeric forms
cipher_digits = [unicode_map[ch] for ch in cipher_text]
otp_digits = [unicode_map[ch] for ch in otp_key]

# Decrypt the cipher text using the OTP key
plaintext_digits = [c ^ o for c, o in zip(cipher_digits, otp_digits)]

# Convert the plaintext digits back to stylized characters
plaintext = ''.join(reverse_unicode_map[d] for d in plaintext_digits)

print("Plaintext:", plaintext)"""

