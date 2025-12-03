/**
 * SaveToWaybackMachine - Lightbox functionality
 * WCAG 2.1 Level AA accessible image viewer
 */

(function() {
  'use strict';

  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxCounter = document.querySelector('.lightbox-counter');
  const closeBtn = document.querySelector('.lightbox-close');
  const prevBtn = document.querySelector('.lightbox-prev');
  const nextBtn = document.querySelector('.lightbox-next');

  let galleryImages = [];
  let currentIndex = 0;
  let previouslyFocusedElement = null;

  /**
   * Get caption for an image from table header or alt text
   * @param {HTMLImageElement} img - The image element
   * @returns {string} Caption text
   */
  function getCaption(img) {
    const cell = img.closest('td');
    if (cell) {
      const cellIndex = Array.from(cell.parentNode.children).indexOf(cell);
      const headerRow = cell.closest('table').querySelector('thead tr, tr:first-child');
      if (headerRow) {
        const headerCell = headerRow.children[cellIndex];
        if (headerCell) {
          return headerCell.textContent;
        }
      }
    }
    if (img.alt) return img.alt;
    const src = img.src;
    const filename = src.substring(src.lastIndexOf('/') + 1);
    return filename.replace(/\.[^/.]+$/, '').replace(/[-_]/g, ' ');
  }

  /**
   * Show image at specified index
   * @param {number} index - Index in galleryImages array
   */
  function showImage(index) {
    if (index < 0) index = galleryImages.length - 1;
    if (index >= galleryImages.length) index = 0;
    currentIndex = index;
    const img = galleryImages[index];
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt || getCaption(img);
    lightboxCaption.textContent = getCaption(img);
    lightboxCounter.textContent = (currentIndex + 1) + ' / ' + galleryImages.length;
  }

  /**
   * Open lightbox with specified image
   * @param {HTMLImageElement} img - The image to display
   */
  function openLightbox(img) {
    previouslyFocusedElement = document.activeElement;
    galleryImages = Array.from(document.querySelectorAll('.content img:not(.nav-card img)'));
    currentIndex = galleryImages.indexOf(img);
    if (currentIndex === -1) currentIndex = 0;
    lightbox.classList.add('active');
    showImage(currentIndex);
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  /**
   * Close lightbox and restore focus
   */
  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
    if (previouslyFocusedElement) {
      previouslyFocusedElement.focus();
    }
  }

  /**
   * Trap focus within lightbox for accessibility
   * @param {KeyboardEvent} e - Keyboard event
   */
  function trapFocus(e) {
    if (!lightbox.classList.contains('active')) return;

    const focusableElements = lightbox.querySelectorAll('button');
    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    if (e.shiftKey && document.activeElement === firstFocusable) {
      e.preventDefault();
      lastFocusable.focus();
    } else if (!e.shiftKey && document.activeElement === lastFocusable) {
      e.preventDefault();
      firstFocusable.focus();
    }
  }

  // Initialize clickable images
  document.querySelectorAll('.content img:not(.nav-card img)').forEach(function(img) {
    img.setAttribute('tabindex', '0');
    img.setAttribute('role', 'button');
    img.setAttribute('aria-label', 'Open image: ' + (img.alt || 'gallery image'));

    img.addEventListener('click', function() {
      openLightbox(this);
    });

    img.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(this);
      }
    });
  });

  // Navigation button handlers
  prevBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    showImage(currentIndex - 1);
  });

  nextBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    showImage(currentIndex + 1);
  });

  closeBtn.addEventListener('click', closeLightbox);

  // Close on background click
  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (!lightbox.classList.contains('active')) return;

    if (e.key === 'Escape') {
      closeLightbox();
    } else if (e.key === 'ArrowLeft') {
      showImage(currentIndex - 1);
    } else if (e.key === 'ArrowRight') {
      showImage(currentIndex + 1);
    } else if (e.key === 'Tab') {
      trapFocus(e);
    }
  });

  // Touch/swipe support
  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;

  lightbox.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  lightbox.addEventListener('touchend', function(e) {
    touchEndX = e.changedTouches[0].screenX;
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
  }, { passive: true });

  /**
   * Handle swipe gestures for navigation
   */
  function handleSwipe() {
    const swipeThreshold = 50;
    const diffX = touchEndX - touchStartX;
    const diffY = touchEndY - touchStartY;

    if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > swipeThreshold) {
      if (diffX > 0) {
        showImage(currentIndex - 1);
      } else {
        showImage(currentIndex + 1);
      }
    }
  }
})();

// Native lazy loading for all images
document.querySelectorAll('img').forEach(function(img) {
  if (!img.hasAttribute('loading')) {
    img.setAttribute('loading', 'lazy');
  }
});
