
const nome = prompt("Seu nome? ");
const sobrenome = "Faustino";
const idade = 24;
const peso = 63;
const altura = 1.80;
let imc;
let anoNascimento;

imc = peso / (altura*altura);
anoNascimento = 2022 - idade;

console.log(`${nome} ${sobrenome} tem ${idade} anos e pesa ${peso}Kg`)
console.log(`tem ${altura} de altura e seu IMC é de ${imc}`);
console.log(`${nome} nasceu em ${anoNascimento}`);
