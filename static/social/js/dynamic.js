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
                $('#comments').append(text);
                setTimeout(function() {
                    comments();
                }, 5000);
            }
        });
    }
    comments();
});
