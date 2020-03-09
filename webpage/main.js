function makePosList(){

    var pls = getValues();
    var outstring = '';

    // Select laser
    if (pls.laser=='10'){
        outstring = '"ALS" "Ligne2/Laser1"' +  '<br>';
    } else {
        outstring = '"ALS" "Ligne1/Laser1"' +  '<br>';
    };

    // Add parameter sweep
    outstring += formatSweep(pls);

    // Output to page
    document.getElementById('outDiv').innerHTML += outstring;
}

function getValues(){

    var posListValues = {
        filepath : document.getElementById('filepath').value,
        user : document.getElementById('user').value,
        filename : document.getElementById('filename').value,
        laser : document.getElementById('laser').value,
        modulation : parseFloat(document.getElementById('modulation').value),
        velocity : parseFloat(document.getElementById('velocity').value),
        x_initial : parseFloat(document.getElementById('x_initial').value),
        y_initial : parseFloat(document.getElementById('y_initial').value),
        z_initial : parseFloat(document.getElementById('z_initial').value),
        delta_mod : parseFloat(document.getElementById('delta_mod').value),
        delta_vel : parseFloat(document.getElementById('delta_vel').value),
        delta_x : parseFloat(document.getElementById('delta_x').value),
        delta_y : parseFloat(document.getElementById('delta_y').value),
        delta_z : parseFloat(document.getElementById('delta_z').value),
        repeats : parseInt(document.getElementById('repeats').value),
    }

    return posListValues;
};

function formatSweep(pls){

    var filepath = pls.filepath+'\\'+pls.filename+'.LWO';
    var modulation = pls.modulation;
    var velocity = pls.velocity;
    var x_initial = pls.x_initial;
    var y_initial = pls.y_initial;
    var z_initial = pls.z_initial;

    var outstring = ""

    for(var i=0; i < (pls.repeats); i++){

        // Format string
        var plsarray = [filepath, modulation, velocity,
            x_initial, y_initial, z_initial];
        var positionString = '"LWO" "' + plsarray.join('" "') + '"' + '<br>';

        // Update values
        outstring += positionString
        modulation += pls.delta_mod;
        velocity += pls.delta_vel;
        x_initial += pls.delta_x;
        y_initial += pls.delta_y;
        z_initial += pls.delta_z;
    }
    return outstring
}