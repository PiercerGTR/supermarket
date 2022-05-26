keyvalues=['name','category','subcategory','amount']

def getkeys(value:dict)->bool:
    for key,_ in value.items():
        if key not in keyvalues and len(value) != 1:
            return False
    return True

def postkeys(value:dict)->bool:
    keylist=list(value.keys())
    if len(keylist)!=len(keyvalues):
        return False
    return sorted(keyvalues) == sorted(keylist)