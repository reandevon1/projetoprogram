document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section-container');
    const discountButton = document.querySelector('.nav-btn-discount');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = button.getAttribute('data-target');
            const target = document.getElementById(targetId);

            sections.forEach(section => {
                section.classList.remove('visible');
                section.classList.add('hidden');
            });

            if (target) {
                target.classList.remove('hidden');
                target.classList.add('visible');
            }
        });
    });

    if (discountButton) {
        discountButton.addEventListener('click', function() {
            window.location.href = 'http://127.0.0.1:5000/';
        });
    }
});
