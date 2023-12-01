<?php
class MiClase {
  public $publico = 42;
  private $privado = "secreto";

  function construct() {
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
      $stack->pop();
  }
}

$arreglo = [1, 2, 3];
foreach ($arreglo as $valor) {
  echo "Valor: $valor";
}

$variable = "Esta es una variable.";
echo $variable;

$constante = 100;
echo "Constante: $constante";

$o = true;
$y = false;
if ($o || $y) {
  echo "Condición OR verdadera.";
}else{
  echo "Condición OP falsa.";
}

if (isset($variable) && $constante == 100) {
  echo "Ambas condiciones son verdaderas.";
}else{
  echo "Caso contrario.";
}

function myFunction($param) {
  echo "Esta es una función. Param: $param";
}

myFunction("Hola");

echo "Fin del programa.";
?> 