import check50
import check50.c
#import filecmp

with open('U1.txt') as f:
    lines = f.read().split()

    litras1 = int(lines[0])
    litras3 = int(lines[1])
    litras5 = int(lines[2])

    litras1Likutis = litras1
    litras3Likutis = litras3
    litras5Likutis = litras5

    litras1Reikia = 0;
    litras3Reikia = 0;
    litras5Reikia = 0;

    aliejusPradinis = int(lines[3])
    aliejusLikutis = aliejusPradinis
    aliejuNeispilstytas = 0

    gamybosIslaidos = int(lines[4])

    litras1Kaina = int(lines[5])
    litras3Kaina = int(lines[6])
    litras5Kaina = int(lines[7])

    gautasPelnas = 0

    while(litras5Likutis != 0 and aliejusLikutis >= 5):
        aliejusLikutis -= 5
        litras5Likutis -= 1
    while(litras3Likutis != 0 and aliejusLikutis >= 3):
        aliejusLikutis -= 3
        litras3Likutis -= 1
    while(litras1Likutis != 0 and aliejusLikutis >= 1):
        aliejusLikutis -= 1
        litras1Likutis -= 1

    litras1ispilstyta = litras1 - litras1Likutis
    litras3ispilstyta = litras3 - litras3Likutis
    litras5ispilstyta = litras5 - litras5Likutis
    aliejuNeispilstytas = aliejusLikutis

    while(aliejusLikutis >= 5):
        litras5Reikia += 1
        aliejusLikutis -= 5
    while(aliejusLikutis >= 3):
        litras3Reikia += 1
        aliejusLikutis -= 3
    while(aliejusLikutis >= 1):
        litras1Reikia += 1
        aliejusLikutis -= 1

    gautasPelnas = (((litras1ispilstyta + litras1Reikia) * litras1Kaina
        + (litras3ispilstyta + litras3Reikia) * litras3Kaina
        + (litras5ispilstyta + litras5Reikia) * litras5Kaina) - gamybosIslaidos)
    
@check50.check()
def exists():
    """aliejus.c egzistuoja."""
    #check50.log(lines)
    check50.exists("aliejus.c")
#    check50.include("1.txt", "2.txt") 

@check50.check(exists)
def compiles():
    """aliejus.c kompiliuojasi be klaidų."""
    check50.c.compile("aliejus.c", lcs50=True)
    
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
    if len(lines) != 8:
        raise check50.Failure("file U1.txt turi būti įrasyti aštuoni skaičiai")
# blogai veikia, pabaigti
#    for i in range(len(lines)):
#        if not isinstance(lines[i], int):
#            raise check50.Failure("file U1.txt turi buti buti irasyti tik sveiki skaiciai")


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

