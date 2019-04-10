# EP1
import numpy as np          # importa biblioteca para uso de matrizes
import re

def LeArquivoDNA(filename):     # funcao para leitura de arquivos txt
    files=open(filename, 'r')
    lists=files.readlines()              # this is a matrix of nlines
    nlines=len(lists)                    # number of lines
    a = lists[0].rstrip('\n').split(' ') # separa as linhas em colunas
    # observa o espaco ' ' como
    # caracter de separacao
    # descarta \n
    cadeiacompleta = a[1] + a[2] + a[3] + a[4] + a[5] + a[6]
    # concatena as colunas 1..6 ignora a[0]
    # agora que cadeiacompleta nao e' vazio faca ate o final
    for i in range(1,nlines):
        a=lists[i].rstrip('\n').split(' ')
        cadeiacompleta = cadeiacompleta + a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
    # retorna a string completa
    return cadeiacompleta

def MSC(X,Y,m,n):               # funcao para verificar a maior
                                # sequencia de caracteres nao contiguos e contiguos  
    sol = np.zeros((m+1,n+1))
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                sol[i][j] = 0
            elif X[i-1]==Y[j-1]:
                sol[i][j] = sol[i-1][j-1] + 1
            else:
                sol[i][j] = max(sol[i-1][j], sol[i][j-1])
    comp = int(sol[m][n])
    cont = comp
    seq = [""]*(cont+1)

    i,j = m,n
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            seq[cont-1]=X[i-1]
            i-=1
            j-=1
            cont-=1
        elif sol[i-1][j]>sol[i][j-1]:
            i-=1
        else:
            j-=1

    seqcontinua = ""
    for k in range(1,m+1):
        for l in range(1,n+1):
            aux = ""
            if X[k-1]==Y[l-1]:
                r = k-1
                s = l-1
                continua = True
                while r<(m-1) and s<(n-1) and continua:
                    aux += X[r]
                    r += 1
                    s += 1
                    if X[r]==Y[s]:
                        continua = True
                    else:
                        continua = False
                a = len(seqcontinua)
                b = len(aux)
                if b>a:
                    seqcontinua = aux        
    return comp, seq, seqcontinua

def gravaArquivo(textos, nome):
    arq = open('{}.txt'.format(nome), 'w')
    for string in textos:
        arq.write(string + " (" + str(len(string)) +")\n")
    arq.close()
    return arq

def main():
    nome = input("Digite o nome do arquivo onde serão armazenados os resultados (sem a extensão): ")
    X = input("Digite a string X ou o nome de um arquivo (com a extensão): ")
    Y = input("Digite a string Y ou o nome de um arquivo (com a extensão): ")
    if (re.match("\w+\.txt$", X)):
        X = LeArquivoDNA(X)
    if (re.match("\w+\.txt$", Y)):
        Y = LeArquivoDNA(Y)
    print("Strings sendo comparadas: %s e %s" %(X, Y))
    m = len(X)
    n = len(Y)
    print("%d %d" %(m, n))
    a,b,c = MSC(X,Y,m,n)
    b = "".join(b)
    gravaArquivo([X, Y, b, c], nome)
    print("Maior subsequência de caracteres não contíguos é %s"%b)
    print("Seu comprimento é %d" %a)
    print("Maior subsequência de caracteres contíguos é %s"%c)
    print("Seu comprimento é %d" %(len(c)))

if __name__== "__main__":
  main()
