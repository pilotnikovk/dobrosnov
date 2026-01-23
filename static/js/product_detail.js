document.addEventListener('DOMContentLoaded', function() {
    // Переключение изображений в галерее
    const mainImage = document.getElementById('main-product-image');
    const thumbnails = document.querySelectorAll('.thumbnail');
    
    if (thumbnails.length > 0) {
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', function() {
                // Удаляем active у всех миниатюр
                thumbnails.forEach(t => t.classList.remove('active'));
                
                // Добавляем active к текущей
                this.classList.add('active');
                
                // Меняем основное изображение
                mainImage.src = this.src;
                mainImage.alt = this.alt;
            });
        });
    }
    
    // Управление количеством товара
    const minusBtn = document.querySelector('.quantity-btn.minus');
    const plusBtn = document.querySelector('.quantity-btn.plus');
    const quantityInput = document.querySelector('.quantity-input');
    
    if (minusBtn && plusBtn && quantityInput) {
        minusBtn.addEventListener('click', function() {
            let value = parseInt(quantityInput.value);
            if (value > 1) {
                quantityInput.value = value - 1;
            }
        });
        
        plusBtn.addEventListener('click', function() {
            let value = parseInt(quantityInput.value);
            quantityInput.value = value + 1;
        });
    }
    
    // Переключение табов
    const tabNavItems = document.querySelectorAll('.tabs-nav li');
    const tabPanes = document.querySelectorAll('.tab-pane');
    
    if (tabNavItems.length > 0 && tabPanes.length > 0) {
        tabNavItems.forEach(item => {
            item.addEventListener('click', function() {
                const tabId = this.getAttribute('data-tab');
                
                // Удаляем active у всех элементов навигации
                tabNavItems.forEach(navItem => navItem.classList.remove('active'));
                
                // Добавляем active к текущему
                this.classList.add('active');
                
                // Скрываем все табы
                tabPanes.forEach(pane => pane.classList.remove('active'));
                
                // Показываем нужный таб
                document.getElementById(tabId).classList.add('active');
            });
        });
    }
    
    // Добавление в корзину
    const addToCartBtn = document.querySelector('.add-to-cart');
    if (addToCartBtn) {
        addToCartBtn.addEventListener('click', function() {
            const productId = window.location.pathname.split('/').filter(Boolean).pop();
            const quantity = parseInt(quantityInput.value);
            
            // Здесь можно добавить AJAX-запрос для добавления в корзину
            console.log(`Добавлено в корзину: товар ${productId}, количество ${quantity}`);
            
            // Временное уведомление
            const notification = document.createElement('div');
            notification.className = 'cart-notification';
            notification.innerHTML = `
                <i class="fas fa-check-circle"></i>
                <span>Товар добавлен в корзину</span>
            `;
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.classList.add('show');
            }, 10);
            
            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => {
                    document.body.removeChild(notification);
                }, 300);
            }, 3000);
        });
    }
    
    // Добавление отзыва
    const addReviewBtn = document.querySelector('.add-review-btn');
    if (addReviewBtn) {
        addReviewBtn.addEventListener('click', function() {
            // Здесь можно реализовать форму добавления отзыва
            alert('Форма добавления отзыва будет реализована позже');
        });
    }
});