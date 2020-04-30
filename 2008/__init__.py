import check50
import check50.c

with open('U1.txt') as f:
    lines = f.read().split()
    stoteleIlipo = [0] * (int(lines[0])+1)
    stoteleIslipo = [0] * (int(lines[0])+1)
    try:
        for eilute in range(1,int(lines[0])+1):
            srautas = int(lines[eilute*2])
            indeksas = int(lines[eilute*2-1])
            if (srautas) > 1:
                stoteleIlipo[indeksas] += srautas
            else:
                stoteleIslipo[indeksas] += srautas
    except:
        pass
#print(stoteleIlipo)
#print(stoteleIslipo)
#print(max(stoteleIlipo))
    
@check50.check()
def exists():
    """tyrimai.cpp egzistuoja."""
    check50.exists("tyrimai.cpp")
#    check50.include("1.txt", "2.txt") 

@check50.check(exists)
def compiles():
    """tyrimai.cpp kompiliuojasi be klaidų."""
    check50.run("g++ tyrimai.cpp -lcrypt -lcs50 -lm -o tyrimai").exit(0)
    
@check50.check(compiles)
def exists_txt():
    """U1.txt egzistuoja."""
    check50.exists("U1.txt")
    
@check50.check(compiles)
def exists_reztxt():
    """U1rez.txt egzistuoja."""
    check50.exists("U1rez.txt")
     
@check50.check(exists)
def test0():
    """Informacija faile U1.txt yra surašyta teisingai"""
    if not lines:
        raise check50.Failure("file U1.txt yra tusčias")
#    if len(lines) != int(lines[0])*2+1:
#        raise check50.Failure("Patikrinkite ar faile U1.txt pakankamai įrašyta skaičių)
# blogai veikia, pabaigti
#    for i in range(len(lines)):
#        if not isinstance(lines[i], int):
#            raise check50.Failure("file U1.txt turi buti buti irasyti tik sveiki skaiciai")

'''
@check50.check(compiles)
def test1():
    """Teisingai paskaičiuoja aliejaus išpilstyma į esamus indus"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    with open('U1rez.txt') as f1:
        linesRez = f1.read().split()
        if(len(linesRez) < 3):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if ((str(litras1ispilstyta) == linesRez[0]) and (str(litras3ispilstyta) == linesRez[1]) and (str(litras5ispilstyta) == linesRez[2])):
                pass
            else:
                raise check50.Failure("Blogai suskaičiuotas ispilstytas aliejus")
            
@check50.check(compiles)
def test2():
    """Teisingai paskaičiuoja aliejaus likutį"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    with open('U1rez.txt') as f2:
        linesRez = f2.read().split()
        if(len(linesRez) < 4):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if (str(aliejuNeispilstytas) != linesRez[3]):
                raise check50.Failure("Blogai suskaičiuotas ispilstytas aliejus")                    

@check50.check(test1)
def test3():
    """Teisingai paskaičiuoja nepanaudotų indų kiekį"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    with open('U1rez.txt') as f1:
        linesRez = f1.read().split()
        if(len(linesRez) < 7):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if ((str(litras1Likutis) == linesRez[4]) and (str(litras3Likutis) == linesRez[5]) and (str(litras5Likutis) == linesRez[6])):
                pass
            else:
                raise check50.Failure("Blogai suskaičiuota kiek liko nepanaudotų indų")
                
@check50.check(test2)
def test4():
    """Teisingai paskaičiuoja reikiamų papildomų indų kiekį"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    with open('U1rez.txt') as f1:
        linesRez = f1.read().split()
        if(len(linesRez) < 10):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if ((str(litras1Reikia) == linesRez[7]) and (str(litras3Reikia) == linesRez[8]) and (str(litras5Reikia) == linesRez[9])):
                pass
            else:
                raise check50.Failure("Blogai suskaičiuota kiek reikia papildomai indų likusiam aliejui išpilstyti")
                
@check50.check(test4)
def test5():
    """Teisingai paskaičiuoja gautą pelną"""
    check50.run("> U1rez.txt").exit(0)
    check50.run("./aliejus").exit(0)
    with open('U1rez.txt') as f1:
        linesRez = f1.read().split()
        if(len(linesRez) < 11):
            raise check50.Failure("File U1rez.txt nepakanka duomenų")
        else:
            if (str(gautasPelnas) != linesRez[10]):
                raise check50.Failure("Blogai suskaičiuoja gautą pelną")
'''
