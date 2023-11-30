<?php
// Operadores aritméticos

echo "HOLA\"dsd\"";
$numero1 = 10;
$numero2 = 5;

$suma = $numero1 + $numero2;
$resta = $numero1 - $numero2;
$multiplicacion = $numero1 * $numero2;
$division = $numero1 / $numero2;
$modulo = $numero1 % $numero2;
$potencia = $numero1 ** $numero2;

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
?>