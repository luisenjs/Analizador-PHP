import ply.yacc as yacc
from lexico import tokens

def p_variaslineas(p):
  ''' variaslineas : programa
                    | programa variaslineas'''
                
                
def p_programa(p):
  '''programa : clase
              | instrucciones
  '''
    
def p_clase(p):
  "clase : CLASS IDENTIFICADOR LLAVE_ABRE instrucciones LLAVE_CIERRA"

def p_instrucciones(p):
  '''instrucciones : asignacion
            | salida
            | ingreso
            | estructuras_datos
            | estructuras_control
            | funcion
            | COMENTARIO_LINEA
            | COMENTARIO_BLOQUE
            | operaciones FIN_LINEA
            | declaracion_s FIN_LINEA
            | BREAK FIN_LINEA
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

#Luis Jara
#Privacidad de variables
def p_variable_tipo(p):
  '''variable_tipo : CONST
                  | PRIVATE
                  | PUBLIC
                  | PROTECTED
                  | STATIC
                  | VAR
  '''

# Stefany Farias
# 3.1 declaración de variables y funciones
def p_decl_variable(p):
  '''decl_variable : SIGNO_DOLAR IDENTIFICADOR
                    | variable_tipo SIGNO_DOLAR IDENTIFICADOR'''

def p_asignacion(p):
  '''asignacion : decl_variable IGUAL valor FIN_LINEA
                | decl_variable IGUAL estructuras_datos
                | decl_variable IGUAL poppila FIN_LINEA
                
  '''

def p_valor(p):
  '''valor : datos
            | pila
            | NULO
            | decl_variable
            | opAritVar
            
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
  '''funcion : FUNCTION IDENTIFICADOR PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA
  '''

def p_funcion_parametros(p):
  '''funcion : FUNCTION IDENTIFICADOR PARENTESIS_ABRE parametros PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA'''

def p_funcionenuso(p):
  '''funcionuso : IDENTIFICADOR PARENTESIS_ABRE parametros PARENTESIS_CIERRA
  '''

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

def p_pop(p):
  '''poppila : decl_variable LAMBDA POP PARENTESIS_ABRE PARENTESIS_CIERRA
  '''

def p_push(p):
  '''pushpila : decl_variable LAMBDA PUSH PARENTESIS_ABRE valor PARENTESIS_CIERRA
            | decl_variable LAMBDA PUSH PARENTESIS_ABRE operaciones_arit PARENTESIS_CIERRA
  '''

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

#Luis Jara
#Operadores con bits
def p_operad_bits(p):
  '''operand_bits : CONJUNCION
                  | DISYUNCION
                  | DISYUNCION_EXC
                  | DESPLAZAR_BITS_IZQ
                  | DESPLAZAR_BITS_DER
  '''

#Luis Jara
#Operaciones aritméticas, lógicas y con bits
def p_operaciones_arit(p):
  '''operaciones_arit : salidas_posibles operad_arit salidas_posibles
                | salidas_posibles operad_arit operaciones_arit
                
  '''

def p_operaciones_bits(p):
  '''operaciones_bits : salidas_posibles operand_bits salidas_posibles
                  | NEGACION salidas_posibles
  '''

def p_operaciones_logica(p):
  ''' operaciones_logicas : ENTERO operad_logico ENTERO
                | FLOTANTE operad_logico FLOTANTE
                | BOOLEANO
                | decl_variable operad_logico decl_variable
                | decl_variable operad_logico ENTERO
                | decl_variable operad_logico FLOTANTE
  '''

def p_operaciones(p):
  '''operaciones : operaciones_logicas
                  | operaciones_arit
                  | operaciones_bits
                  | pushpila
                  | poppila
  '''
  
def p_paraCalculos(p):
  '''paraCalculos : ENTERO
                  | FLOTANTE
                  | decl_variable'''

def p_combinarOp(p):
  '''combinarOp : operad_arit paraCalculos
                | operad_arit paraCalculos combinarOp'''

def p_opAritmeticaEnVar(p):
  "opAritVar : paraCalculos combinarOp"
  
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
  ''' bloque : instrucciones
              | retorno
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
  ''' retorno : RETURN salidas_posibles FIN_LINEA
              | RETURN operaciones FIN_LINEA
  '''

# Luis Jara
# Estructura de control foreach
def p_foreach(p):
  '''foreach : FOREACH PARENTESIS_ABRE decl_variable AS decl_variable PARENTESIS_CIERRA LLAVE_ABRE sentenciasAnidadas LLAVE_CIERRA
              | FOREACH PARENTESIS_ABRE decl_variable AS decl_variable IGUAL MAYOR decl_variable PARENTESIS_CIERRA LLAVE_ABRE sentenciasAnidadas LLAVE_CIERRA
  '''

#Luis Jara
#Estructura de control while
def p_while(p):
  "while : WHILE PARENTESIS_ABRE decl_variable operad_logico valor PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA"

#Luis Jara
#Estructura de control if-else
def p_if_else_corto(p):
  " if_else : if_else_inicio if_else_fin"

#if-elseif-else
def p_if_else_extendido(p):
  " if_else : if_else_inicio if_else_cuerpo if_else_fin"

#Bloque IF
def p_if_else_inicio(p):
  "if_else_inicio : IF PARENTESIS_ABRE operaciones_logicas PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA"

#Bloque ELSEIF
def p_if_else_cuerpo(p):
  ''' if_else_cuerpo : ELSEIF PARENTESIS_ABRE operaciones_logicas PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA
                    |  ELSEIF PARENTESIS_ABRE operaciones_logicas PARENTESIS_CIERRA LLAVE_ABRE bloque LLAVE_CIERRA if_else_cuerpo
  '''

#Bloque ELSE
def p_if_else_fin(p):
  "if_else_fin : ELSE LLAVE_ABRE bloque LLAVE_CIERRA"


'''def p_error(p):
  if p:
    print("Error sintáctico, no se esperaba '%s'" % p.value)
  else:
    print("Error sintáctico, sentencia incompleta")'''

parser = yacc.yacc()

'''
while True:
   try:
       s = input('code > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result:
    print(result)
    
    def sintactico(codigo):
  parser.parse(codigo)
  
    '''

errores_sintaxis = []  
def p_error(p):
    if p:
        print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        errores_sintaxis.append("Error de sintaxis en token {}, en la linea {}, Col: {}".format(p.type, p.lineno, p.lexpos))
        parser.errok()
        # logs_file.write(today.strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +"Error de sintaxis - Token: "+ str(p.type) +", Línea: "+ str(p.lineno) +", Col: "+ str(p.lexpos) +"\n")
    else:
        errores_sintaxis.append("Error de sintaxis Fin de Linea")
        print("Error de sintaxis Fin de Linea")
        # logs_file.write(today.strftime("%m/%d/%Y, %H:%M:%S")+ "\t" +"Error de sintaxis Fin de Linea"+"\n")

  
def obtener_analizador_sintactico():
    return yacc.yacc()


def validaRegla(s):
    result1 = parser.parse(s)
    print(result1)
    return result1
