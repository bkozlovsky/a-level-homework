// 1. Дан массив с числами. Выведите последовательно его элементы используя рекурсию и не используя цикл.
// Так же если елементы массива это object или array, то их елементы тоже выводи отдельно
// [1, 4, 5, [8, 0, 10, 3], 6, 64, 64, 54, {key: "name", age: 18}]

let arr = [1, 4, 5, [8, 0, 10, 3], 6, 64, 64, 54, {key: "name", age: 18}]

function list_elements(array) {
    if (array.length > 0) {
        let arr_elm = array.shift();
        if (Array.isArray(arr_elm) == true) {
            console.log(arr_elm.shift())
            list_elements(arr_elm)
        } else if (arr_elm.constructor == Object) {
            list_elements(Object.values(arr_elm))
        } else {
            console.log(arr_elm);
        }
        list_elements(array);
    };
}

list_elements(arr)

// 2. Дано число. Сложите его цифры. Если сумма получилась более 9-ти, опять сложите его цифры. И так, пока сумма не станет однозначным числом (9 и менее).

function makeArray(number) {
    let array = String(number).split('').map(Number)
    return array
}

function mult_numbers(arr) {
    if (arr.length == 0) {
        return 0
    } else {
        return arr[0] + mult_numbers(arr.slice(1))
    }
}

console.log(mult_numbers(makeArray(123)))

// 3. Дан массив с числами. Создайте из него новый массив, где останутся лежать только положительные числа. Создайте для этого вспомогательную функцию isPositive(), которая параметром будет принимать число и возвращать true, если число положительное, и false - если отрицательное.
// var arr = [1, 2, 3, -1, -2, -3];

let arr = [1, 2, 3, -1, -2, -3];

let newarr = [];

function isPositive(num) {
    if (num > 0) {
        return true
    } else {
        return false
    }
}

function make_array(array) {
    if (array.length == 0) {
        return newarr
    } else {
        if (isPositive(array[0]) == true) {
            newarr.push(array[0])
            make_array(array.slice(1))
        }
    }
}

console.log(make_array(arr))

// 4. Сделайте функцию getDigitsSum (digit - это цифра), которая параметром принимает целое число и возвращает сумму его цифр.

let number = 123

let array = String(number).split('').map(Number)

function getDigitsSum(arr) {
    if (arr.length == 0) {
        return 0
    } else {
        return arr[0] + mult_numbers(arr.slice(1))
    }
}

console.log(getDigitsSum(array))

// 5. Дан массив с числами. Запишите в новый массив только те числа, которые больше нуля и меньше 10-ти. Для этого используйте вспомогательную функцию isNumberInRange из предыдущей задачи.

let arr = [1, 2, 3, -1, -2, -3];

let newarr = [];

function isNumberInRange(num) {
    if (num > 0 && num < 10) {
        return true
    } else {
        return false
    }
}

function make_array(array) {
    if (array.length == 0) {
        return newarr
    } else {
        if (isNumberInRange(array[0]) == true) {
            newarr.push(array[0])
            make_array(array.slice(1))
        }
    }
}

console.log(make_array(arr))

// 7. Сделайте функцию getDivisors, которая параметром принимает число и возвращает массив его делителей (чисел, на которое делится данное число).


// 8. Дан массив с целыми числами. Создайте из него новый массив, где останутся лежать только четные из этих чисел. Для этого используйте вспомогательную функцию isEven из предыдущей задачи.

