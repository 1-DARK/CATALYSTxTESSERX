   // JavaScript for interactive elements
           document.addEventListener('DOMContentLoaded', function() {
            // Add animation class to social icons on page load
            const socialIcons = document.querySelectorAll('.social-icon');
           
            setTimeout(() => {
                socialIcons.forEach((icon, index) => {
                    setTimeout(() => {
                        icon.style.opacity = '0';
                        icon.style.transform = 'translateY(20px)';
                        icon.style.transition = 'all 0.3s ease';
                       
                        setTimeout(() => {
                            icon.style.opacity = '1';
                            icon.style.transform = 'translateY(0)';
                        }, 50);
                    }, index * 100);
                });
            }, 500);
           
            // Current year for copyright
            const year = new Date().getFullYear();
            document.querySelector('.footer-bottom p').innerHTML =
                `&copy; ${year} <a href="#"DiagnoAI</a>. All Rights Reserved.`;
        });
        document.addEventListener('DOMContentLoaded', function() {
            // Add animation class to social icons on page load
            const socialIcons = document.querySelectorAll('.social-icon');
           
            setTimeout(() => {
                socialIcons.forEach((icon, index) => {
                    setTimeout(() => {
                        icon.style.opacity = '0';
                        icon.style.transform = 'translateY(20px)';
                        icon.style.transition = 'all 0.3s ease';
                       
                        setTimeout(() => {
                            icon.style.opacity = '1';
                            icon.style.transform = 'translateY(0)';
                        }, 50);
                    }, index * 100);
                });
            }, 500);
           
            // Current year for copyright
            const year = new Date().getFullYear();
            document.querySelector('.footer-bottom p').innerHTML =
                `&copy; ${year} <a href="#">DiagnoAI</a>. All Rights Reserved.`;
        });