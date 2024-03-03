$(document).ready(function(){


    $(".focus-trigger-login").focus(function(){
        changeView(1);
    });

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