function sendData(){
    $('#button').click(function (){
        $.ajax('/ajaxtest/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'username': $('#username').val(),
                'password': $('#password').val(),
                'password_confirm': $('#password_confirm').val()
            },
            'success': function(data){
                alert(data.status);
            }
        })
    })
}

$(document).ready(function(){
    sendData();
})