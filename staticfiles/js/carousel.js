document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.hero-carousel');
    const slides = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.querySelector('.carousel-control.prev');
    const nextBtn = document.querySelector('.carousel-control.next');
    let currentSlide = 0;
    const slideCount = slides.length;
    
    // Инициализация карусели
    function initCarousel() {
        if (slideCount > 0) {
            slides[0].classList.add('active');
            
            // Автопереключение слайдов
            setInterval(() => {
                goToNextSlide();
            }, 5000);
        }
    }
    
    // Переключение на следующий слайд
    function goToNextSlide() {
        goToSlide((currentSlide + 1) % slideCount);
    }
    
    // Переключение на предыдущий слайд
    function goToPrevSlide() {
        goToSlide((currentSlide - 1 + slideCount) % slideCount);
    }
    
    // Переключение на конкретный слайд
    function goToSlide(slideIndex) {
        slides[currentSlide].classList.remove('active');
        currentSlide = slideIndex;
        slides[currentSlide].classList.add('active');
    }
    
    // Обработчики событий для кнопок
    prevBtn.addEventListener('click', goToPrevSlide);
    nextBtn.addEventListener('click', goToNextSlide);
    
    // Инициализация
    initCarousel();
});