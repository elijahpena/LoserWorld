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
            }
        });
    });
});
