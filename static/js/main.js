/**
* Template Name: FlexStart - v1.12.0
* Template URL: https://bootstrapmade.com/flexstart-bootstrap-startup-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach(e => e.addEventListener(type, listener))
    } else {
      select(el, all).addEventListener(type, listener)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 10
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        aos_init();
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfokio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40
      },

      1200: {
        slidesPerView: 3,
      }
    }
  });

  /**
   * Animation on scroll
   */
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', () => {
    aos_init();
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

})();


document.getElementById('copy-button12').addEventListener('click', function() {
  var textToCopy1 = " A scary house in jungle, dark, detailed, cinematic, oil painting style, HD, 16K";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    innerHTML('Text copied to clipboard');
  }, function() {
    innerHTML('Failed to copy text to clipboard');
  });
});

document.getElementById('copy-button11').addEventListener('click', function() {
  var textToCopy1 = "An illustration of an ancient big portal with magic symbol, open to the cosmos, starry sky , mountains";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button10').addEventListener('click', function() {
  var textToCopy1 = "Photorealistic landscape beautiful lighting crashed spaceship mountains forest dark";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button9').addEventListener('click', function() {
  var textToCopy1 = "A medieval village in switzerland, ornate, beautiful, atmosphere, vibe, flowers, concept art illustration, greg rutowski, volumetric lighting, sunbeams, particles";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button8').addEventListener('click', function() {
  var textToCopy1 = "Ethereal autumn leaves goddess, epic, intricate character portrait, intricate, beautyful, 8k resolution, dynamic lighting, hyperdetailed, quality 3D rendered, volumetric lighting, greg rutkowski, oil on canvas, detailed background, artstation character portrait, dnd character portrait";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button7').addEventListener('click', function() {
  var textToCopy1 = "A mystical castle in the clouds with a rainbow bridge leading up to it 4K, trending on artstation, sharp focus, studio photo, intricate details, highly detailed ";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button6').addEventListener('click', function() {
  var textToCopy1 = "mystical river";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button5').addEventListener('click', function() {
  var textToCopy1 = "A painting of a beautiful futuristic city in synth retrowave.";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button4').addEventListener('click', function() {
  var textToCopy1 = "Two unicorns talking ultra realistic 4k";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button3').addEventListener('click', function() {
  var textToCopy1 = "Kneeling cat knight, portrait, finely detailed armor, intricate design, silver, silk, cinematic lighting, 4k";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button2').addEventListener('click', function() {
  var textToCopy1 = "Astronaut surfing in space";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button1').addEventListener('click', function() {
  var textToCopy1 = "Painting of anime style  Champs-Élysées Eiffel tower autumn  with a row of trees fountain and the sun rays coming through the leaves. Makoto Shinkai. Soft lighting, outdoor environment, vibrant colors, front view. desktop wallpaper ";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button13').addEventListener('click', function() {
  var textToCopy1 = "A sunken ship resting on the ocean floor with marine life growing around it.";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button14').addEventListener('click', function() {
  var textToCopy1 = "A magical forest with glowing mushrooms and mischievous fairies flitting between the trees, highly detailed, cinematics, 8K";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});
document.getElementById('copy-button15').addEventListener('click', function() {
  var textToCopy1 = "A fantastical landscape with floating islands and waterfalls cascading between them ,highly detailed, cinematics, 8K, desktop wallpaper ";
  navigator.clipboard.writeText(textToCopy1).then(function() {
    console.log('Text copied to clipboard');
  }, function() {
    console.error('Failed to copy text to clipboard');
  });
});

