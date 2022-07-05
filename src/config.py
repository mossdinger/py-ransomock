import os


def getPath(isDemo):
    if (isDemo):
        return [os.environ['HOME'] + "\Desktop\Demo"]
    else:
        return ["C:\ "]
