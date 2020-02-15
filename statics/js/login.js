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