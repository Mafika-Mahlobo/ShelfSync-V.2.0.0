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
    })



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