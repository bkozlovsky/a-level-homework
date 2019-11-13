// 1. Высота body 4000px; Через каждые 3 секунды плавно крутите "ползунок" вниз и так же через секунду вверх. И так бесконечно раз

setInterval(function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}, 3000)

setInterval(function() {
    window.scrollTo({
        top: -document.body.scrollHeight,
        behavior: "smooth"
    });
}, 1000)

// 2. Дан ol. Через 3 секунды получите его последнего потомка и удалите его.

setInterval(function() {
    let arr = document.getElementsByTagName('ol')[0].children
    let last_child = arr[arr.length - 1]
    document.getElementsByTagName('ol')[0].removeChild(last_child)
}, 3000)

// 3. Проверка на номер. Создать input и каждый раз, когда пользователь печатает текст. Проверять на то, что внутри input только число. Если там только число, то светить текст зеленым, если не только число, то светить красным. PS. color: red, green | Проверять через setInterval

input.oninput = function() {
    if (isNaN(input.value) == true) {
        input.style.color = 'red'
    } else {
        input.style.color = 'green'
    }
}


// 4. Дан элемент в вёрстке с id #myunique. Добавьте ему класс www. через js естественно

myunique.classList.add("www")

// 5. Дан элемент #myunique. Удалите у него класс www.

myunique.classList.remove("www")

// 6. Дан элемент #myunique. Проверьте наличие у него класса www.

myunique.classList.forEach(function(elm) {
	if (elm == 'www') {
		console.log(true);
    } else {
		console.log(false)
	}
});

// 7. Дан элемент #myunique. Добавьте ему класс www, если его нет и удалите - если есть. | Вы зарание не знаете, есть тамм этот класс или нету

if (myunique.classList.length > 0) {
    myunique.classList.forEach(function(elm) {
        if (elm == 'www') {
            myunique.classList.remove("www")
            console.log('Removed!')
        } else {
            myunique.classList.add("www")
            console.log('Added!')
        }
    });
} else {
    myunique.classList.add("www")
    console.log('Added!')
}

// 8. Дан элемент #myunique. Узнайте количество его классов.

let class_number = myunique.classList.length

// 9. Дан элемент #myunique. По клику на него выведите название его тега.

myunique.onclick = (function(e) {
    alert(myunique.tagName)
})

// 10. Дан элемент #myunique. По клику на него выведите название его тега в нижнем регистре.

myunique.onclick = (function(e) {
    alert(myunique.tagName.toLowerCase())
})

// 11. Даны элементы с классом www. Добавьте каждому элементу в конец название его тега в нижнем регистре.

myunique.classList.forEach(function(elm) {
	if (elm == 'www') {
        document.getElementsByClassName(elm)[0].innerText += myunique.tagName.toLowerCase()
    } else {
		console.log(false)
	}
});

// 12. Дан ol. Вставьте ему в конец li с текстом 'HELLO WORLD!'.

let node = document.createElement('li');
let nodetext = document.createTextNode("HELLO WORLD!");
node.appendChild(nodetext)
document.getElementsByTagName('ol')[0].appendChild(node)

// 13. Дан элемент ul, а в нем li #myunique. Вставь alert те перед элементом #myunique новую li с текстом '!!!'.

let arr = document.getElementsByTagName('ul')[0].children

for (i=0; i < arr.length; i++) {
    elm = arr[i]
    if (elm.innerText == '#myunique') {
        let node = document.createElement('li');
        let nodetext = document.createTextNode("!!!");
        node.appendChild(nodetext)
        document.getElementsByTagName('ul')[0].insertBefore(node, elm)
        break;
    }
};

// 14. Дан элемент #elem. Найдите его соседа сверху и добавьте ему в конец текст '!'.

let arr = document.getElementsByTagName('ul')[0].children

for (i=0; i < arr.length; i++) {
    elm = arr[i]
    if (elm.innerText == '#elem') {
        arr[i-1].innerText += '!'
        break;
    }
};