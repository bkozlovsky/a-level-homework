function display_tag(string) {
    return string;
}

function insert_tag(string) {
    let new_element = document.createElement(string)
    document.body.appendChild(new_element)
    return true
}