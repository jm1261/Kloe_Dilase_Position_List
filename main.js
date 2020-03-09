// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction

// $(document).ready(function () {
//     console.log("ready!");
//     var butt = document.getElementById("submit");
//     butt.addEventListener('click', getValues);
// });

function makePosList(){
    var pls = getValues();
    var outstring = formatValues();
    saveValues();
}

function getValues(){

    var posListValues = {
        filepath : document.getElementById('filepath').value,
        user : document.getElementById('user').value,
        filename : document.getElementById('filename').value,
        laser : document.getElementById('laser').value,
        modulation : document.getElementById('modulation').value,
        velocity : document.getElementById('velocity').value,
        x_initial : document.getElementById('x_initial').value,
        y_initial : document.getElementById('y_initial').value,
        z_initial : document.getElementById('z_initial').value,
        delta_mod : document.getElementById('delta_mod').value,
        delta_vel : document.getElementById('delta_vel').value,
        delta_x : document.getElementById('delta_x').value,
        delta_y : document.getElementById('delta_y').value,
        delta_z : document.getElementById('delta_z').value,
        repeats : document.getElementById('repeats').value,
    }

    return posListValues;
};

function formatValues(){

}

function saveValues(){
    
}

var defaultInputs = {
    "filepath": "D:\\LITHO FILES",
    "user": "Josh",
    "filename": "Test",
    "laser": 10,
    "modulation": 0.0,
    "velocity": 50,
    "x_initial": 1,
    "y_initial": 1,
    "z_initial": 0,
    "delta_mod": 10,
    "delta_vel": 1,
    "delta_x": 0.5,
    "delta_y": 1,
    "delta_z": 1,
    "repeats": 10
}