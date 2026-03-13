// ============================================
// PRECISION TRADER SYSTEM — SALES PAGE JS
// ============================================

(function () {
  'use strict';

  // --- STICKY CTA BAR (Mobile Only) ---
  const stickyCta = document.getElementById('stickyCta');
  const heroCtaBtn = document.querySelector('.hero__cta');

  if (stickyCta && heroCtaBtn) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            stickyCta.classList.remove('is-visible');
            document.body.classList.remove('has-sticky-cta');
          } else {
            // Only show on mobile
            if (window.innerWidth <= 768) {
              stickyCta.classList.add('is-visible');
              document.body.classList.add('has-sticky-cta');
            }
          }
        });
      },
      { threshold: 0 }
    );
    observer.observe(heroCtaBtn);

    // Also hide sticky when any CTA card is visible
    var ctaCards = document.querySelectorAll('.cta-card');
    ctaCards.forEach(function (card) {
      var cardObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting && window.innerWidth <= 768) {
              stickyCta.classList.remove('is-visible');
              document.body.classList.remove('has-sticky-cta');
            }
          });
        },
        { threshold: 0.3 }
      );
      cardObserver.observe(card);
    });
  }

  // --- VSL PLAYER ---
  // Replace thumbnail with actual video embed on click
  var vslPlayer = document.getElementById('vsl');
  if (vslPlayer) {
    vslPlayer.addEventListener('click', function () {
      // Replace YOUR_VIDEO_EMBED_URL with your Wistia/Vimeo embed URL
      var embedUrl = 'YOUR_VIDEO_EMBED_URL';

      if (embedUrl === 'YOUR_VIDEO_EMBED_URL') {
        // If no embed URL set, just log a message
        console.log('Set your video embed URL in script.js');
        return;
      }

      var iframe = document.createElement('iframe');
      iframe.src = embedUrl + '?autoplay=1';
      iframe.setAttribute('frameborder', '0');
      iframe.setAttribute('allow', 'autoplay; fullscreen');
      iframe.setAttribute('allowfullscreen', '');
      iframe.style.position = 'absolute';
      iframe.style.top = '0';
      iframe.style.left = '0';
      iframe.style.width = '100%';
      iframe.style.height = '100%';

      vslPlayer.innerHTML = '';
      vslPlayer.style.position = 'relative';
      vslPlayer.appendChild(iframe);
    });
  }

  // --- SMOOTH SCROLL for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
