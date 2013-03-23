var chat_hidden = false;

function optimize_size(n) {
    resize_chat();

    var height = $(window).innerHeight();
    var width = $("#streams").width();
    var best_height = 0;
    var best_width = 0;
    var wrapper_padding = 0;
    for (var per_row = 1; per_row <= n; per_row++) {
        var num_rows = Math.ceil(n / per_row);
        var max_width = Math.floor(width / per_row) - 4;
        var max_height = Math.floor(height / num_rows) - 4;
        if (max_width * 9/16 + 30 < max_height) {
            max_height = max_width * 9/16 + 30;
        } else {
            max_width = (max_height - 30) * 16/9;
        }
        if (max_width > best_width) {
            best_width = max_width;
            best_height = max_height;
            wrapper_padding = (height - num_rows * max_height)/2;
        }
    }
    $(".stream").height(best_height);
    $(".stream").width(best_width);
    $("#streams").css("padding-top", wrapper_padding);
}

function absolute_center(object) {
    var window_height = $(window).height();
    var window_width = $(window).innerWidth();
    var obj_height = object.height();
    var obj_width = object.width();
    var pos_x = (window_width - obj_width)/2;
    var pos_y = (window_height - obj_height)/2;
    if (pos_x < 0) {
        pos_x = 0;
    }
    if (pos_y < 0) {
        pos_y = 0;
    }
    object.css('position', 'absolute');
    object.css('left', pos_x);
    object.css('top', pos_y);
}

function resize_chat() {
    // Semi-placeholder
    var window_height = $(window).height();
    if(!chat_hidden) {
        var chat_width = 304;
        var wrapper_width = $("#wrapper").width();
        $("#streams").width(wrapper_width - chat_width - 10);
        $("#chatbox").width(chat_width);
        $(".stream_chat").height(window_height - 75);
    }
}
