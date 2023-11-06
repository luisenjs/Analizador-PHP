<?php
class MiClase {
  public $publico = 42;
  private $privado = 'secreto';

  function __construct() {
      echo "Constructor de la clase.";
  }

  public function funcionPublica() {
      echo "Método público.";
  }

  private function funcionPrivada() {
      echo "Método privado.";
  }
}

$stack = new SplStack();

for ($i = 1; $i <= 5; $i++) {
  if ($i % 2 == 0) {
      $stack->push($i);
  } else {
      //$stack->pop();
  }
}

echo "Elemento superior de la pila: " . $stack->top();

$clase = new MiClase();
$clase->funcionPublica();
echo $clase->publico;

if (is_callable([$clase, 'funcionPrivada'])) {
  echo "La función privada es llamable.";
} else {
  echo "La función privada no es llamable.";
}

$array = [1, 2, 3];
foreach ($array as $valor) {
  echo "Valor: $valor";
}

$variable = "Esta es una variable.";
echo $variable;

$constante = 100;
echo "Constante: $constante";

$or = true;
$and = false;
if ($or || $and) {
  echo "Condición OR verdadera.";
}

if (isset($variable) && $constante == 100) {
  echo "Ambas condiciones son verdaderas.";
}

function myFunction($param) {
  echo "Esta es una función. Param: $param";
}

myFunction("Hola");

echo "Fin del programa.";
?> 