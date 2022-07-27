jQuery(document).ready(function(){
    var scrollvalue =jQuery(".first-container").offset().top;
    jQuery(window).scroll(function(){
        var scrollPos =jQuery(window).scrollTop();

        if(scrollPos>=scrollvalue-95){
            jQuery("nav").removeClass("bg-transparent");
            jQuery("nav").addClass("bg-dark");

            

        }else{
            jQuery("nav").addClass("bg-transparent");
            jQuery("nav").removeClass("bg-dark")

        }  
    }); 

   
});