import numpy as np
import scipy as sp

def gaus_scipy(matriz, n):
    A = np.zeros((n,n))
    b = np.zeros((n,1))

    for i in range(n):
        for j in range(n):
            if j == n-1:
                b[i]= matriz[i][j+1]
            A[i][j] = matriz[i][j]

    S = sp.linalg.solve(A, b)
    
    return S

def gaussJordan(matrix, n):
  for i in range(n):
    if matrix[i][i] == 0:
      print("erro!")
    for j in range(n):
      if i != j:
        fator = matrix[j][i]/matrix[i][i]
        for k in range(n+1):
          matrix[j][k] = matrix[j][k] - (fator * matrix[i][k])

  for i in range(n):
      x[i] = matrix[i][n]/matrix[i][i]
      
  return x


n = int(input('digite o numero de incognitas: '))

incognitas = []

for i in range(n):
    incognitas.append(input('digite quais são as incognitas:'))

matriz = np.zeros((n,n+1))

x = np.zeros(n)

# Reading augmented matrix coefficients
print('digite a matrix de coeficientes:')
for i in range(n):
    for j in range(n+1):
        matriz[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

print("Gauss Jordan com a biblioteca Numpy")
x = gaussJordan(matriz, n)
for i in range(n):
    print(incognitas[i]+' = '+ str(x[i]))

print("\nGauss Jordan com a biblioteca Scipy:")
y = gaus_scipy(matriz, n)
for i in range(n):
    print(incognitas[i]+' = '+ str(y[i][0]))
