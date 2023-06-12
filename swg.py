import os

def strAPT():
    return 'qazqazqazqazqazqazqazqazqazqaz'

def strOBJ():
    return 'wsxwsxwsxwsxwsxwsxwsxwsxwsxwsx','wsxwsxwsxwsxwsxwsxwsxwsxwsxwsx','qazqazqazqazqazqazqazqazqazqaz'

def strMESH():
    return 'qazqazqazqazqazqazqazqazqazqaz'

def strSHT():
    return 'qazqazqazqazqazqazqazqazqazqaz'



def strSchem(WHICH_SCHEM = 'doesntmatter'):
    if WHICH_SCHEM == "structure":
        return 'wsxwsxwsxwsxwsxwsxwsxwsxwsxwsx'
    return 'wsxwsxwsxwsxwsxwsxwsxwsxwsxwsx'

def index_of_bytes(data, pattern):
    for i in range(len(data) - len(pattern) + 1):
        if data[i:i+len(pattern)] == pattern:
            return i
    return -1

def nname(oname):
    a = 30
    rex = oname
    if len(rex) > a:
        print("new text is too long")
        return
    elif len(rex) < a:
        ld = a - len(rex)
        rex += '_'
        if ld > 1:
            for i in range(ld - 1):
                rex += '0'
        
    return rex

def setCardsOut(rt):
    dlist = os.listdir('output/' + rt + '/')
    path = 'output/' + rt + '/' + rt + str(len(dlist)) + '/'
    os.mkdir(path)
    os.mkdir(path + '/appearance/')
    os.mkdir(path + '/appearance/mesh/')
    os.mkdir(path + '/object/')
    os.mkdir(path + '/object/tangible/')
    os.mkdir(path + '/object/tangible/cards/')
    os.mkdir(path + '/shader/')
    os.mkdir(path + '/texture/')
    os.mkdir(path + '/lua/')
    os.mkdir(path + '/lua/object/')
    os.mkdir(path + '/lua/object/tangible/')
    os.mkdir(path + '/lua/object/tangible/cards/')
    os.mkdir(path + '/lua/lootObjects/')
    return path

def replace_text_in_file(file_name, old_text, new_text, new_file_name):
    with open(file_name, 'rb') as file:
        file_bytes = file.read()
    
    if len(new_text) > len(old_text):
        print("new text is too long")
        return
    elif len(new_text) < len(old_text):
        ld = len(old_text) - len(new_text)
        new_text += '_'
        if ld > 1:
            for i in range(ld - 1):
                new_text += '0'
    
    old_bytes = old_text.encode('utf-8')
    new_bytes = new_text.encode('utf-8')
    
    index = index_of_bytes(file_bytes, old_bytes)
    
    if index < 0:
        print("Text was not found")
        return
    
    new_file_bytes = file_bytes[:index] + new_bytes + file_bytes[index + len(old_bytes):]

    with open(new_file_name, 'wb') as file:
        file.write(new_file_bytes)