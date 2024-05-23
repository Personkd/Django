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
                document.getElementById('comments').innerHTML += template
            }
        })
    })
}

function sendData_post(){
    $("#update_post").click(function (){
        $.ajax($("update_post").data('page'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'updated_post': $('#text_of_updated_post').val()
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