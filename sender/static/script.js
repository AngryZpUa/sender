function CheckBoxTeploseti(){
    if (document.getElementById("check_teploseti").checked){
        document.getElementById("account_surname").disabled = false;
        document.getElementById("hot_water_counter").disabled = false;
    }
    else{
        document.getElementById("account_surname").disabled = true;
        document.getElementById("hot_water_counter").disabled = true;
    }
}

function CheckBoxOblenergo(){
    if (document.getElementById("check_oblenergo").checked){
        document.getElementById("electricity_counter").disabled = false;
    }
    else{
        if (document.getElementById("check_elektropostach").checked){
            document.getElementById("electricity_counter").disabled = false;
        }
        else{
            document.getElementById("electricity_counter").disabled = true;
        }
    }
}

function CheckBoxElektropostach(){
    if (document.getElementById("check_elektropostach").checked){
        document.getElementById("elektropostach_password").disabled = false;
        document.getElementById("electricity_counter").disabled = false;
    }
    else{
        document.getElementById("elektropostach_password").disabled = true;
        if (document.getElementById("check_oblenergo").checked){
            document.getElementById("electricity_counter").disabled = false;
        }
        else{
            document.getElementById("electricity_counter").disabled = true;
        }
    }
}

function CheckBoxVodokanal(){
    if (document.getElementById("check_vodokanal").checked){
        document.getElementById("vodokanal_password").disabled = false;
        document.getElementById("cold_water_counter").disabled = false;
    }
    else{
        document.getElementById("vodokanal_password").disabled = true;
        document.getElementById("cold_water_counter").disabled = true;
    }
}

function ClearLabels(){
    document.getElementById("label_teploseti").innerHTML = "";
    document.getElementById("label_teploseti").className = "label";
    document.getElementById("label_oblenergo").innerHTML = "";
    document.getElementById("label_oblenergo").className = "label";
    document.getElementById("label_elektropostach").innerHTML = "";
    document.getElementById("label_elektropostach").className = "label";
    document.getElementById("label_vodokanal").innerHTML = "";
    document.getElementById("label_vodokanal").className = "label";
}