# -*- coding: utf-8 -*-
import sys
a = []
b = []
c = []
reg = 0
ip = 0

prompt= False

interactive = True

usesys= True

debug = False

# get-single-char code stolen shamelessly from StackOverflow, and also shamelessly ignored in preference of an input queue

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


def adq():
    try:
        return a.pop()
    except:
        return 0
def bdq():
    try:
        return b.pop()
    except:
        return 1
def cdq():
    try:
        return c.pop()
    except:
        return ord(inputqueue())

inputq = []
def inputqueue():
    global inputq
    if len(inputq) == 0:
        inputq = input(" ? : ")+"\n"
    q = inputq[0]
    inputq=inputq[1:]
    return q

def inp():
    global inputq
    from operator import __add__, __sub__
    num = 0    
    op = __add__
    if len(inputq) == 0:
        inputq = input(" ? : ") + "\n"
    if inputq[0] not in "-+0123456789.":
        return num
    if inputq[0] in "-+":
        if inputq[0] in "-":
            op = __sub__
        inputq = inputq[1:]
    while 1:
        if len(inputq) == 0:
            inputq = input(" ? : ")+"\n"
        if inputq[0] in "0123456789":
            num = op(num * 10, int(inputq[0]))
            inputq = inputq[1:]
        else:
            return num
            
def get():
    return reg

def ap():
    try:
        return a[-1]
    except:
        return 0

def bp():
    try:
        return b[-1]
    except:
        return 1

def cp():
    try:
        return c[-1]
    except:
        return reg

def aq(queued):
    a.insert(0,queued)
    return queued
    
def bq(queued):
    b.insert(0,queued)
    return queued

def cq(queued):
    c.insert(0,queued)
    return queued

def rs(queued):
    global reg
    reg = queued
    return queued

def ac():
    return aq(cdq())


def bc():
    return bq(cdq())

def ba():
    return bq(adq())

def ab():
    return aq(bdq())
    
def ca():
    return cq(adq())

def cb():
    return cq(bdq())
    
def pa():
    x = ap()
    if usesys:
        sys.stdout.write(str(x))
        sys.stdout.flush()
    else:
        print(str(x))
    return x
def pb():
    x = bp()
    if usesys:
        sys.stdout.write(str(x))
        sys.stdout.flush()
    else:
        print(x)
    return x
def pc():
    x = cp()
    if usesys:
        sys.stdout.write(str(x))
        sys.stdout.flush()
    else:
        print(str(x))
    return x
    
def pta():
    x = ap()
    if usesys:
        sys.stdout.write(chr(x))
        sys.stdout.flush()
    else:
        print(chr(x))
    return x
def ptb():
    x = bp()
    if usesys:
        sys.stdout.write(chr(x))
        sys.stdout.flush()
    else:
        print(chr(x))
    return x
def ptc():
    x = cp()
    if usesys:
        sys.stdout.write(chr(x))
        sys.stdout.flush()
    else:
        print(chr(x))
    return x 

def wa():    
    global ip
    if ap():
        pass
    else:
        nest = 1
        while nest:
            ip += 1
            if program[ip][0] in [wa,wb,wc,wr]: nest+=1
            elif program[ip][0] in [mrk]: nest -= 1
def wb():
    global ip
    if bp():
        pass
    else:
        nest = 1
        while nest:
            ip += 1
            if program[ip][0] in [wa,wb,wc,wr]: nest+=1
            elif program[ip][0] in [mrk]: nest -= 1

def wc():
    global ip
    if cp():
        pass
    else:
        nest = 1
        while nest:
            ip += 1
            if program[ip][0] in [wa,wb,wc,wr]: nest+=1
            elif program[ip][0] in [mrk]: nest -= 1
def wr():
    global ip
    if reg:
        pass
    else:
        nest = 1
        while nest:
            ip += 1
            if program[ip][0] in [wa,wb,wc,wr]: nest+=1
            elif program[ip][0] in [mrk]: nest -= 1
def al():
    return len(a)
def bl():
    return len(b)
def cl():
    return len(c)

def adda(val):
    return val+adq()

def addb(val):
    return val+bdq()

def addc(val):
    return val+cdq()

def suba(val):
    return val-adq()
def subb(val):
    return val-bdq()
def subc(val):
    return val-cdq()

def inc(val):
    return val+1
def dec(val):
    return val-1
    
def mrk():
    global ip
    nest = 1
    ip-=1
    while nest:
        if program[ip][0] in [wa,wb,wc,wr]: nest-=1
        elif program[ip][0] in [mrk]: nest += 1
        ip -= 1

functions = {
   "a":(adq,0),
   "b":(bdq,0),
   "c":(cdq,0),
   "r":(get,0),
   "A":(aq,1),
   "B":(bq,1),
   "C":(cq,1),
   "R":(rs,1),
   "o":(pa,0),
   "p":(pb,0),
   "q":(pc,0),
   "O":(pta,0),
   "P":(ptb,0),
   "Q":(ptc,0),
   "1":(ap,0),
   "2":(bp,0),
   "3":(cp,0),
   "!":(al,0),
   "@":(bl,0),
   "#":(cl,0),
   "*":(adda,1),
   "+":(addb,1),
   ",":(addc,1),
   "-":(suba,1),
   ".":(subb,1),
   "/":(subc,1),
   "4":(wa,0),
   "5":(wb,0),
   "6":(wc,0),
   "7":(wr,0),
   ")":(inc,1),
   "(":(dec,1),
   "x":(mrk,0),
   "i":(inp,0)}

def tokenize(string):
    global program    
    program = [functions.get(x) for x in string if x in functions.keys()]
    if debug: print(program)

program = []

def interpret():
    global reg
    global ip
    global a
    global b
    global c
    global inputq
    global prompt
    if debug: 
        print("interpreting",len(program))
    while ip < len(program):
        if program[ip][1]:
            reg = program[ip][0](reg)
        elif program[ip][0] in [wa,wb,wc,wr,mrk]:
            program[ip][0]()
        else: reg = program[ip][0]()
        if debug: print("reg",reg,"IP",ip,"a",a,"b",b,"c",c)
        ip+=1
    print()
    ip = 0
    reg = 0
    if debug: print(a,b,c)
    a,b,c,inputq=[],[],[],[]
if __name__ == "__main__":
    while 1:
        
        if prompt:
           i = input(" > : ")
        else:
           with open(sys.argv[0], 'r') as content_file:
                i = content_file.read()
        tokenize(i)
        interpret()
        if not prompt:
            break;
