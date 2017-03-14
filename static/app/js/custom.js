$(document).ready(function() {

    //\\\\\\\\\\\\\\Panel Toolbox event
   $(document).on("click", ".collapse-link", function() {
        var a = $(this).closest(".x_panel")
          , b = $(this).find("i")
          , c = a.find(".x_content");
        a.attr("style") ? c.slideToggle(200, function() {
            a.removeAttr("style")
        }) : (c.slideToggle(200),
        a.css("height", "auto")),
        b.toggleClass("fa-chevron-up fa-chevron-down")
    }),

     $(document).on("click", ".close-link", function() {
        var a = $(this).closest(".panel-container");
        a.remove()
    })
    //\\\\\\\\\\\\\\END Panel Toolbox event


});//$(document).ready(function() {