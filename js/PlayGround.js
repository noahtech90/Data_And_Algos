function generateHTML() {   
    var para = document.createElement("p");
    var node = document.createTextNode("Writing HTML with Javascript");
    var rando = document.createTextNode("  Lorem ipsum dolor sit amet consectetur adipisicing elit.")

    var btn = document.createElement("button")
    var btnText = document.createTextNode("This is another button")

    para.appendChild(node);
    para.appendChild(rando);
    btn.appendChild(btnText)


    var element = document.getElementById("javascript");
    element.appendChild(para);
    element.appendChild(btn)
    } 
