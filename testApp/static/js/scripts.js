$(function() {
    $( window ).scroll(function() {
        if($(this).scrollTop() != 0) {
            $('#toTop').fadeIn();
        }
        else {
            $('#toTop').fadeOut();
        }
    });


    $('#toTop').click(function() {
        $('body,html').animate({scrollTop:0},800);
    });


    $( document ).ready(function() {
        $('.full-image__paralax-image').parallax("50%", 0.3);
    });


    $( ".product__link" ).click(function() {
        $('.background-overlay').addClass('active');
        $('.feature-products__popup').addClass('active');
        return false
    });
    $( ".popup__close" ).click(function() {
        $('.background-overlay').removeClass('active');
        $('.feature-products__popup').removeClass('active');
        return false
    });

});