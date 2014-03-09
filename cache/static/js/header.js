$(document).ready(function() {
    $(".nav >li").hover(function() {
        $(this).children("ul").addClass("active");
    },function(){
        $(this).children("ul").removeClass ("active");
    });
});
    function addHoverCss() {
        jQuery("body tr").hover(function () {
            jQuery(this).addClass("hover");
        }, function () {
            jQuery(this).removeClass("hover");
        });
    }




