const btn_create = document.getElementById("btn_create");
const btn_delete = document.getElementById("btn_delete");
const btn_create_new_consumption = document.getElementById("btn_create_new_consumption");
const btn_send_invoices = document.getElementById("btn_invoices");


function create_database(){
        $.ajax({
          url: "create_database",
         context: document.body
        }).done(function() {
         location.reload()
        });
    }

function create_new_consumption(){
        $.ajax({
          url: "create_new_consumption",
         context: document.body
        }).done(function() {
         location.reload()
        });
    }


 function delete_all_files(){
         $.ajax({
              url: "delete_all_files",
             context: document.body
            }).done(function() {
             location.reload();
            });
        }

 function send_invoices(){
         $.ajax({
              url: "send_invoices",
             context: document.body
            }).done(function() {
             alert("invoices sent");
            });
        }

btn_create.addEventListener("click", function () {
    create_database();
});

btn_create_new_consumption.addEventListener("click", function () {
    create_new_consumption();
});


btn_delete.addEventListener("click", function () {
    delete_all_files();
});

btn_send_invoices.addEventListener("click", function () {
    send_invoices();
});
