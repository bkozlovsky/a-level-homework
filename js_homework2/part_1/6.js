let user_input = prompt("Введите название элемента как показано в примере (id=some_id, class=some_class, tag=some_tag): ")

function $() {
    if (user_input.includes('id') == true) {
        user_input = user_input.replace('id=', '')
        return document.getElementById(user_input)
    } else if (user_input.includes('class') == true) {
        user_input = user_input.replace('class=', '')
        let arr = document.getElementsByClassName(user_input)
        if (arr.length == 1){
            return arr[0]
        } else {
            return arr
        }
    } else if (user_input.includes('tag') == true) {
        user_input = user_input.replace('tag=', '')
        return document.getElementsByTagName(user_input)
    }
}

