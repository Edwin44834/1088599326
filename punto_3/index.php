<?php
$a =inset($_GET['a']) ? (float) $_GET['a']:0;
$b =inset($_GET['b']) ? (float) $_GET['b']:0;

$resultado = $a + $b;
echo "la suma de $a + $b es: $resultado";
