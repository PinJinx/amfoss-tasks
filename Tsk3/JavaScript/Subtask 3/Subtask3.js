const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('Enter a val: ', (input) => {
    let n = parseInt(input);
    if (n % 2 === 0) {
        n -= 1;
    }
    let k = (n + 1) - 2;
    for (let i = 1; i <= n; i += 2) {
        k -= 1;
        console.log(' '.repeat(k) + '*'.repeat(i));
    }
    for (let i = n - 2; i > 0; i -= 2) {
        k += 1;
        console.log(' '.repeat(k) + '*'.repeat(i));
    }
    rl.close();
});
