# EP1
import numpy as np

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

def MSCnaocont(X,Y,m,n):       # funcao para verificar a maior
                               # sequencia de caracteres nao contiguos   
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
    return comp, seq

def main():
    X = input("Digite a string X ou o nome de um arquivo: ")
    Y = input("Digite a string Y ou o nome de um arquivo: ")
    print("Strings sendo comparadas: %s e %s" %(X, Y))
    if (X == "DengueVirus2StrainBA05i_Jakarta" or X == "DengueVirus3StrainTB55i_KualaLumpur" or 
    X == "InfluenzaTypeA_H1N1_California" or X == "InfluenzaTypeA_H3N2_NewYork" and 
    Y == "DengueVirus2StrainBA05i_Jakarta" or Y == "DengueVirus3StrainTB55i_KualaLumpur" or 
    Y == "InfluenzaTypeA_H1N1_California" or Y == "InfluenzaTypeA_H3N2_NewYork"):
        X = LeArquivoDNA(X+".txt") 
        Y = LeArquivoDNA(Y+".txt")
    m = len(X)
    n = len(Y)
    print("%d %d" %(m, n))
    a,b = MSCnaocont(X,Y,m,n)
    print("Maior subsequência de caracteres não contíguos é " + "".join(b))
    print("Seu comprimento é %d" %a)

if __name__== "__main__":
  main()
