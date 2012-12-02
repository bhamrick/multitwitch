function Frame(parent_frame) {
    this.width = 0;
    this.height = 0;
    this.parent_frame = parent_frame;
    this.children = new Array();
    this.split_direction = "";
    if (parent_frame != null) {
        this.content_node = document.createElement('div');
        parent_frame.content_node.appendChild(this.content_node)
    } else {
        this.content_node = document.getElementById('root_content_node');
    }
}

function Resize(frame, width, height) {
    alert("" + frame + " " + width + " " + height);
    frame.width = width;
    frame.height = height;
    // Update actual DOM dimensions too
    frame.content_node.style.width = width + "px";
    frame.content_node.style.height = height + "px";
    alert(frame.split_direction);
    if(frame.split_direction == "h") {
        alert("horizontal");
        // Horizontal splits divide the height evenly
        for(var i = 0; i < frame.children.length; i++) {
            Resize(frame.children[i], width, height/frame.children.length);
        }
    } else if(frame.split_direction == "v") {
        alert("vertical");
        // Vertical splits divide the width evenly
        for(var i = 0; i < frame.children.length; i++) {
            Resize(frame.children[i], width/frame.children.length, height);
        }
    }
}
