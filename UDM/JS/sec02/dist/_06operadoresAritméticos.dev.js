"use strict";

/*
ORDEM DE IMPORTANCIA 
() >>> ** >>> * / % >>> + - 

+  adição/ concatenação
-  subtração
/  divisão
*  multiplicação
** potenciação
% resto da divisão

*/

/* exemplo
const num = 10;
const num2 = 3;

console.log(num + num2);
console.log(num - num2);
console.log(num / num2);
console.log(num * num2);
console.log(num ** num2);
console.log(num % num2);
*/

/*
let contador =   1;
contador++;
contador++;
contador++;
contador++;
console.log(contador);

Operador de atribuição 
+=
-=
*=
/=
*/
var contador = 2;
contador += 2;
contador = Math.pow(contador, 2);
contador /= 2;
contador -= 2;
console.log(contador);