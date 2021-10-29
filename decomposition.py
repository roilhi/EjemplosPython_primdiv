from my_functions import primes
from my_functions import division
def decomposition(n):
  """ Esta función devuelve una lista con los valores de la descomposicion
  de un número en factores primos. Esto es, la multiplicación de los elementos 
  de esa lista nos da el número n.
  Ejemplo descomposicion(40) = [2,2,2,5] 
  Y en efecto: 2*2*2*5= 40"""
  # Variable que guarda el cociente de la división sucesiva
  qp = n
  # Inicializando el cociente que deberá llegar a 1 para finalizar el algoritmo
  q = qp
  # Variable que recorre la lista de primos de 2 a n
  k = 0
  # Variable que guarda el residuo de la división
  r = 0
  # Inicializando la lista donde se guardarán los factores primos de la descomposición
  prime_factors=[]
  # Inicializa condición para el ciclo while
  condicion = True
  # Mientras la condición sea verdadera, el ciclo while seguirá calculando
  while condicion:
    # La condición cambiará su estado a falso cuando el cociente de la división sea 1
    # y además el residuo sea cero
    if r==0 and q ==1:
      # La condición cambia de estado a falso y finaliza el cálculo
      condicion = False
    else:
      # Calcula una lista con los primos [2, 3, 5, ... n]
      # luego, toma el k-esimo elemento para realizar la división
      prime_fac = primes(n)[k]
      # Obtiene el cociente y residuo de dividir consecutivamente n, 
      # es decir, encuentra si n es divisible entre el factor primo k-ésimo
      q,r = division(qp, prime_fac)
      if r==0:
        # Cuando el factor primo k-ésimo es divisible, el residuo es cero y se
        # guarda en la lista
        prime_factors.append(prime_fac)
        # Cambia el estado del divisor al cociente encontrado anteriormente
        qp = q
      else:
        # Cuando no es divisible el factor primo se recorre y divide por 
        # el siguiente de la lista. Se calculan cociente y residuo
        k=k+1
        prime_fac = primes(n)[k]
        q,r = division(qp, prime_fac)
        # Se guarda el último factor primo obtenido en la lista
        if q==1 and r==0:
          prime_factors.append(prime_fac)
  # Finalmente se devuelve como salida la lista de factores primos
  return prime_factors
