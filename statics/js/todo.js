//ajax traer lista de todo
getTodoList();

function getTodoList() {
    $.ajax({
        url: "getTodoList/",
        type: "GET",
        success: function (response) {
            response = JSON.parse(response)
            console.log("get todo list")
            console.log("RESPONSE = " + response);




            var html = "";
            var divTodoList = document.getElementById("divTodoList");
            if (response.length == 0) {
                html = "<div class='card'><div class='card-body'><h5 class='card-title'>To-do list is empty.</h5></div></div>";
            } else {
                for (var i = 0; i < response.length; i++) {
                    html += "<div class='card' style='width: 25rem;'><div class='card-body'><h5 class='card-title' align='left'>" + response[i].fields.todo + "</h5><h6 class='card-subtitle mb-2 text-muted' align='left'>" + response[i].fields.date + "</h6>";
                    if (response[i].fields.done) {
                        html += "<input class='form-check-input' type='checkbox' value='1' id='defaultCheck1' onclick='updateTodo(false," + response[i].pk + ")' checked></input>";
                    }
                    else {
                        html += "<input class='form-check-input' type='checkbox' value='1' id='defaultCheck1' onclick='updateTodo(true," + response[i].pk + ")'>";
                    }
                    html += "<label class='form-check-label' for='defaultCheck1'>Done</label><button class='btn btn-primary' align='right' id='dlt' onclick='deleteTodo(" + response[i].pk + ")' type='submit'>Delete</button></div></div>";
                }
            }
            divTodoList.innerHTML = html;
        },
        error: function (response) {
            console.log("Error: " + response)
        }
    });
}


function deleteTodo(idTodo) {
    $.ajax({
        url: "deleteTodo/",
        type: "POST",
        data: { "id": idTodo },
        success: function (response) {
            console.log("Succes: " + response);
            getTodoList();

        },
        error: function (response) {
            console.log("Error: " + response)
        }
    });
}

function addTodo() {
    console.log("Entro aca JS");
    todo = document.getElementById("idNewTodo").value;
    //done = document.getElementById('idCheckboxDone').checked;
    done = false;
    console.log("Tengo esto: " + todo + "   " + done);
    $.ajax({
        url: "addTodo/",
        type: "POST",
        data: { "todo": todo, "done": done },
        success: function (response) {
            console.log("addTodo Succes: " + response);
            getTodoList();
            document.getElementById("idNewTodo").value = "";
            //document.getElementById('idCheckboxDone').checked = false;
        },
        error: function (response) {
            console.log("addTodo Error: " + response)
        }
    });

}

function updateTodo(done, idTodo) {
    $.ajax({
        url: "updateTodo/",
        type: "POST",
        data: { "done": done, "id": idTodo },
        success: function (response) {
            console.log("updateTodo Succes: " + response);
            getTodoList();

        },
        error: function (response) {
            console.log("updateTodo Error: " + response)
        }
    });

}