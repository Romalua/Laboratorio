"use strict";

/*
alert("Mensagem");
confirm("Confirmação");
prompt("Nome: ")
*/
var num1 = prompt("Numero: ");
var num2 = prompt("Outro Numero: ");
num1 = Number(num1);
num2 = Number(num2);
var resultado = num1 * num2;
alert("O resultado  ".concat(resultado));
alert("Multiplicando ".concat(num1, " por ").concat(num2, " resulta em ").concat(resultado));