
function show_loading_for_redirect(params) {
    const loading = document.getElementById("loadingOverlay")
    loading.style.display = "flex";
}

function hide_loading(params) {
    const loading = document.getElementById("loadingOverlay")
    loading.style.display = "none";
}

jQuery(function ($) {
    $('.community-slider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        autoplay: true,
        autoplaySpeed: 1000,
        speed: 1000
    });

    $("#header .toggle").click(function () {
        $(".sidebar").toggleClass("active");
    });

    $(".toggle-gen-sidebar").click(function () {
        $(this).parent().toggleClass("active");
    })

    $(".panel-btn.toggle").click(function () {
        $(this).find("p").slideToggle();
    })
    $(".style-box .panel-btn").click(function (e) {
        e.stopPropagation()
        $(this).next().toggleClass("active");
    })
    $(".style-dropdown").click(function (e) {
        e.stopPropagation()
    })
    $(window).click(function (e) {
        $(".style-dropdown").removeClass("active");
    })
    
    $(".panel-btn.toggle p").click(function (e) {
        e.stopPropagation()
    })

    // Add event listener to range input
    $('#image-count').on('input', function() {
        // Get the current value of the range input
        var count = $(this).val();
        // Update the count display element
        $('#image-count-display').text(count);
    });
    $('#image-count-display').text($('#image-count').val());

})


