import numpy as np
import h5py

def hasKeys(item):
    try:
        item.keys()
        return True
    except:
        return False

def isRecarrayLike(item):
    if not (isinstance(item, np.ndarray)):
        return False
    elif isinstance(item,np.recarray):
        return True
    elif (isinstance(item,np.ndarray) and item.dtype.names != None):
        return True

def is__I3Index__(parent,child):
    if ("__I3Index" in parent) or ("__I3Index" in child):
        return True
    else:
        return False

def isDataSet(h5File,path):
    if not path in h5File:
        return True
    elif isinstance(h5File[path], h5py.Dataset):
        return True
    elif isinstance(h5File[path],np.ndarray):
        return True
    else:
        return False

def makeFileStr(pathToDset, H5File):
    keys = []
    while not pathToDset in H5File:
        print
        _ = pathToDset.split("/")
        pathToDset = ("/").join(_[:-1])
        keys.append(_[-1])
    keys = keys[::-1]
    fileStr = "['%s'][()]" % pathToDset
    for key in keys:
        fileStr = "%s['%s']" % (fileStr, key)
    return fileStr

pyString1 = "import numpy as np\nimport h5py\n\nclass "

pyString2 = "():\n\n\tdef __init__(self):\n\t\tself.h5File = h5py.File('"

pyString3 = "', 'r')\n"
