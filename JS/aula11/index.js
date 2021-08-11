/*
window.alert ('Mensagem');
window.confirm('Deseja realmente apagar ? ');
window.prompt("Digite seu nome: ");
var nome = window.prompt('Seu nome de novo: ');
window.alert(`Seu nome é ${nome}`);
*/

const num1 = prompt('Digite o primeiro valor: ');
const num2 = prompt('Digite o segundo valor: ');
const num3 = prompt('Digite o terceiro valor: ');
num1 = Number(num1);
num2 = Number(num2);
num3 = Number(num3);

window.alert(`Resultado é ${num1 + num2 + num3}`);