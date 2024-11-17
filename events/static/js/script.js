document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper('.swiper', {
      loop: true,
      slidesPerView: 1, // Adjust number of slides per view
      spaceBetween: 10,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      autoplay: {
        delay: 3000, // 3 seconds
        disableOnInteraction: false,
      },
    });
  });
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: "smooth", // Smooth scrolling effect
    });
  }
  //darkmode toggle
  function darkmode() {
    document.body.classList.toggle("darkmode");
  }
  
  function menutoggle() {
    const hamburgerIcon = document.getElementById("hamburgerIcon");
    menu = document.querySelector(".menu-content");
    menu.classList.toggle("hidden");
    if (menu.classList.contains("hidden")) {
      hamburgerIcon.classList.remove("fa-times");
      hamburgerIcon.classList.add("fa-bars");
    } else {
      hamburgerIcon.classList.remove("fa-bars");
      hamburgerIcon.classList.add("fa-times");
    }
  }
  
  const dropdown = document.getElementById("dropdown");
  const dropdownItems = document.getElementById("dropdown-items");
  dropdown.addEventListener("mouseover", hover);
  dropdown.addEventListener("mouseleave", hoverhide);
  dropdownItems.addEventListener("mouseover", hover);
  dropdownItems.addEventListener("mouseleave", hoverhide);
  function hoverhide() {
    dropdownItems.classList.add("hidden");
  }
  function hover() {
    dropdownItems.classList.toggle("hidden");
  }
  