<?php
// Operadores aritméticos

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

$y = $numero3 & $numero4;  // Conjunción a nivel de bits
$o = $numero3 | $numero4;    // Disyunción a nivel de bits
$oexcl = $numero3 ^ $numero4;  // Disyunción exclusiva a nivel de bits
$no = ~$numero3;  // Negación a nivel de bits
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

/*
BLOQUE COMENTARIO
:D
*/
?>