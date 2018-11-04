from numpy import *

class AlgoClass:
    FileName   = "algo.ofppt"
    FileMode   = "r+"
    
    TotalLines = 0
    LinesArray = []
    
    TotalChars = 0
    CharsArray = []

class cClass:
    FileName   = "main.c"
    FileMode   = "w"
    
    TotalLines = 0
    LinesArray = []
    
    TotalChars = 0
    CharsArray = []


def GetAlgo(): #Ret Tuple([NumLines].[NumChrs].[LinesArray].[CharsArray])
    a   = AlgoClass()
    op  = open(a.FileName,a.FileMode)
    opr = op.read()
    
    with open(a.FileName,a.FileMode) as f:
        a.LinesArray = f.readlines()
        a.TotalLines = len(a.LinesArray)
        f.close()
    
    for item in opr:
        a.CharsArray += item
        a.TotalChars += 1
    op.close()
    return a.TotalLines, a.TotalChars, a.LinesArray, a.CharsArray


def Algo2c():
    #Algo Syntax
    r     = GetAlgo() #Tuple([NumLines].[NumChrs].[LinesArray].[CharsArray])
    words = r[2]
    words = [w.replace('Ecrire(', 'printf(') for w in words]
    words = [w.replace('Lire(', 'scanf("%d",') for w in words]
    words = [w.replace(') Alors:', ')\n{') for w in words]
    words = [w.replace('SinonSi(', '}\nelse if(') for w in words]
    words = [w.replace('Sinon', '}\nelse\n{') for w in words]
    words = [w.replace('FinSi', '}\n') for w in words]
    words = [w.replace('Si(', 'if(') for w in words]
    words = [w.replace('Debut', 'main()\n{') for w in words]
    words = [w.replace('Fin', '}') for w in words]
    #Type de Vars :
    #entier - reel - bool - string - char - ptr(pointers)
    words = [ l.replace(':',';') for l in words]
    words = [ l.replace('Variables','') for l in words]
    words = [ l.replace('entier','int ') for l in words]
    words = [ l.replace('reel','double ') for l in words]
    words = [ l.replace('reelf','float ') for l in words]
    words = [ l.replace('bool','bool ') for l in words]
    words = [ l.replace('char','char ') for l in words]
    words = [ l.replace('string','string ') for l in words]
    words = ''.join(words)
    dbvar    = ['int','double','bool','string','char']
    tmp      = []
    typeTmp  = []

    for vty in dbvar:
        if vty in words:
            ind      = words.index(vty)
            typeTmp += vty+'.'
            location = str(ind)+"-"+str(ind+len(vty)-1)+"." 
            tmp   += location
    #Managing Indexs f lwl
    tmp = ''.join(tmp)
    tmp = tmp.split('.')
    tmp = ' '.join(tmp).split()
    #Managing Types Apres
    typeTmp = ''.join(typeTmp)
    typeTmp = typeTmp.split('.')
    typeTmp = ' '.join(typeTmp).split()
    #Ret
    return words, tmp, typeTmp


def WriteC():
    c   = cClass()    
    #Writing C Lines
    fs = open(c.FileName,c.FileMode)
    listos = Algo2c()[0]
    for line in listos:
        fs.write(line)
    fs.close()

WriteC()
print(str(Algo2c()[0])+"\n")
print(str(Algo2c()[1])+"\n")
print(str(Algo2c()[2])+"\n")
#print("\nLines : "+str(GetAlgo()[0])+"\nCharacters : "+str(GetAlgo()[1])+"\nLine Array : "+str(GetAlgo()[2])+"\nChar Array : "+str(GetAlgo()[3]))

