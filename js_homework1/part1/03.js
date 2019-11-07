/*
03. В переменную age запишите возраст человека. Если значение больше или равно 20 и меньше 27, через console.warn выводится “Выслать повестку”.
*/

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  })
  
readline.question(`Сколько Вам лет? `, (age) => {
  if (age >= 20 && age < 27) {
    console.warn("\nВыслать повестку")
  } else {
    console.log("\nСвободен")
  }
  readline.close()
})