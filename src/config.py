import os

def getPath(isDemo):
    if (isDemo):
        return [ os.getenv('HOME') + "/Desktop/Demo"]
    else:
        return [ "C:// "]
