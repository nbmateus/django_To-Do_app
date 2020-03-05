$(document).ready(function(){
    var loginForm = $("#idLoginForm")
    var regForm = $("#idRegForm")
    
    loginForm.submit(function(){
        event.preventDefault();
        $.ajax({
            url: $(this).attr("action"),
            type: $(this).attr("method"),
            data: $(this).serialize(),
            success: function (response) {      
                if(response.errors){
                    document.getElementById('idLogFormErrors').innerHTML ="<font color='red'>"+response.errors.__all__+"</font>";
                }else{
                    window.location.href = response.redirectUrl;
                }
            },
            error: function (response) {
                console.log("Error: " + response)
            }
        });

    })

    regForm.submit(function(){
        event.preventDefault();
        $.ajax({
            url: $(this).attr("action"),
            type: $(this).attr("method"),
            data: $(this).serialize(),
            success: function (response) { 
                if(response.errors){
                    if(response.errors.username){
                        document.getElementById('idRegFormErrors').innerHTML ="<font color='red'>"+response.errors.username+"</font>";
                    }else if(response.errors.password2){
                        document.getElementById('idRegFormErrors').innerHTML ="<font color='red'>"+response.errors.password2+"</font>";
                    }else if(response.errors){
                        document.getElementById('idRegFormErrors').innerHTML ="<font color='red'>Undefined error.</font>";
                    }
                }  
                else{
                    window.location.href = response.redirectUrl;
                }
            },
            error: function (response) {
                console.log("Error: " + response)
            }
        });      
    })

})


/*
$(document).ready(function () {
    $("#idLoginBtn").click(function () {
        $.ajax({
            url: "/signIn/",
            type: "POST",
            data: { "username": $('#idLogUser').val(), "password": $('#idLogPass').val() },
            success: function (response) {
                console.log("Success: " + response)
            },
            error: function (response) {
                console.log("Error: " + response)
            }
        });
    });
});

$(document).ready(function () {
    $("#idRegBtn").click(function () {
        if ($('#idSignUpPass1').val() != $('#idSignUpPass2').val()) {
            alert("Passwords must be the same!");
        }
        else {
            $.ajax({
                url: "/signIn/",
                type: "POST",
                data: { "username": $('#idSignUpUser').val(), "password": $('#idSignUpPass1').val() },
                success: function (response) {
                    console.log("Success: " + response)
                },
                error: function (response) {
                    console.log("Error: " + response)
                }
            });
        }

    });
});


function signupForm() {
    var regForm = document.getElementById('idSignUpForm')
    console.log("MANDO REG")
    $.ajax({
        type: regForm.attr('method'),
        url: regForm.attr('action'),
        data: regForm.serialize(),
        success: function (data) {
            regForm.innerHTML = "{% csrf_token %}{{ regForm }}";
        },
        error: function (data) {
            console.log("error")
        }
    });
});*/