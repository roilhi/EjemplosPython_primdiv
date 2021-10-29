def pascals_triangle(n):
  """ Esta función devuelve una lista de listas con los coeficientes 
  del triángulo de Pascal o coeficientes binomiales 
  El argumento de entrada es el número n de niveles o líneas 
  Ejemplo: pascals_triangle(3)=[[1],[1,1],[1,2,1]] 
  Llama a otra función que crea una lista con los coeficientes 
  binomiales del triángulo"""
  # En esta lista se irán almacenando todos los coeficientes generados (almacena las líneas)
  coefs =[]
  for w in range(1,n+1):
    # Llama varias veces a la función que crea una lista con los coeficientes binomiales en el intervalo [1,n]
    coefs.append(pascal_coefs(w))
  return coefs 
def pascal_coefs(r):
  """ Función que da como salida una lista con los coeficientes binomiales
      del último nivel del triángulo de Pascal. Ejemplo: pascal_coefs(3) = [1,2,1] """
  # En este ciclo se va creando cada línea.
  for k in range(1,r+1):
    # En esta lista se irán guardando los valores de cada línea del triángulo
    line = []
    C = 1 # El primer coeficiente de cada línea siempre vale 1
    for m in range(1,k+1):
      line.append(C) # Guarda en la línea el valor de cada coeficiente
      C=int(C*(k-m)/m) # Aquí se calcula el valor de cada coeficiente
  return line #Se devuelve la lista de listas con todos los coeficientes creados