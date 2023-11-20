import ply.lex as lex

#Stefany Farias
#Palabras reservadas
reservadas={
    "and":"AND",
    "as" : "AS",
    "array" : "ARRAY",
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
    "fgets" : "FGETS",
    "readline" : "READLINE",
    "fscanf" : "FSCANF",
    "STDIN" : "STDIN",
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

#Stefany Farias
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Caracter inválido '%s'" % t.value[0])
  t.lexer.skip(1)

def t_FLOTANTE(t):
  r'(-?\d*\.\d+)|^0.0$'
  t.value = float(t.value)
  return t

def t_ENTERO(t):
  r'(-?[1-9]\d*)|0'
  t.value = int(t.value)
  return t

def t_BOOLEANO(t):
  r'(true|True|TRUE|false|False|FALSE)'
  t.type = reservadas.get(t.value, "BOOLEANO")
  return t

def t_IDENTIFICADOR(t):
  r'[a-zA-Z0-9_]?[a-zA-Z_0-9]+'
  t.type = reservadas.get(t.value.lower(),"IDENTIFICADOR")
  return t

t_ignore = " \t"

lexer = lex.lex()

code4 = '''
// Operadores aritméticos

echo "HOLA\"dsd\"";
$numero1 = 10;
$numero2 = 5;

$suma = $numero1 + $numero2;  // Suma
$resta = $numero1 - $numero2;  // Resta
$multiplicacion = $numero1 * $numero2;  // Multiplicación
$division = $numero1 / $numero2;  // División
$modulo = $numero1 % $numero2;  // Módulo
$potencia = $numero1 ** $numero2;  // Potencia

echo "Suma: $suma\n";
echo "Resta: $resta\n";
echo "Multiplicación: $multiplicacion\n";
echo "División: $division\n";
echo "Módulo: $modulo\n";
echo "Potencia: $potencia\n";

$numero3 = 7;
$numero4 = 3;

$and = $numero3 & $numero4;  // Conjunción a nivel de bits
$or = $numero3 | $numero4;    // Disyunción a nivel de bits
$xor = $numero3 ^ $numero4;  // Disyunción exclusiva a nivel de bits
$not = ~$numero3;  // Negación a nivel de bits
$desplazamiento_izq = $numero3 << 1;  // Desplazamiento de bits a la izquierda
$desplazamiento_der = $numero3 >> 1;  // Desplazamiento de bits a la derecha

echo "Conjunción a nivel de bits: $and\n";
echo "Disyunción a nivel de bits: $or\n";
echo "Disyunción exclusiva a nivel de bits: $xor\n";
echo "Negación a nivel de bits: $not\n";
echo "Desplazamiento de bits a la izquierda: $desplazamiento_izq\n";
echo "Desplazamiento de bits a la derecha: $desplazamiento_der\n";

$valor1 = 10;
$valor2 = 20;

$igualdad = $valor1 == $valor2;  // Igualdad
$identidad = $valor1 === $valor2;  // Identidad
$diferente = $valor1 != $valor2;  // Diferente
$no_identidad = $valor1 !== $valor2;  // No identidad
$menor = $valor1 < $valor2;  // Menor que
$mayor = $valor1 > $valor2;  // Mayor que
$menor_igual = $valor1 <= $valor2;  // Menor o igual que
$mayor_igual = $valor1 >= $valor2;  // Mayor o igual que

echo "Igualdad: " . ($igualdad ? 'true' : 'false') . "\n";
echo "Identidad: " . ($identidad ? 'true' : 'false') . "\n";
echo "Diferente: " . ($diferente ? 'true' : 'false') . "\n";
echo "No identidad: " . ($no_identidad ? 'true' : 'false') . "\n";
echo "Menor que: " . ($menor ? 'true' : 'false') . "\n";
echo "Mayor que: " . ($mayor ? 'true' : 'false') . "\n";
echo "Menor o igual que: " . ($menor_igual ? 'true' : 'false') . "\n";
echo "Mayor o igual que: " . ($mayor_igual ? 'true' : 'false') . "\n";

// Operadores de incremento y decremento
$numero5 = 5;

$numero5++;  // Incremento
$numero5--;  // Decremento

echo "Incremento: $numero5\n";
echo "Decremento: $numero5\n";

$valor3 = true;
$valor4 = false;

$condicion_or = $valor3 || $valor4;  // OR lógico
$condicion_and = $valor3 && $valor4;  // AND lógico

echo "OR lógico: " . ($condicion_or ? 'true' : 'false') . "\n";
echo "AND lógico: " . ($condicion_and ? 'true' : 'false') . "\n";

/*
BLOQUE COMENTARIO
:D
*/

lexer.input(code4)

for token in lexer:
  print(token)
'''