let user_input = prompt("Введите элемент, значение которого нужно найти: ")

function getInnerTextOfElement(string) {
    let s = '#.'
    if (string.includes(s[0]) == true) {
        string = string.replace(s[0], '')
        return document.getElementById(string).innerText
    } else if ((string.includes(s[1]) == true)) {
        string = string.replace(s[1], '')
        return document.getElementsByClassName(string)[0].innerText
    }
}