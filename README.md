# Ransomock
Ransomock is a tool used for mocking windows ransomware behavior written in python3  
  
To run this tool, use the following command  
` python3 ./Ransomock.py`

Configurations can be edited in config.json  
**Please only use demo mode in the current version, as it is not tested on real machine yet**  
With Demo mode enabled, Ransomock will only encrypt/decrypt files in Desktop\demo folder


## Warning
The current version decrypt files back to original file with .txt extension only

## Dependency
Ransomock requires python installed on the machine along with the 'pycrypto' module  
  
Use this script to install pycrypto module  
` python3 -m pip install pycrypto `

## Configuration
Configurations can be changed in config.json

## TO-DO (High to Low Prio)
- Decrypt to original file extensions
- C2 Mock
- arguments for cli usage
