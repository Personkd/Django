function sendData_comment(){
    $('#create_new_comment').click(function (){
        $.ajax($('#create_new_comment').data('page'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'new_text': $('#text_of_new_comment').val()
            },
            'success': function(template){
                document.getElementById('comments').innerHTML += template;
            }
        });
    })
}

$(document).ready(function(){
    sendData_comment();
})