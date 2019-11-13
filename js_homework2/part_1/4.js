let user_input = prompt("Введите тег, который нужно удалить: ")

function delete_tag(string) {
    if (document.getElementById(string) == null) {
        alert('Такого тега нет, удаление невозможно')
    } else {
        let elm = document.getElementById(string);
        document.body.removeChild(elm)
        alert('Готово!')
    }
}
delete_tag(user_input)