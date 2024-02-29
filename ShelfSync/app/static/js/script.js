$(document).ready(function(){

    $(".focus-trigger-login").focus(function(){
        changeView(1);
    });

    $(".focus-trigger-search").focus(function(){
         changeView(2);
    });


    /*$(".typing-seach").on("input", function(){
            $.ajax({
                url: "/api/resources",
                type: "POST",
                success: function(data){
                    $("#temp-id").text(data)
                },
                error: function(err){
                    console.log(err)
                }
            });
    });
*/

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