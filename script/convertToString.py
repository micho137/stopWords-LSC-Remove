def convertToString(list):
    cadena = ' '.join(list).replace("[","").replace("]","")
    #cadena = str(list).replace("[","").replace("]","") # Este cadena nos deja las palabras entre comillas simples ''
    return cadena