/* 1. Выведите столбец чисел от 1 до 50. через do while
50 включительно */

let char = 0

do {
    char++
    console.log(char)
} while (char < 50)

/* 2. Дан массив с элементами [1, 2, 3, 4, 5]. С помощью цикла for выведите все эти элементы на экран. Через for of */

let arr = [1, 2, 3, 4, 5]

for (elm of arr) {
    console.log(elm)
}

/* 3.  Дан массив с элементами [2, 3, 4, 5]. С помощью цикла for найдите произведение элементов этого массива. Через for of */

let arr = [2, 3, 4, 5]

let multipl = 1

for (elm of arr) {
    multipl *= elm
}

console.log(multipl)

/* 4. Дан объект obj с ключами 'Минск', 'Москва', 'Киев' с элементами 'Беларусь', 'Россия', 'Украина'. С помощью цикла for-in выведите на экран строки такого формата: 'Минск - это Беларусь.'.

var obj = {
 'Минск': 'Беларусь',
 'Москва': 'Россия',
 'Киев': 'Украина'
}; */

let obj = {'Минск': 'Беларусь', 'Москва': 'Россия', 'Киев': 'Украина'};

for (x in obj) {
    console.log(`${x} - это ${obj[x]}`);
}

/* 5. Выведите столбец четных чисел в промежутке от 0 до 100. через while */
let i = 0

while (i <= 100) {
    console.log(i)
    i++
}

/* 6. Дан объект obj. С помощью цикла for-in выведите на экран ключи и элементы этого объекта. 
var obj = {green: 'зеленый', red: 'красный', blue: 'голубой'} */

let obj = {green: 'зеленый', red: 'красный', blue: 'голубой'}

for (x in obj) {
    console.log(`Ключ: ${x}; Значение: ${obj[x]}`)
}

/* 7. Дан массив с элементами 2, 5, 9, 15, 0, 4. С помощью цикла for и оператора if выведите на экран столбец тех элементов массива, которые больше 3-х, но меньше 10. */

let arr = [2, 5, 9, 15, 0, 4]

for (elm of arr) {
    if (elm > 3 && elm < 10) {
        console.log(elm)
    }
}

/* 8. Дан массив с числами. Числа могут быть положительными и отрицательными. Найдите сумму положительных элементов массива.*/

let arr = [1, 14, -25, 44, 13, -89, -54, 45]

let sum = 0

for (elm of arr) {
    if (elm > 0) {
        sum += elm
    }
}

console.log(sum)

/* 9. Дан массив с элементами 1, 2, 5, 9, 4, 13, 4, 10. С помощью цикла for и оператора if проверьте есть ли в массиве элемент со значением, равным 4. Если есть - выведите на экран 'Есть!' и выйдите из цикла. Если нет - пропускаем итерацию
 */

let arr = [1, 2, 5, 9, 4, 13, 4, 10]

for (elm of arr) {
    if (elm == 4) {
        console.log("Есть!")
    } else {
        //pass
    }
}

/* 10. Дан массив числами, например: [10, 20, 30, 50, 235, 3000]. Выведите на экран только те числа из массива, которые начинаются на цифру 1, 2 или 5. */

let arr = [10, 20, 30, 50, 235, 3000]

let nums = '125'

for (char of arr) {
    if (String(char).includes(nums[0]) || String(char).includes(nums[1]) || String(char).includes(nums[2])) {
        console.log(char)
    }
}

/* 11. Возведите 2 в 10 степень. Результат запишите в переменную st.*/

let st = 2**10

/* 12. Дана строка 'aaa@bbb@ccc'. Замените все @ на '!' с помощью глобального поиска и замены. (посмотрите replace например) */

let str = 'aaa@bbb@ccc'

result = str.replace(/@/g, '!')

/* 13. Дана строка 'aaa bbb ccc'. Вырежите из нее слово 'bbb' тремя разными способами (через substr, substring, slice). */

let str = 'aaa bbb ccc'

substr_result = str.substr(4, 3)
substring_result = str.substring(4, 7)
slice_result = str.slice(4, 7)

