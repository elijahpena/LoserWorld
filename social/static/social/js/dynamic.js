$(document).ready(function() {
    $('#create_comment').click( function() {
        $('#create_comment').after("<div id=\"new_comment\"></div>");
        $.ajax({
            type: 'GET',
            url: window.location.href + 'comment_create/',
            data: {},
            dataType: 'html',
            success: function(text) {
                $('#new_comment').prepend(text);
                $('form#comment').attr('action', window.location.href + 'comment_create/');
            }
        });
    });

    function comments() {
        $.ajax({
            type: 'GET',
            url: window.location.href + 'comments/',
            data: {},
            dataType: 'html',
            success: function(text) {
                $('#comments').html('');
                $('#comments').append(text);
            }
        });
    }
    comments();


});

function edit_comment(event) {
    var comment_id = $(this).attr('id');
    $.ajax({
        type: 'GET',
        url: window.location.href + `comment/${comment_id}/update/`,
        data: {},
        dataType: 'html',
        success: function(text) {
            $(`li#${comment_id}`).html('');
            $(`li#${comment_id}`).html(text);
            $('form#comment').attr('action', window.location.href + `comment/${comment_id}/update/`);
        }
    });
}

function delete_comment(event) {
    var comment_id = $(this).attr('id');
    $.ajax({
        type: 'GET',
        url: window.location.href + `comment/${comment_id}/delete/`,
        data: {},
        dataType: 'html',
        success: function(text) {
            $(`li#${comment_id}`).html('');
            $(`li#${comment_id}`).html(text);
            $('form#comment').attr('action', window.location.href + `comment/${comment_id}/delete/`);
        }
    });
}
