const fs = require('fs');
const path = require('path');
const scriptDir = path.dirname(__filename);
const inputFilePath = path.join(scriptDir, 'input.txt');
const outputFilePath = path.join(scriptDir, 'output.txt');
const input = fs.readFileSync(inputFilePath, 'utf8');
let n = parseInt(input.trim());
if (n % 2 === 0) {
    n -= 1;
}

let k = (n + 1) - 2;
let output = '';
for (let i = 1; i <= n; i += 2) {
    k -= 1;
    output += ' '.repeat(k) + '*'.repeat(i) + '\n';
}
for (let i = n - 2; i > 0; i -= 2) {
    k += 1;
    output += ' '.repeat(k) + '*'.repeat(i) + '\n';
}
fs.writeFileSync(outputFilePath, output);
