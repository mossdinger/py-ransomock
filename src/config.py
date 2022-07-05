import os


def getPath(isDemo):
    if (isDemo == "True"):
        return [os.environ['HOME'] + "\Desktop\Demo"]
    else:
        return ["C:\ "]
