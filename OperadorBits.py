#Definimos las compuertas lógicas 
def AND (a,b):
    return a & b

def OR (a,b):
    return a | b

def NOT (a):
    return 1-a

def XOR (a,b):
    return AND(
        OR(a,b), 
        NOT(AND(a,b))
    )
    
#Definimos el sumador 
def adder(a,b,C_in):

    #S = A XOR B XOR CIN
    #CIN = C_in //Variable que declara el Carry

    axorb= XOR(a,b)
    
    #La suma es la unión de axorb con el carry
    suma = XOR (axorb, C_in)

    #C_out = (A AND B) OR (Cin AND (A XOR B))
    C_out = OR(
        AND(a,b), 
        AND (C_in, axorb)
    )

    return suma, C_out

#Definimos el Sumador y restador de 4 bits
def sumador_restador_4_bits(A,B,M):

    """
    A,B: Listas de 4 bits [A3,A2,A1,A0]-> En binario, pero en este codigo se representa así [A0, A1, A2, A3]
    M = 0 -> SUMA
    M = 1 -> RESTA
    """

    Res =[0, 0, 0, 0]

    #Si M = 1 Se invierte B
    B_mod = [XOR(bit, M) for bit in B]
    #Carry es lo que pasa al siguiente bit
    carry = M #Suma el +1 cuando es resta 

    # Propagación del carry desde el bit menos significativo
    for i in range(4):
        Res[i], carry = adder(A[i], B_mod[i], carry)

    return Res, carry

# Representación: [A0, A1, A2, A3]
A = [1,0,1,0]   # 5 en binario 0101
B = [1,1,0,0]   # 3 en binario 0011

suma, carry_suma = sumador_restador_4_bits(A, B, 0)
resta, carry_resta = sumador_restador_4_bits(A, B, 1)

# Convertimos a forma más legible (MSB a LSB)---> Del bit más significativo al menos significativo 
print("Suma:   ", suma[::-1], "Carry:", carry_suma)   # [1,0,0,0]
print("Resta:  ", resta[::-1], "Carry:", carry_resta)  # [0,0,1,0]

