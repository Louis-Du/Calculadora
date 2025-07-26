print("--Bienvenido a la Calculadora--")
def proceso_arimetico(entrada):
  try:
    entrada = entrada.replace(' ','') # Remplaza ' ' por ''.
    resultado = 0

    if '+' in entrada:
      sumar = entrada.split('+')
      numero1 = float(sumar[0])
      numero2 = float(sumar[1])
      resultado = numero1 + numero2

    elif '-' in entrada:
      restar = entrada.split('-')
      numero1 = float(restar[0])
      numero2 = float(restar[1])
      resultado = numero1 - numero2

    elif '*' in entrada:
      multiplicar = entrada.split('*')
      numero1 = float(multiplicar[0])
      numero2 = float(multiplicar[1])
      resultado = numero1 * numero2

    elif '/' in entrada:
      dividir = entrada.split('/')
      numero1 = float(dividir[0])
      numero2 = float(dividir[1])
      resultado = numero1 / numero2

    elif '^' in entrada:
      elevar = entrada.split('^')
      numero1 = float(elevar[0])
      numero2 = float(elevar[1])
      resultado = numero1 ** numero2
    print(resultado)
  except ZeroDivisionError:
    print("ERROR: No es posible dividir entre 0, vuelve a intentarlo en otro universo")
  except ValueError:
    print("ERROR: Hay un error... o varios")
      
while True:
  problema = input("¿Qué cálculo haremos hoy? \n ")
  if problema == '':
    break
  proceso_arimetico(problema)

