 function validate_input(){
    var pass1 = document.getElementById("pass1").value;
    var pass2 = document.getElementById("pass2").value;
    var mail = document.getElementById("email").value;
    var button = document.getElementById("submit_button");
    var checkpass;
    var checkemail;
    if (pass1 == pass2){
        checkpass = true;
    }
    else{
        checkpass=false;
    }
    checkemail = mail.includes("@");
    if (checkemail == true && checkpass == true){
        button.classList.remove("button_initial_state");
        button.classList.add("button_check_true");
    }
    else{
        button.classList.remove("button_initial_state");
        button.classList.add("button_check_false");
    }
}

