################################
##      MADE BY AMRANI SAAD   ##
##      AKA : [0 x 5 4 4 D]   ##
##      STARTED : 20 Oct 2018 ##
##-----------Contact----------##
##  Facebook: saadox.amrani   ##
##  skype   : saad.amrani3    ##
##  discord : KissM3#4096     ##
################################

import re


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

    ##### String Type #######
    CharsTotal = 100
    #########################


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
    #Algo Condition and Lire Ecrire
    r     = GetAlgo() #Tuple([NumLines].[NumChrs].[LinesArray].[CharsArray])
    words = r[2]
    #words = [w.replace('Ecrire(', 'printf(') for w in words]
    words = [w.replace(') Alors:', ')\n{') for w in words]
    words = [w.replace('SinonSi(', '}\nelse if(') for w in words]
    words = [w.replace('Sinon', '}\nelse\n{') for w in words]
    words = [w.replace('FinSi', '}\n') for w in words]
    words = [w.replace('Si(', 'if(') for w in words]
    words = [w.replace('Debut', 'int main()\n{') for w in words]
    #Lire-ScanfDetect VariablesTypes
    LireVar = ""
    isThereLire = False
    #index of var inside lire() is 5
    for each in words:
        if 'Lire(' in each:
            #Get the variable by () indexes
            LireVar = str(each[each.index('(') +1:each.index(')')]) 
            isThereLire = True
    #Algo Boucles
    words = [w.replace('FinTantQue', '}\n') for w in words]
    words = [w.replace('TantQue', 'while') for w in words]
    words = [w.replace('Faire:', '{') for w in words]
    #Lines for managing scanf("%type",var) and printf();
    AlgoTypes = ['entier','reel','reelf','string','char','bool']
    varLinez = []
    for lin in r[2]:
        for ty in AlgoTypes:
            if ty in lin:
                varLinez += lin
    varLinez = ''.join(varLinez).split('\n')
    varLinez = [ item for item in varLinez if item ] ## will delete empty rows

    #Checking type of varuable used in Lire() 
    VarsAndTypes = LireVariableType(varLinez)
    ij = 0
    for each in VarsAndTypes[1]:
        if LireVar in each:
            break
        ij += 1
    #And Finaly We Got Our Type ha7na readt to type scanf
    if isThereLire :
        typeOfThisVariable =  VarsAndTypes[0][ij]
        if typeOfThisVariable == 'entier':
            words = [w.replace('Lire(', 'scanf("%d",&', 1) for w in words]
        elif typeOfThisVariable == 'reel' or typeOfThisVariable == 'reelf':
            words = [w.replace('Lire(', 'scanf("%lf",&',1) for w in words]
        elif typeOfThisVariable == 'char':
            words = [w.replace('Lire(', 'scanf("%c",&',1) for w in words]
        elif typeOfThisVariable == 'bool': #write 0 or 1
            words = [w.replace('Lire(', 'scanf("%d",&',1) for w in words]
        elif typeOfThisVariable == 'string':
            words = [w.replace('Lire(', 'scanf("%s",&',1) for w in words]
   
    #WORK STOPED HERE #TODO# LIST AFTER
    '''
    #####################################################################
    1 > Probelem in Algo'S Vars :
        lets say our variable is 'a' of type int 
        and we have another variable declared named 'atest' of type double
        when we search in the Table of all algo File's vars generated ,
        to get the type of variable 'a' .. we get the 'atest' since 'a'
        is in 'atest'.
    1 > [Solution that might work]
        We need to get the len(var) to get the exact length ,
        then we compare it with the length founf on our vars Table !
    #####################################################################
    2 > Problem in Replacing Multiple Lire(:
        For example we have Lire(a); with a int 
        and after that we have Lire(b); with B double
        when generating the main.c file both of these gets replaced with :
        scanf("%lf",&var) .. instead  it has to be %lf for double(reel) vars
        and %d for entier(int) vars.
    2 > [Solution possible]
        in words[] i think it replaces every Lire(  with the last
        Lire()'s infos found in the file ..
        probably i gtta replace while searching in the file for Lire( 
        in for loop using str.replace(old,new,max) // max to replace 
        must be once to replace only the first found with it's var types
        then go next and replace it depends on if() statements types of 
        that algo var !
    #####################################################################    
    '''
    print(VarsAndTypes)
    
    #Type de Vars :
    #entier - reel - bool - string - char - ptr(pointers)
    words = [ l.replace(':',';') for l in words]
    words = [ l.replace('variables','') for l in words]
    words = [ l.replace('entier','int ') for l in words]
    words = [ l.replace('reel','double ') for l in words]
    words = [ l.replace('reelf','float ') for l in words]
    words = [ l.replace('bool','bool ') for l in words]
    words = [ l.replace('char','char ') for l in words]
    words = [ l.replace('string','string ') for l in words]
    words = [w.replace('Fin', 'return 0; // matmse7ch hadi\n}') for w in words]
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

def LireVariableType(arrVars):
    tempArr = arrVars

    AlgoTypes = ['entier','reel','reelf','string','char','bool']
    types = []
    newVars = []
    MyDic   = {}

    for each in tempArr:
        lenRow  = len(each)
        for eachvar in AlgoTypes:
            if eachvar in each:
                types += eachvar
                newVars += each[len(eachvar)+1:lenRow]
                newVars = ''.join(newVars)
            MyDic[eachvar] = newVars
        types += '/'
        newVars += '/'
    types = ''.join(types).split('/')
    types = [item for item in types if item]
    newVars = ''.join(newVars).split('/')
   # newVars = ''.join(newVars).split(',')
    newVars = ';'.join(newVars).split(';')

    newVars = [item for item in newVars if item]
    
    return types , newVars#, MyDic

def WriteC():
    c   = cClass()    
    #Writing C Lines
    fs = open(c.FileName,c.FileMode)
    fs.write('#include "saad_Lib/mylib.h" //matmse7ch hadi\n\n')
    listos = Algo2c()[0]
    for line in listos:
        fs.write(line)
    fs.close()


WriteC()
#print(str(Algo2c()[0])+"\n")
#print(str(Algo2c()[1])+"\n")
#print(str(Algo2c()[2])+"\n")
#print("\nLines : "+str(GetAlgo()[0])+"\nCharacters : "+str(GetAlgo()[1])+"\nLine Array : "+str(GetAlgo()[2])+"\nChar Array : "+str(GetAlgo()[3]))

