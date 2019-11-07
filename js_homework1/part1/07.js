/*
07. Напишите программу, которая в консоли выводит текстовое поздравление. Программа поздравляет того, чье имя определяется в переменной username:
Happy birthday dear {{username}}
Например Happy birthday dear Maxim
*/

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
readline.question(`What's your name? `, (name) => {
    console.log("\nHappy Birthday, dear " + name + "!")
    readline.close()
})