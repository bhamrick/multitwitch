var root_frame = null;

$(document).ready(function() {
    root_frame = new Frame(null);
    root_frame.split_direction="v";
    root_frame.children.push(new Frame(root_frame));
    root_frame.children.push(new Frame(root_frame));
    Resize(root_frame, $(window).width(), $(window).height());
});
