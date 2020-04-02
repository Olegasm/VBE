import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdout("Emma").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdout("Rodrigo").exit()

#@check50.check(compiles)    
#def myTest():
#    """Bandom paduoti input ir gauti output is c programos"""
#    check50.run("./programa").stdin("blah", timeout=60).stdout("blah", timeout=60).exit(timeout=60)
