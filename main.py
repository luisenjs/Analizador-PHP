import ply.yacc as yacc
from lexico import tokens

def p_instrucciones(p):
  '''instrucciones : asignacion
            | valor
            | salida
            | ingreso
            | estructuras_datos
            | funcion
  '''

# Stefany Farias
# 1 impresión de valor(es) 
def p_salidas_posibles(p):
  '''salidas_posibles : datos
                | decl_variable
  '''

def p_salida_forma1(p):
  '''salida : ECHO salidas_posibles FIN_LINEA'''

def p_salida_forma2(p):
  '''salida : PRINT PARENTESIS_ABRE salidas_posibles PARENTESIS_CIERRA FIN_LINEA'''

def p_salida_forma3(p):
  '''salida : PRINT salidas_posibles FIN_LINEA'''
  
# Luis Jara
# 2 Ingreso de datos
def p_ingreso_forma1(p):
  '''ingreso : READLINE PARENTESIS_ABRE CADENA PARENTESIS_CIERRA FIN_LINEA'''

def p_ingreso_forma2(p):
  '''ingreso : FGETS PARENTESIS_ABRE STDIN PARENTESIS_CIERRA FIN_LINEA'''

def p_ingreso_forma3(p):
  '''ingreso : FSCANF PARENTESIS_ABRE STDIN COMA CADENA COMA SIGNO_DOLAR IDENTIFICADOR PARENTESIS_CIERRA FIN_LINEA'''

# Stefany Farias
# 3.1 declaración de variables y funciones
def p_decl_variable(p):
  "decl_variable : SIGNO_DOLAR IDENTIFICADOR"

def p_asignacion(p):
  '''asignacion : decl_variable IGUAL valor FIN_LINEA'''

def p_valor(p):
  '''valor : datos

  '''

def p_datos(p):
  '''datos : ENTERO
          | FLOTANTE
          | CADENA 
          | BOOLEANO
  '''

# Stefany Farias
# 3.2 declaración de funciones
def p_funcion(p):
  '''funcion : FUNCTION IDENTIFICADOR PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA
  '''

def p_funcion_parametros(p):
  '''funcion : FUNCTION IDENTIFICADOR PARENTESIS_ABRE parametros PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA'''

def p_parametros(p):
  '''parametros : SIGNO_DOLAR IDENTIFICADOR
                  | SIGNO_DOLAR IDENTIFICADOR COMA parametros
  '''

# Luis Jara
# 4 estructuras de datos
def p_estructuras_datos(p):
  ''' estructuras_datos : pila FIN_LINEA
                        | arreglo FIN_LINEA
  '''
def p_pila(p):
  '''pila :  NEW STACK PARENTESIS_ABRE PARENTESIS_CIERRA'''

def p_arreglo_vacio(p):
  '''arreglo : ARRAY PARENTESIS_ABRE PARENTESIS_CIERRA
              | CORCHETE_ABRE CORCHETE_CIERRA
  '''

def p_arreglo_indexado(p):
  '''arreglo : ARRAY PARENTESIS_ABRE elementos PARENTESIS_CIERRA
              | CORCHETE_ABRE elementos CORCHETE_CIERRA
  '''

def p_arreglo_asociativo(p):
  '''arreglo : ARRAY PARENTESIS_ABRE asociacion PARENTESIS_CIERRA
              | CORCHETE_ABRE asociacion CORCHETE_CIERRA
  '''

def p_asociacion(p):
  '''asociacion : datos IGUAL MAYOR datos
                  | datos IGUAL MAYOR datos COMA asociacion
  '''
def p_elementos(p):
    '''elementos : datos
                  | datos COMA elementos
    '''

#Stefany Farias
def p_operad_aritmeticas(p):
  '''operad_arit : SUMA
                | RESTA
                | MULTIPLICACION
                | DIVISION
                | POTENCIA
                | MODULO
  '''

def p_operad_logicos(p):
  '''operad_logico : IGUALDAD
                | IDENTIDAD
                | DIFERENTE
                | NO_IDENTIDAD
                | MAYOR
                | MAYOR_IGUAL
                | MENOR
                | MENOR_IGUAL
                | AND
                | OR
                | XOR
  '''
  
#Stefany Farias
#Condicionales simples y con conectores
def p_estructuras_control(p):
  ''' estructuras_control : for
                          | foreach
                          | if_else
                          | while
                          
  '''

#Bloques de código permitidos dentro de funciones o bucles
def p_bloque(p):
  ''' bloque : asignacion
              | salida
              | retorno
              | estructuras_control
  '''

#Stefany Farias
#Estructura de control for
def p_for(p):
   '''for : FOR PARENTESIS_ABRE asignacion declaracionp declaracion_s PARENTESIS_CIERRA LLAVE_ABRE sentenciasAnidadas LLAVE_CIERRA'''

def p_sentenciasAnidadas(p):
  '''sentenciasAnidadas : instrucciones 
            | instrucciones sentenciasAnidadas
  '''

def p_declaracionM(p):
   '''declaracionp :  decl_variable valorc'''

def p_valorC(p):
  ''' valorc : menor
              | mayor'''

def p_menor(p):
  '''menor : MENOR_IGUAL ENTERO FIN_LINEA'''

def p_mayor(p):
  '''mayor : MAYOR_IGUAL ENTERO FIN_LINEA'''

def p_declaracionsimple(p):
   '''declaracion_s : decl_variable crecimiento
                    | crecimiento decl_variable
   '''

def p_crecimiento(p):
  '''crecimiento : INCREMENTO 
                | DECREMENTO'''

def p_retorno(p):
  ''' retorno : RETURN salidas_posibles FIN_LINEA'''




def p_error(p):
  if p:
    print("Error sintáctico, no se esperaba '%s'" % p.value)
  else:
    print("Error sintáctico, sentencia incompleta")

parser = yacc.yacc()

while True:
   try:
       s = input('code > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result:
    print(result)