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