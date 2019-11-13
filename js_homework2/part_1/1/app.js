let image_request = prompt('Введите ссылку картинки, которую хотите разместить: ')

let rotate_degree = Number(prompt('На сколько градусов повернуть? '))

function is_url(str) {
  regexp =  /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
    if (regexp.test(str)) {
        return true;
    } else {
        return false;
    }
}


try {
    if (is_url(image_request) == true) {
        for (i=0; i < 5; i++) {
            let new_image = document.createElement("img");
            new_image.src = image_request
            new_image.style.transform = myimg.style.transform
            new_image.style.margin = '60px'
            myimg.style.transform +=`rotate(${rotate_degree}deg)`
            img_container.appendChild(new_image)
        }
    } else {
        alert("По-моему ты ввел что-то не то, попробуй еще разок.")
        window.location.reload(true);
    }
} catch (err) {
    alert("Ты точно вводишь правильные данные? Перепроверь и попробуй еще раз.")
    window.location.reload(true);
}
