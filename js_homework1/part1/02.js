/*

02. Создайте три переменные с любыми числовыми значениями. Используя условный оператор и не используя логические, найдите минимальное число и отобразите на экране имя переменной и ее значение.

*/

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
readline.question(`Please input a: `, (a) => {
    readline.question(`Please input b: `, (b) => {
        readline.question(`Please input c: `, (c) => {
            let result = [a, "a"]
            console.log(result)
            if (b < result[0]) {
                result[0] = b
                result[1] = 'b'
                console.log(result)
            }
            if (c < result[0]) {
                result[0] = c
                result[1] = 'c'
                console.log(result)
            } 
            console.log("\nVariable name: " + result[1], "\nValue: " + result[0])
        readline.close()
        })
    })
})

