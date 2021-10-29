from my_functions import division 
def is_prime_recursion(x, i = 2):
  """En esta función se devuelve un valor lógico True/False según
  si un número x ingresado es primo o no.
  Ejemplo: is_prime_recursion(13) = True, ya que el 13 es primo
  Aunque el segundo argumento de entrada aparezca constante, se irá
  incrementando para completar la recursividad """
  # Se comienza la descomposición desde el número 2, ya que es el primer primo
  # de la tabla
  if x <= 2:
    # La función regresa true si el número de entrada es 2, ya que éste es primo
    return True if x == 2 else False
  # Si algún residuo de las divisiones sucesivas realizadas es igual a cero,
  # el número x no es primo (es divisible entre i)
  if division(x,i)[1]==0:
      return False
  # Si el cuadrado de i es mayor a x entonces no es divisible, por lo tanto regresará TRUE
  if i * i > x:
      return True
  # Finalmente se llama de manera recursiva a la función, incrementa el valor del
  # divisor en 1 para seguir probando si x es divisible entre 3,4,5,.. etc
  return is_prime_recursion(x, i + 1)