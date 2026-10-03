document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const menuBtn = document.querySelector(".menu-btn");
  const navLinks = document.querySelectorAll("#nav a");
  const sections = document.querySelectorAll("main section[id]");

  if (menuBtn) {
    menuBtn.addEventListener("click", () => {
      const open = body.classList.toggle("menu-open");
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.textContent = open ? "×" : "☰";
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      body.classList.remove("menu-open");
      if (menuBtn) {
        menuBtn.setAttribute("aria-expanded", "false");
        menuBtn.textContent = "☰";
      }
    });
  });

  function updateActive() {
    let current = "home";
    const y = window.scrollY + 180;

    sections.forEach((section) => {
      if (
        y >= section.offsetTop &&
        y < section.offsetTop + section.offsetHeight
      ) {
        current = section.id;
      }
    });

    navLinks.forEach((link) => {
      link.classList.toggle(
        "active",
        link.getAttribute("href") === "#" + current,
      );
    });
  }

  window.addEventListener("scroll", updateActive, { passive: true });
  updateActive();

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      e.preventDefault();

      window.scrollTo({
        top: target.offsetTop - 70,
        behavior: "smooth",
      });
    });
  });
});
