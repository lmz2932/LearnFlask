function change(){
    var x = document.getElementById("demo");
    x.innerHTML = Date();
}

function showArray(){
    var a = new Array("Chery", "Geely");
    var b = ["Volvo", "Saab"];
    var c = new Array();
    c[0] = "Audi";
    c[1] = "Volkswagen";

    console.log(a);
    console.log(b);
    console.log(c);
}

function showObject(){
    var person = {
        first_name: "mars",
        last_name: "loo",
        "age": 25,
        full_name: function (){
            return this.first_name + " " + this.last_name;
        }
    };

    console.log(person.full_name);
    document.write(person.full_name);
}

function dbclick(){
    alert("double click");
}

function changeLetter(char){
    return String.fromCharCode(char.charCodeAt(0)+1)
}

var d = new Date()
console.log(Number(false));
