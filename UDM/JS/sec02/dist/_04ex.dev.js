"use strict";

var nome = prompt("Seu nome? ");
var sobrenome = "Faustino";
var idade = 24;
var peso = 63;
var altura = 1.80;
var imc;
var anoNascimento;
imc = peso / (altura * altura);
anoNascimento = 2022 - idade;
console.log("".concat(nome, " ").concat(sobrenome, " tem ").concat(idade, " anos e pesa ").concat(peso, "Kg"));
console.log("tem ".concat(altura, " de altura e seu IMC \xE9 de ").concat(imc));
console.log("".concat(nome, " nasceu em ").concat(anoNascimento));