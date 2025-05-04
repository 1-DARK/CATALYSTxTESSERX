document.addEventListener('DOMContentLoaded', function() {
    const toggler = document.querySelector('.navbar-toggler');
    const navbarLinks = document.querySelector('.navbar-links');
    const links = document.querySelectorAll('.navbar-links a');
    
    // Toggle menu on button click
    toggler.addEventListener('click', function() {
        const isExpanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !isExpanded);
        navbarLinks.classList.toggle('active');
    });
    
    // Close menu when a link is clicked (for mobile)
    links.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                toggler.setAttribute('aria-expanded', 'false');
                navbarLinks.classList.remove('active');
            }
        });
    });
    
    // Close menu when clicking outside (optional)
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768 && 
            !navbarLinks.contains(e.target) && 
            !toggler.contains(e.target)) {
            toggler.setAttribute('aria-expanded', 'false');
            navbarLinks.classList.remove('active');
        }
    });
    
    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            toggler.setAttribute('aria-expanded', 'false');
            navbarLinks.classList.remove('active');
        }
    });
});
