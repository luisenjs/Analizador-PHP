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

#Stefany Farias
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
  
  

#Stefany Farias
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

#Stefany Farias
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