/*
09. Обратите внимание на те или иные расчеты, нужные вам в обычной жизни. Это может быть оплата за электричество, количество километров, пройденных за месяц (если вы, например, ходите по одному и тому же маршруту каждый день), количество батонов, кофе, масла, всего чего угодно и так далее. Так же можете написать любую калькуляцию, нужную вам в работе. Представьте это в форме кода, подобного следующему:

var firstParameter = 5; //смысл переменной
var secondParameter = 10; //иной комментарий, поясняющий переменную

var somePartialResult = firstParameter*5; //суть переменной и формулы
var someOtherPartialResult = secondParameter/100500; //

var result = somePartialResult + someOtherPartialResult; //суть результата и переменной

То есть, напишите калькуляцию, которая из входных данных подсчитывает результат, с осмысленными названиями переменных и комментариями к ним и формулам, использованным в калькуляции.

Суть - научиться правильно и осмысленно называть переменные и не только 😉
*/

let stepsGoal = 10000 // ежемесячная цель по количеству шагов, которые нужно пройти

let steps2019 = {'January': 7142, 'February': 7555, 'March': 7941, 'April': 7553, 'May': 6381, 'June': 10305, 'July': 7007, 'August': 10201, 'September': 8272, 'October': 7882} // реальное количество шагов пройденное по месяцам с начала 2019-го года


// инициализируем функцию, которая считает среднее количество пройденных шагов за весь период
function calculateAverage(dict) {
    let sum = 0
    for (let steps of Object.values(dict)) {
        sum += steps
    }
    let average = sum / Object.values(dict).length
    return average
}

// инициализируем функцию, которая анализирует статистику и выводит объект с месяцами и количеством шагов, в которых цель была достигнута
function analyzeActivity(dict) {
    emptyObj = {}
    for (let [month, steps] of Object.entries(dict)) {
        if (steps > stepsGoal) {
            emptyObj[month] = steps
        }
    }
    return emptyObj
}

let stepsAverage2019 = calculateAverage(steps2019) // считаем среднее количество шагов, пройденных за период Январь - Октябрь 2019-го года

let activity2019 = analyzeActivity(steps2019) // анализируем активность в период с Января по Октябрь 2019-го года

// Выдаем сообщение пользователю с результатами
let resultsMessage = "Среднее количество шагов за указанный период: " + stepsAverage2019 + "\n\nВы успешно достигли цели в следующих месяцах: \n"

console.log(resultsMessage)

for (i = 0; i < Object.keys(activity2019).length; i++) {
    console.log(Object.keys(activity2019)[i], " : ", activity2019[Object.keys(activity2019)[i]])
}

//console.log(Object.keys(activity2019))

