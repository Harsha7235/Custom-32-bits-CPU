LOADI 0 5
LOADI 1 3
ADD 0 1
HALT            R0 = 8
                R1 = 3




LOADI 0 10
LOADI 1 4
SUB 0 1
HALT            R0 = 6






LOADI 0 6
LOADI 1 7
MUL 0 1
HALT           R0 = 42





LOADI 0 20
LOADI 1 4
DIV 0 1
HALT           R0 = 5





LOADI 0 25
STORE 0 100
LOAD 1 100
HALT           Memory[100] = 25
               R1 = 25




LOADI 0 10
STORE 0 200

LOADI 1 20
STORE 1 201

LOAD 2 200
LOAD 3 201

ADD 2 3
HALT           R2 = 30





LOADI 0 50
PUSH 0

POP 1
HALT           R1 = 50









LOADI 0 5
LOADI 1 7

PUSH 0
PUSH 1

POP 2
POP 3

ADD 2 3
HALT               R2 = 12




LOADI 0 5
LOADI 1 1

SUB 0 1
JZ 0 6
JMP 2

HALT               5
                   4
                   3
                   2
                   1
                   0 





LOADI 0 10
CALL 4
LOADI 1 2
ADD 0 1
RET              R0 = 12







LOADI 0 5
LOADI 1 1
LOADI 2 1

MUL 1 0
SUB 0 2
JZ 0 7
JMP 3

HALT                 R1 = 120








LOADI 0 0
LOADI 1 1
LOADI 2 5

ADD 0 1
SUB 2 1
JZ 2 7
JMP 3

HALT                    










push constant 5
push constant 3
add                           LOADI 1 5
                              PUSH 1
                              LOADI 1 3
                              PUSH 1
                              POP 2
                              POP 1
                              ADD 1 2 
                              PUSH 1



push constant 2
push constant 3
add
push constant 4
add                        (2+3)+4 = 9










push constant 10
push constant 20
push constant 30
add
add                        60




LOADI 0 5
LOADI 1 10

ADD 0 1

STORE 0 300

LOAD 2 300

PUSH 2
POP 3

HALT                         R0 = 15
                             R2 = 15
                             R3 = 15



LOADI 0 10
LOADI 1 0
DIV 0 1
HALT