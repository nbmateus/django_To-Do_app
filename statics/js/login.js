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
*/