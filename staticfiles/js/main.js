// GoHerbal JavaScript

$(document).ready(function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if( target.length ) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 100
            }, 1000);
        }
    });

    // Add to cart functionality
    $('.add-to-cart-btn').on('click', function(e) {
        e.preventDefault();
        var $btn = $(this);
        var originalHtml = $btn.html();
        
        // Show loading state
        $btn.html('<i class="fas fa-spinner fa-spin"></i>');
        $btn.prop('disabled', true);
        
        // Simulate API call
        setTimeout(function() {
            // Show success state
            $btn.html('<i class="fas fa-check"></i>');
            $btn.removeClass('btn-light btn-outline-primary').addClass('btn-success');
            
            // Update cart count (simulate)
            var currentCount = parseInt($('#cart-count').text()) || 0;
            $('#cart-count').text(currentCount + 1);
            
            // Reset button after 2 seconds
            setTimeout(function() {
                $btn.html(originalHtml);
                $btn.removeClass('btn-success').addClass('btn-light');
                $btn.prop('disabled', false);
            }, 2000);
        }, 1000);
    });

    // Search functionality
    $('#product-search').on('input', function() {
        var query = $(this).val();
        if (query.length > 2) {
            // Simulate search suggestions
            console.log('Searching for:', query);
        }
    });

    // Quantity selector
    $('.quantity-btn').on('click', function() {
        var $input = $(this).siblings('input[type="number"]');
        var currentVal = parseInt($input.val()) || 1;
        var min = parseInt($input.attr('min')) || 1;
        var max = parseInt($input.attr('max')) || 999;
        
        if ($(this).hasClass('quantity-plus') && currentVal < max) {
            $input.val(currentVal + 1);
        } else if ($(this).hasClass('quantity-minus') && currentVal > min) {
            $input.val(currentVal - 1);
        }
    });

    // Image gallery
    $('.thumbnail-img').on('click', function() {
        var newSrc = $(this).attr('src');
        $('#main-product-image').attr('src', newSrc);
        $('.thumbnail-img').removeClass('active');
        $(this).addClass('active');
    });

    // Form validation
    $('form').on('submit', function(e) {
        var isValid = true;
        
        $(this).find('input[required], select[required], textarea[required]').each(function() {
            if (!$(this).val()) {
                isValid = false;
                $(this).addClass('is-invalid');
            } else {
                $(this).removeClass('is-invalid');
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            alert('Please fill in all required fields.');
        }
    });

    // Auto-hide alerts
    $('.alert').delay(5000).fadeOut();

    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Back to top button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });

    $('#back-to-top').click(function() {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
});

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function showNotification(message, type = 'success') {
    const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
    const notification = `
        <div class="alert ${alertClass} alert-dismissible fade show position-fixed" 
             style="top: 20px; right: 20px; z-index: 9999;">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    $('body').append(notification);
    
    setTimeout(() => {
        $('.alert').fadeOut();
    }, 3000);
}

// AJAX setup for Django CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});