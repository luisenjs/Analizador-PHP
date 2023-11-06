<?php
function evaluarExpresionPosfija($expresion) {
$pila = new SplStack();
$tokens = explode(' ', $expresion);

foreach ($tokens as $token) {
    if (is_numeric($token)) {
        $pila->push($token);
    } else {
        $operando2 = $pila->pop();
        $operando1 = $pila->pop();

        switch ($token) {
            case '+':
                $pila->push($operando1 + $operando2);
                break;
            case '-':
                $pila->push($operando1 - $operando2);
                break;
            case '*':
                $pila->push($operando1 * $operando2);
                break;
            case '/':
                $pila->push($operando1 / $operando2);
                break;
        }
    }
}

return $pila->pop();
}

$expresionPosfija = "3 4 + 5 * 2 /";
$resultado = evaluarExpresionPosfija($expresionPosfija);

echo "Resultado de la expresión posfija: $resultado";
?> 