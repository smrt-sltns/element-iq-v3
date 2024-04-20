
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

      $("#header .toggle").click(function(){
        $(".sidebar").toggleClass("active");
      });

      $(".toggle-gen-sidebar").click(function(){
        $(this).parent().toggleClass("active");
      })

      $(".panel-btn.toggle").click(function(){
        $(this).find("p").slideToggle();
      })

      $(".panel-btn.toggle p").click(function(e){
        e.stopPropagation()
      })
})


