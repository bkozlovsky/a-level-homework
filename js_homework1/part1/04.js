/*
04. В переменную day записан текущий день недели. Если это не суббота и не воскресенье, выведите в console.log сообщение о необходимости идти на работу.
*/

let weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

let today = 'monday'

//через if else

if (weekdays.includes(today) == true) {
    console.log("Иди на работу!")
} else {
    console.log("Отдыхай!")
}

//через тернарку

let result = weekdays.includes(today) == true ? console.log("Иди на работу!") : console.log("Отдыхай!")
