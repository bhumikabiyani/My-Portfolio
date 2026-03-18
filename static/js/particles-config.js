// ============================================
// Lightweight Particle Animation (Pure JS Canvas)
// No external library needed
// ============================================

(function () {
  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particles = [];
  let animationId;
  let mouse = { x: null, y: null, radius: 120 };

  function resize() {
    const hero = canvas.parentElement;
    canvas.width = hero.offsetWidth;
    canvas.height = hero.offsetHeight;
  }

  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 2 + 0.5;
      this.speedX = (Math.random() - 0.5) * 0.6;
      this.speedY = (Math.random() - 0.5) * 0.6;
      this.opacity = Math.random() * 0.5 + 0.1;
      this.color = Math.random() > 0.7 ? 'rgba(255, 189, 57,' : 'rgba(255, 255, 255,';
    }

    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      // Wrap around edges
      if (this.x > canvas.width) this.x = 0;
      if (this.x < 0) this.x = canvas.width;
      if (this.y > canvas.height) this.y = 0;
      if (this.y < 0) this.y = canvas.height;

      // Mouse interaction
      if (mouse.x !== null) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          const force = (mouse.radius - dist) / mouse.radius;
          this.x -= dx * force * 0.02;
          this.y -= dy * force * 0.02;
        }
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color + this.opacity + ')';
      ctx.fill();
    }
  }

  function initParticles() {
    particles = [];
    const count = Math.min(Math.floor((canvas.width * canvas.height) / 8000), 120);
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function connectParticles() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 100) {
          const opacity = (1 - dist / 100) * 0.15;
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(255, 189, 57,' + opacity + ')';
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    connectParticles();
    animationId = requestAnimationFrame(animate);
  }

  // Mouse tracking (relative to the canvas)
  canvas.parentElement.addEventListener('mousemove', function (e) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });

  canvas.parentElement.addEventListener('mouseleave', function () {
    mouse.x = null;
    mouse.y = null;
  });

  // Initialize
  window.addEventListener('resize', function () {
    resize();
    initParticles();
  });

  resize();
  initParticles();
  animate();
})();


// ============================================
// Typing Text Effect
// ============================================
(function () {
  const elements = document.querySelectorAll('.typing-text');
  if (!elements.length) return;

  const combinedTexts = [
    'Software Developer',
    'Full-Stack Engineer',
    'AI/ML Enthusiast',
    'React Native Developer',
    'Build Mobile Apps',
    'Build Scalable Systems',
    'NodeJS Developer',
    'Golang Developer',
    'Python Developer',
    'React Developer',
  ];

  elements.forEach((el) => {
    const texts = combinedTexts;
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let speed = 80;

    function type() {
      const current = texts[textIndex];

      if (isDeleting) {
        el.textContent = current.substring(0, charIndex - 1);
        charIndex--;
        speed = 40;
      } else {
        el.textContent = current.substring(0, charIndex + 1);
        charIndex++;
        speed = 80;
      }

      if (!isDeleting && charIndex === current.length) {
        speed = 2000; // pause at full text
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textIndex = (textIndex + 1) % texts.length;
        speed = 400; // pause before next word
      }

      setTimeout(type, speed);
    }

    type();
  });
})();


// ============================================
// Scroll to Top Button
// ============================================
(function () {
  const btn = document.getElementById('scroll-to-top');
  if (!btn) return;

  window.addEventListener('scroll', function () {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  });

  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();


// ============================================
// Cursor Glow Effect
// ============================================
(function () {
  const glow = document.getElementById('cursor-glow');
  if (!glow) return;

  // Only enable on non-touch devices
  if ('ontouchstart' in window) return;

  document.addEventListener('mousemove', function (e) {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
    glow.classList.add('active');
  });

  document.addEventListener('mouseleave', function () {
    glow.classList.remove('active');
  });
})();


// ============================================
// Animate Stats Counters on Scroll
// ============================================
(function () {
  const counters = document.querySelectorAll('.stat-counter');
  if (!counters.length) return;

  let animated = false;

  function animateCounters() {
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-target'));
      const duration = 2000;
      const step = target / (duration / 16);
      let current = 0;

      function update() {
        current += step;
        if (current >= target) {
          counter.textContent = target;
          return;
        }
        counter.textContent = Math.floor(current);
        requestAnimationFrame(update);
      }
      update();
    });
  }

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        animateCounters();
      }
    });
  }, { threshold: 0.3 });

  const statsSection = document.getElementById('stats-section');
  if (statsSection) observer.observe(statsSection);
})();
