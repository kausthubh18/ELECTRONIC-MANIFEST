// Contact form handling
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    this.reset(); // Resets the form fields
});

// Sidebar and Carousel interaction
$(document).ready(function() {
    // When a sidebar item is clicked
    $('.list-group-item').on('click', function () {
        var targetIndex = $(this).data('target'); // Get the target index from the data attribute
        $('#galleryCarousel').carousel(targetIndex); // Move the carousel to the target index
        $('.list-group-item').removeClass('active'); // Remove active class from all sidebar items
        $(this).addClass('active'); // Add active class to the clicked sidebar item
    });

    // When the carousel slides
    $('#galleryCarousel').on('slide.bs.carousel', function (e) {
        var activeIndex = $(e.relatedTarget).index(); // Get the index of the new active slide
        $('.list-group-item').removeClass('active'); // Remove active class from all sidebar items
        $('.list-group-item').eq(activeIndex).addClass('active'); // Add active class to the sidebar item corresponding to the new active slide
    });
});
