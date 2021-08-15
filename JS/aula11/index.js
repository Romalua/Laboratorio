/*
window.alert ('Mensagem');
window.confirm('Deseja realmente apagar ? ');
window.prompt("Digite seu nome: ");
var nome = window.prompt('Seu nome de novo: ');
window.alert(`Seu nome é ${nome}`);
*/

let num1 = prompt('Digite o primeiro valor: ');
let num2 = prompt('Digite o segundo valor: ');
let num3 = prompt('Digite o terceiro valor: ');

num1 = Number(num1);
num2 = Number(num2);
num3 = Number(num3);

resultado = num1 + num2 + num3
window.alert(`Resultado é ${resultado}`);