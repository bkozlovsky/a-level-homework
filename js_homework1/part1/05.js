/*
05. Сформируйте строку вида ".#.#.#.#.#." с помощью цикла for.
*/

let chars = ".#"

let result = ""

for (i = 0; i < 5; i++) {
    result += chars[0]
    result += chars[1]
}
result += chars[0]
console.log(result)