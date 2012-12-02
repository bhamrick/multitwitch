function optimize_size(n) {
    var height = $(window).innerHeight();
    var width = $(window).innerWidth();
    alert("" + height + " x " + width);
    var best_height = 0;
    var best_width = 0;
    for (var per_row = 1; per_row <= n; per_row++) {
        var num_rows = Math.ceil(n / per_row);
        var max_width = Math.floor(width / per_row) - 4;
        var max_height = Math.floor(height / num_rows) - 4;
        if (max_width * 9/16 + 30 < max_height) {
            max_height = max_width * 9/16 + 30;
        } else {
            max_width = (max_height - 30) * 16/9;
        }
        alert("" + per_row + " : " + max_height + " x " + max_width);
        if (max_width > best_width) {
            best_width = max_width;
            best_height = max_height;
        }
    }
    $(".stream").height(best_height);
    $(".stream").width(best_width);
}
