$(document).ready(function(){


    /*$(".focus-trigger-login").focus(function(){
        changeView(1);
    });*/

    $(".focus-trigger-search").focus(function(){
         changeView(2);
    });


    /*main menu navigation*/
    $(".menu-select-assets").click("input", function(){
        $(".logged-iframe").attr("src", "../static/iframe_pages/assets.html");
        $(".search-container-logged").css("visibility", "visible");
        $(".top-crud-buttons").css("visibility", "visible");
        $(".inside-frame-logged").css("visibility", "visible");
    });

    $("#add_book_button").click(function(){
        $.ajax({
            url: "/api/resources",
            method: "POST",
            success: function(){
                window.location.href = "{{ url_for('search_book') }}"
            },
        });
    });

    $("#register-button").click(function(){
        $(".registration-box").css("visibility", "visible");
    });

    $("#close-button-register").click(function(){
        $(".registration-box").css("visibility", "hidden");
    });

    $("#delete_confirm").click(function(){
        $("#confirmation-box-delete-id").css("visibility", "visible");
    });

    $("#delete-cancel").click(function(){
        $(".confirmation-box").css("visibility", "hidden");
    });

    $(".menu-select-users").click(function(){
        $("#registration-box-employee").css("visibility", "visible");
    });

    $("#toggleButton").val(0);

    $("#toggleButton").change(function(){

        if ($(this).is(":checked")){

            $(this).val(1);
        }else{

             $(this).val(0);
        }
    });


    $("#add-user-typing").on("input", function(){
        var key = $("#add-user-typing").val();
        get_employee(key);

    });


    function update(value){
        var values = value.split(",");
        var is_admin = "";

        $("#update-name").val(values[1]);
       /* $("#update-surname").val(values[1]);*/
        $("#update-email").val(values[3]);
        $("#update-phone").val(values[4]);
        $("#update-posistion").val(values[2]);
        $("#update-heading").text("Update user information");
        $("#update-submit").prop("disabled", false);
    }

    function delete_employee(employee_id){

        $.ajax({
            url: "/api/delete_employee/<employee_id>",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({employee_id: employee_id}),
            success: function(response){
                alert("Employee deleted");
            }
        });

    }

/*display book info in front-end*/
    function select_book(book_id) {

        $(".isbn-display").text(book_id);
        /*get data from api*/
        /*set remaining text values*/
        $(".checkin-button").val(book_id);
        $(".checkin-button").val(book_id);
    }

 $(".checkin-button").click(function(){
    alert(this.value);
 })

/*get books from database based on keyword*/
    function get_books(keyword){

        $.ajax({
            url: "/api/local_books/<key_word>",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({key_word: keyword}),
            success: function(response){
                $(".logged-list").empty();

                $.each(response, function(index, row){
                    var item = `<button class="lists-items list-group-item book_list list-item-logged select-book-transaction" value="${row[0]}">${row[1]}</button>`;

                    $(".logged-list").append(item);

                });
            }
        });
    }


    /*click event for selecting book*/
    $(".logged-list").on("click", ".select-book-transaction", function(){
        select_book(this.value);

    });


    $("#typing-search-resource").on("input", function(){
        var key = $("#typing-search-resource").val()

        get_books(key);
    });


    //fetch employees
    function get_employee(keyword){

        $.ajax({
            url: "/api/user_search",
            type: "POST",
            data: {user_key: keyword},
            success: function(response){
                
                $("#view-add-employee").empty();

                $.each(response, function(index, row){
                    var item = `<li class="lists-items list-group-item book_list list-item-logged add-user-scroll_list add-user-content-container">
                               <div class="add-user-text-container">
                                   ${row[1]}
                               </div>
                               <div class="add-user-buttons-container">
                                    <button class="submit-button btn btn-info sub universal-menu-text" id="edit-button" value="${row}">Edit</button>
                                    <button class="submit-button btn btn-info sub universal-menu-text" id="delete-employee" value="${row[3]}">Delete</button>
                               </div>
                       </li>`;

                $("#view-add-employee").append(item);
                });
            }
        });
    }

    $("#view-add-employee").on("click", "#edit-button", function() {
                update(this.value);
    });

    $("#view-add-employee").on("click", "#delete-employee", function() {
                delete_employee(this.value);
    });


    $("#update-submit").click(function(event){
        event.preventDefault();

        var name = $("#update-name").val();
        var surname = $("#update-surname").val();
        var email = $("#update-email").val();
        var phone = $("#update-phone").val();
        var password = $("#update-password").val();
        var position = $("#update-posistion").val();
        var is_admin = $("#toggleButton").val();

        $.ajax({
            url: "/api/update_employee/<employee_info>",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                name: name,
                surname: surname,
                email: email,
                phone: phone,
                position: position,
                password: password,
                is_admin: is_admin
            }),
            success: function(response){
                alert("Emplyoyee information updated");
            }
        });
    });



    $("#logout").click(function(){
        $("#signout-form").submit(); 
    });


$.event.special.contentChanged = {
    setup: function() {
        var $this = $(this),
            $origHtml = $this.html();

        $this.data('origHtml', $origHtml);
        $this.on('DOMSubtreeModified', function() {
            if($this.data('origHtml') !== $this.html()) {
                $this.trigger('contentChanged');
            }
        });
    },
    teardown: function() {
        $(this).off('DOMSubtreeModified');
    }
};


$(".success-msg").hover(function(){
    $("#success").delay(3000).fadeOut('slow');
});

$('.success-msg').on('contentChanged', function() {
    if ($(this).html().trim() !== '') {

        //Do
    } else {

        $("#success").delay(3000).fadeOut('slow');
        $("#error").delay(3000).fadeOut('slow');
    }
});


$(".success-msg").click(function(){
    $('.success-msg').trigger('contentChanged');
});

$('.success-msg').trigger('contentChanged');


//change view of main page
    function changeView(flag){
        if (flag === 0){
            $(".body_container").css("flex-direction", "row");
            $(".text-container").css("width", "50%");

        } else if (flag === 1){
            $(".body_container").css("flex-direction", "column");
            $(".text-container").css("width", "100%");

        }else{
            $(".body_container").css("flex-direction", "column-reverse");
            $(".text-container").css("width", "100%");
            $(document).scrollTop(0);
        }
    }

});