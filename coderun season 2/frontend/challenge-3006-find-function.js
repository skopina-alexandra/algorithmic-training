const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', input => {
    let n = parseInt(input.trim())
    console.log(phi(n))
    rl.close()
})

const phi = n => {
    let result = n;
    for (let i = 2; i * i <= n; i++){
        if (n % i == 0){
            while (n % i == 0){
                n /= i;
            }
            result -= result / i
        }
    }
    if (n > 1){
        result -= result / n
    }

    return parseInt(result)
}