"use strict";

var varA = 'A'; //B

var varB = 'B'; //C

var varC = 'C'; //A

/*
const varATemp = varA;
varA = varB;
varB = varC;
varC = varATemp;*/

var _ref = [varB, varC, varA];
varA = _ref[0];
varB = _ref[1];
varC = _ref[2];
console.log(varA, varB, varC);