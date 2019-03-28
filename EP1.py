# EP1

X = input("Digite a string X: ")
Y = input("Digite a string Y: ")
print("Strings sendo comparadas: %s e %s" %(X, Y))
m = len(X)
n = len(Y)
print("%d %d" %(m, n))


def LeArquivoDNA(filename):     # funcao para leitura de arquivos txt
    files=open(filename, 'r')
    lists=files.readlines()              # this is a matrix of nlines
    nlines=len(lists)                    # number of lines
    a = lists[0].rstrip('\n').split(' ') # separa a linhas em colunas
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
    for i in range(m,0,-1):
        for j in range(m,0,-1):
            if i==0 or j==0:
                sol[i][j] = 0
            elif X[i-1]==Y[j-1]:
                sol[i][j] += sol[i-1][j-1]
            else:
                sol[i][j] = max(sol[i-1][j], sol[i][j-1])
    return sol[m][n]

print(MSCnaocont(X,Y,m,n))
