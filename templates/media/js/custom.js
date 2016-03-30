jQuery(document).ready(function() {


    $('.stripe-button-el').addClass('btn btn-lg btn-danger');
    $('.stripe-button-el').text('Stripe');
    $('.stripe-button-el').removeClass('stripe-button-el');

    $("#submitPayment").on("click", function () {
        var btn = $(this).button("loading")
        setTimeout(function () {
            btn.button('reset');
        }, 3500)
    });


    $(".hideeeee").click(function () {
        $('.get_none').show();
        $('.rules_data').hide();
        $('.hideeeee').hide();
        $('.jumbotron').hide();
        $('.canceleledd').show();
        $('.cancelele').hide();
        //$('.paypal.is-active').css("border-radius", '0px');
        $('.paypal.is-active').css("background-color", "lightblue");
    });

    $(".canceleledd").click(function () {
        $('.get_none').hide();
        $('.rules_data').show();
        $('.hideeeee').show();
        $('.jumbotron').show();
        $('.canceleledd').hide();
        $('.cancelele').show();
    })

});