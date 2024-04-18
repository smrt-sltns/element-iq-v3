
function show_loading_for_redirect(params) {
    const loading = document.getElementById("loadingOverlay")
    loading.style.display = "flex";
}

function hide_loading(params) {
    const loading = document.getElementById("loadingOverlay")
    loading.style.display = "none";
}

jQuery(function($){
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
})


