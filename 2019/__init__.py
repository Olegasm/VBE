import check50
import check50.c
#import filecmp

@check50.check()
def exists():
    """aliejus.cpp egzistuoja."""
    check50.exists("aliejus.cpp")
#    check50.include("1.txt", "2.txt") 

@check50.check(exists)
def compiles():
    """aliejus.cpp kompiliuojasi be klaidų."""
    check50.run("g++ aliejus.cpp -lcrypt -lcs50 -lm -o aliejus").exit(0)
    
@check50.check()
def exists_txt():
    """U1.txt egzistuoja."""
    check50.exists("U1.txt")
    
@check50.check()
def exists_reztxt():
    """U1rez.txt egzistuoja."""
    check50.exists("U1rez.txt")
    
@check50.check(compiles)
def test0():
    """teisingai paskaiciuoja pripilta alieju."""
    check50.run("> U1rez.txt")
#    check50.run(./aliejus).exit(0)
        
        

'''
@check50.check(compiles)    
def run_aliejus():
    """Bandom paduoti input ir gauti output is c++ programos."""
    check50.run("./aliejus").stdin("blah").stdout("blah").exit()

@check50.check(compiles)
def test2():
    """Testuoja ar patalpina output i kintamaji."""
    out = check50.run("./programa").stdin("2").stdout()
    check_output(out, open("1.txt").read())    
    
@check50.check(exists)
def isOutput():
    """Rastas U1rez.txt"""
    check50.exists("U1rez.txt")
    
@check50.check(isOutput)    
def read_first_file_line():
    """Ar teisingai apskaičiuoja pripiltų indų ir likusio aliejaus skaičius?"""
    compare_files1(open("U1rez.txt").readline(), open("1.txt").readline())
    
@check50.check(read_first_file_line)
def test1():
    """Tikrina užduoties "Aliejus" korektišką atlikimą"""
    compare_files(open("U1rez.txt").read(), open("1.txt").read())

def compare_files(output, correct):
    if output == correct:
        return 
    raise check50.Mismatch(correct, output, help= None)

def compare_files1(output, correct):
    if output == correct:
        return
    
    help = None
    if output[0] != correct[0]:
        help = "Vieno litro indo pripilymas apskaičiuotas neteisingai"
    raise check50.Mismatch(correct, output, help=help)    

def check_output(output, correct):
    if output == correct:
        return
    
    output = output.splitlines()
    correct = correct.splitlines()

    help = None

    raise check50.Mismatch(correct, output, help=help)    
''' 
#@check50.check(exists)
#def compiles():
#    """U1.c kompiliuojasi"""
#    check50.c.compile("U1.c", lcs50=True)

#bandymas patikrinti ar .cpp file'as kompiliuojasi
# bet neveikia: error: invalid argument '-std=c11' not allowed with 'C++'
#@check50.check(exists)
#def compiles1():
#    """testU1.cpp kompiliuojasi"""
#    check50.c.compile("testU1.cpp", lcs50=True)

# bandymas paleisti sukompiliuota .cpp file'ą, bet nesigauna.
#@check50.check(compiles)
#def testingCPP():
#    """Ar pasileidžia sukompiliuotas CPP file'as"""
#    out = check50.run("./testU1").stdin("1").stdout()
#    out = check50.run("./testU1").stdout()
#    compare_values(out, open("2.txt").read())
#    check50.run("./testU1").stdout(1)
    
# Skirta .cpp output patikrinimui
#def compare_values(output, correct):
#    if output == correct:
#        return 
#    raise check50.Mismatch(correct, output, help= None)