/* 14. В переменной date лежит дата в формате '2025-12-31'. Преобразуйте эту дату в формат '31/12/2025'. */

let date = '2025-12-31'

let arr = date.split("-").reverse()

let result = `${arr[0]}/${arr[1]}/${arr[2]}`

console.log(result)

/* 15. Дана строка 'js'. Сделайте из нее строку 'JS'. */

let str = 'js'

result = str.toUpperCase()

/* 16. Дана строка 'JS'. Сделайте из нее строку 'js'. */

let str = 'JS'

result = str.toLowerCase()

/* 17. Дана строка 'я учу javascript!'. Найдите количество символов в этой строке. */

let str = 'я учу javascript!'

let result = str.length

console.log(result)

/* 18. Дана строка 'я учу javascript!'. Вырежите из нее слово 'учу' и слово 'javascript' тремя разными способами (через substr, substring, slice). */

let str = 'я учу javascript!'

// вырезаем "Учу" тряемя разными способами
substr_result = str.substr(2, 3)
substring_result = str.substring(2, 5)
slice_result = str.slice(2, 5)

// выразаем 'javascript' тремя разными способами

substr_result = str.substr(6, 10)
substring_result = str.substring(6, 16)
slice_result = str.slice(6, 16)

/* 19. Дана строка 'я учу javascript!'. Найдите позицию подстроки 'учу'. */

let str = 'я учу javascript!'

result = str.indexOf('учу')

console.log(result)

/* 20. Дана строка 'Я-учу-javascript!'. Замените все дефисы на '!' с помощью глобального поиска и замены. */

let str = 'Я-учу-javascript!'

console.log(str.replace(/-/g, '!'))

/* 21. Дана строка 'я учу javascript!'. С помощью метода split запишите каждое слово этой строки в отдельный элемент массива.
 */

let str = 'Я-учу-javascript!'

let arr = str.split("-")

console.log(arr)

/* 22. Дана строка 'я учу javascript!'. С помощью метода split запишите каждый символ этой строки в отдельный элемент массива. */

let str = 'Я-учу-javascript!'

let arr = str.split('')

console.log(arr)

/* 23. В переменной date лежит дата в формате '2025-12-31'. Преобразуйте эту дату в формат '31.12.2025'. */

let date = '2025-12-31'

let arr = date.split("-").reverse()

let result = `${arr[0]}.${arr[1]}.${arr[2]}`

console.log(result)

/* 24. Дан массив ['я', 'учу', 'javascript', '!']. С помощью метода join преобразуйте массив в строку 'я+учу+javascript+!'.
 */

let arr = ['я', 'учу', 'javascript', '!']

console.log(arr.join("+"))

/* 25. Напишите функция, которая принимает аргументом строку и возврашает нам строку преобразуя первую букву строки в верхний регистр.*/

let str = "это обычная строка"

function titleFirstCase(string) {
    let arr = string.split('')
    arr[0] = arr[0].toUpperCase()
    return arr.join('')
}

console.log(titleFirstCase(str))

/* 26. Напишите функция, которая принимает аргументом строку и возврашает нам строку преобразуя последнюю букву строки в верхний регистр. */

let str = "это обычная строка"

function titleLastCase(string) {
    let arr = string.split('')
    arr[arr.length -1] = arr[arr.length -1].toUpperCase()
    return arr.join('')
}

console.log(titleLastCase(str))

/* 27. Напишите функция, которая принимает аргументом строку и преобразуйте например 'var_test_text' в 'varTestText'. Функция, конечно же, должен работать с любыми аналогичными строками.
 */

let str = 'var_test_text_another_length_added'

function convertString(string) {
    arr = string.split("_")
    arr2 = arr.slice(1)
    for (i in arr2) {
        arr2[i] = arr2[i].split('')
        arr2[i][0] = arr2[i][0].toUpperCase()
        arr2[i] = arr2[i].join('')
    }
    return `${arr[0]}` + arr2.join('')
}

console.log(convertString(str))

/* 28. Создайте смешанный массив, например [1, 2, 3, ‘a’, ‘b’, ‘c’, ‘4’, ‘5’, ‘6’]. Посчитайте сумму всех его чисел, включая строковые. Выведите сумму в alert. */

