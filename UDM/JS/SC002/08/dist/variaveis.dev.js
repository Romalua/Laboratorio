"use strict";

var varA = 'A'; //B

var varB = 'B'; //C

var varC = 'C'; //A

var varATemp = varA;
varA = varB;
varB = varC;
varC = varATemp;
console.log(varA, varB, varC);