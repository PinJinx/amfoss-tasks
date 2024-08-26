const fs = require('fs');
const path = require('path');

// Get the directory of the current script
const scriptDir = path.dirname('__filename');

// Read the content of 'input.txt'
const inputFilePath = path.join(scriptDir, 'input.txt');
const content = fs.readFileSync(inputFilePath, 'utf8');

// Write the content to 'output.txt'
const outputFilePath = path.join(scriptDir, 'output.txt');
fs.writeFileSync(outputFilePath, content);
