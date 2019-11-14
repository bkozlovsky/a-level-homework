// 1. Даны ссылки. Привяжите всем ссылкам событие - каждый раз по наведению на ссылку в конец атрибута title запишется её текст.

let elements = document.getElementsByTagName('a')

let arr = Array.from(elements)

arr.forEach(function(elm) {
    elm.onmouseover = function() {
        elm.title = elm.innerText
    }
})


// 2. 5 ссылок. Привяжите всем ссылкам событие онклик - по клику на ссылку в конец ее текста дописывается ее href в круглых скобках. Внутри href должно быть по умолчанию https://google.com

let elements = document.getElementsByTagName('a')

let arr = Array.from(elements)

arr.forEach(function(elm) {
    elm.onclick = function() {
        elm.innerText += ` (${elm.href})`
    }
})

// 3. 5 ссылок как и в задаче 2. Только после трех кликов на ссылку следует убрать от нее событие, которое добавляет href в конец текста как в предыдушей задачи

let elements = document.getElementsByTagName('a')

let arr = Array.from(elements)

let counter = 0

arr.forEach(function(elm) {
    elm.onclick = function() {
        elm.innerText += ` (${elm.href})`
        counter += 1
    if (counter == 3) {
        elm.onclick = null
    }
    }
})

// 4. Дано 20 абзацов с числами от 1 до 20. По нажатию на абзац в нем должен появится квадрат числа, которое он содержит. Так же написать мне код Emmet(как генерировать 20 абзацов).
// Разраешается написать 2 строки кода в js

p{$}*20 // Emmet code

// Всё нужно писать через let, const, и стрелочными функциями

Array.from(document.getElementsByTagName('p')).forEach((elm) => elm.onclick = () => elm.innerText = elm.innerText ** 2)

// 6. Создать button и повесить обработчик. При при нажатии должно выдавать alert("Hey")

document.getElementById('button1').onclick = function() {
    alert('Hey')
}

// 7. Создать button и повесить обработчик нажатие. По нажатию на кнопку должно поменяться ее текст. По умолчанию Кнопка. После нажатие Кирпич

let elm = document.getElementById('button1')

elm.onclick = function() {
    elm.innerText = 'Кирпич'
}


// 12. Дан элемент #myunique. Узнайте количество его классов при нажатии и вставялйте в innerText.

let elm = document.getElementById('myunique')

let elm_classes = elm.classList

elm.onclick = function() {
    alert(`В данном элементе ${elm_classes.length} классов`)
    elm_classes.forEach(function(element) {
        elm.innerText += ` ${element}`
    })
}


// 13. Даны элементы с классом www$, $ - это инкремент. Добавьте каждому элементу в конец название его тега в нижнем регистре при нажатии. Каждый раз.


// 15. Дан ol, а внутри него li. Сделайте так, чтобы по нажатию на любую li эта li удалялась.

let elements = document.getElementsByTagName('li')

let arr = Array.from(elements)

arr.forEach(function(elm) {
    elm.onclick = function() {
        document.getElementsByTagName('ol')[0].removeChild(elm)
    }
})

// 16. Дан инпут. Дана кнопка. По нажатию на кнопку клонируйте этот инпут и вставляйте рядом.

let input = document.getElementById('input1')

let button = document.getElementById('myunique')

button.onclick = function() {
    let new_element = input.cloneNode(true)
    new_element.id = 'input2'
    input.after(new_element)
}

// 17. Высота body 2000px; По нажатию на кнопку прокрутите страницу до самого низа

myunique.onclick = function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}

// 18. Дан элемент #myunique. По клику на него увеличьте его ширину и высоту и шрифт в 2 раза. Делайте это анимировано

myunique.onclick = function() {
    myunique.style.padding = '20px 40px'
    myunique.style.fontSize = '40px'
    myunique.style.backgroundColor = 'red'
    myunique.style.transition = '2s all'
}