"use strict";

var nome = 'Lucas Barreto';
var sobrenome = "Faustino";
var idade = 24;
var peso = 63;
var altura = 1.80;
var imc;
var anoNascimento;
imc = peso / (altura * altura);
anoNascimento = 2022 - idade;
console.log(nome, sobrenome, 'tem', idade, 'anos e pesa', peso, 'Kg');
console.log('tem', altura, 'de altura e seu IMC é de', imc);
console.log(nome, 'nasceu em', anoNascimento);