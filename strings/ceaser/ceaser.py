def caesarCipherEncryptor(string, key):
    # Write your code here.
    encrypted_string = ''
    for char in string:
        result_char_int = ord(char) + (key % 26)
        if result_char_int > 122:
            result_char_int -= 26
        encrypted_string += chr(result_char_int)
    return encrypted_string

a = "ovmqkwtujqmfkao"
key = 52
result = caesarCipherEncryptor(a, key)
print(result)