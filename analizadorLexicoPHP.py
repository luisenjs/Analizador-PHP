import ply.lex as lex

#Stefany Farias
#Palabras reservadas
reservadas={
    "and":"AND",
    "array" : "ARRAY",
    "break": "BREAK",
    "callable": "CALLABLE",
    "class": "CLASS",
    "const": "CONST",
    "elseif": "ELSEIF",
    "else": "ELSE",
    "for": "FOR",
    "foreach": "FOREACH",
    "function": "FUNCTION",
    "if": "IF",
    "new": "NEW",
    "or": "OR",
    "print" : "PRINT",
    "private": "PRIVATE",
    "protected": "PROTECTED",
    "public": "PUBLIC",
    "return": "RETURN",
    "static": "STATIC",
    "var": "VAR",
    "while": "WHILE",
    "xor": "XOR",
    "SplStack" : "STACK",
    "explode" : "EXPLODE",
    "push" : "PUSH",
    "pop" : "POP",
    "echo": "ECHO",
}

#Luis Jara
#Tokens y expresiones
tokens = (
  "SIGNO_DOLAR",
  "ENTERO",
  "FLOTANTE",
  "CADENA",
  "BOOLEANO",
  "IDENTIFICADOR",
  "NULO",
  "IGUAL",
  "SUMA",
  "RESTA",
  "MULTIPLICACION",
  "DIVISION",
  "MODULO",
  "POTENCIA",
  "CONJUNCION",
  "DISYUNCION",
  "DISYUNCION_EXC",
  "NEGACION",
  "DESPLAZAR_BITS_IZQ",
  "DESPLAZAR_BITS_DER",
  "IGUALDAD",
  "IDENTIDAD",
  "DIFERENTE",
  "NO_IDENTIDAD",
  "MENOR",
  "MAYOR",
  "MENOR_IGUAL",
  "MAYOR_IGUAL",
  "INCREMENTO",
  "DECREMENTO",
  "COMENTARIO_LINEA",
  "COMENTARIO_BLOQUE",
  "PARENTESIS_ABRE",
  "PARENTESIS_CIERRA",
  "LLAVE_ABRE",
  "LLAVE_CIERRA",
  "CORCHETE_ABRE",
  "CORCHETE_CIERRA",
  "FIN_LINEA",
  "PUNTO",
  "COMA",
  "DOS_PUNTOS",
  "INTERROGANTE"
)+tuple(reservadas.values())

t_SIGNO_DOLAR = r'\$'
t_CADENA = r'".*?"|".*?\n.*?"|\'.*?\'|\'.*?\n.*?\''
t_NULO = r'null'
t_IGUAL = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_POTENCIA = r'\*\*'
t_CONJUNCION = r'&'
t_DISYUNCION = r'\|'
t_DISYUNCION_EXC = r'\^'
t_NEGACION = r'~'
t_DESPLAZAR_BITS_IZQ = r'<<'
t_DESPLAZAR_BITS_DER = r'>>'
t_IGUALDAD = r'=='
t_IDENTIDAD = r'==='
t_DIFERENTE = r'!='
t_NO_IDENTIDAD = r'!=='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'--'
t_COMENTARIO_LINEA = r'//.*'
t_COMENTARIO_BLOQUE = r'/\*[\s\S]*?\*/'
t_PARENTESIS_ABRE = r'\('
t_PARENTESIS_CIERRA = r'\)'
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_CORCHETE_ABRE = r'\['
t_CORCHETE_CIERRA = r'\]'
t_FIN_LINEA = r';'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOS_PUNTOS = r'\:'
t_INTERROGANTE = r'\?'