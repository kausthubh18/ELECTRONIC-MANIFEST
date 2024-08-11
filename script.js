// Contact form handling
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    this.reset();
});

// Sidebar and Carousel interaction
$('.list-group-item').on('click', function () {
    var target = $(this).data('target');
    $('#galleryCarousel').carousel($(this).index());
    $('.list-group-item').removeClass('active');
    $(this).addClass('active');
});

$('#galleryCarousel').on('slide.bs.carousel', function (e) {
    var activeIndex = $(e.relatedTarget).index();
    $('.list-group-item').removeClass('active');
    $('.list-group-item').eq(activeIndex).addClass('active');
});