let arr = [1, 2, 3, 'a', 'b', 'c', '4', '5', '6']

let sum = 0

for (elm of arr) {
    if (isNaN(Number(elm)) == false) {
        sum += Number(elm)
    }
}

console.log(sum)

/* 29. Сгенерируйте массив из n случайных чисел с двумя знаками после запятой. Переберите массив и распечатайте в консоли значения его элементов, возведенные в пятую степень, не используя функцию Math.pow(). */

let arr = []

for (var i = 0; i < 15; i++) {
    arr.push((Math.random() * 10).toFixed(2))
}

for (elm of arr) {
    console.log(elm ** 5)
}

/* 30. Создайте массив со значениями: ‘AngularJS’, ‘jQuery’
 a. Добавьте в начало массива значение ‘Backbone.js’
 b. Добавьте в конец массива значения ‘ReactJS’ и ‘
 c. Добавьте в массив значение ‘CommonJS’ вторым элементом
 d. Найдите и удалите из массива значение ‘jQuery’, выведите его в alert со словами “Это здесь лишнее”
 z.  Сделайте массив и назовите dlyaLyudshix, перебирает массив, где только удалили ‘jQuery’, и перебирайте этот массив и если вы найдёте там значние ‘Vue.js’, то положите в массив с названием dlyaLyudshix */

 let arr = ['AngularJS', 'jQuery'];

 arr.push('ReactJS', 'Vue.js')
 
 arr.unshift('Backbone.js')
 
 arr[1] = 'CommonJS'
 
 arr.splice(arr.indexOf('jQuery'), 1)
 
 let dlyaLyudshix = []
 
 for (elm of arr) {
     if (elm == 'Vue.js') {
         dlyaLyudshix.push(elm)
     }
 }
 
 console.log(dlyaLyudshix)

 /* 31. Задание на МС.  Создайте пустой массив. В цикле до n на каждой итерации запускайте prompt для ввода любых символов, полученное значение добавляйте в конец созданного массива. После выхода из цикла посчитайте сумму всех чисел массива и выведите в alert полученный результат */

let arr = []

i = 0
sum = 0

while (i < 5) {
    char_input = prompt("Введите символ: ")
    arr.push(char_input)
    i++
 }

for (elm of arr) {
    if (isNaN(Number(elm)) == false) {
        sum += Number(elm)
    }
}

console.log(`Сумма чисел в массиве: ${sum}`)

/* 32. Задание на МС.  Напишите объект, описывающий модель телефона, заполнив все свойства значениями, прочитанными из prompt (например: brand, model, resolution, color...). */

let obj = {}

let brand = prompt("Введите название бренда вашего телефона: ")

let model = prompt("Введите модель вашего телефона: ")

let color = prompt("Введите цвет вашего телефона: ")

obj['brand'] = brand
obj['model'] = model
obj['color'] = color

console.log(obj)

/* 33. Задание на МСМК: Создайте строку с текстом ‘Как однажды Жак звонарь сломал фонарь головой’. Разбейте ее на массив слов, и переставьте слова в правильном порядке с помощью любых методов массива (indexOf, splice ...). Затем объедините элементы массива в строку и выведите в alert исходный и итоговый варианты. */

let str = 'Как однажды Жак звонарь сломал фонарь головой'

let arr = str.split(" ")

let alt1 = arr.splice(0, 4)

alt1.push(arr[arr.length -1], arr[arr.length -3], arr[arr.length -2])

console.log(alt1.join(' '))

/* 34. Используя вложенные циклы, сформируйте двумерный массив, содержащий таблицу умножения:
 "1x1=1; 2x1=1"
 "1x2=2; 2x2=4"
И выходим и останавливаем цикл, когда будет 6 умножнить на 6 */

let j = 1

let arr = []

while (j <= 6) {
    for (i = 1; i <= 6; i++) {
        let mult = j * i
        result = [`${j}x${i}=${mult}`]
        arr.push(result)
        i++
    }
    j++
}

console.log(arr)