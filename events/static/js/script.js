//imitialize slider
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
       speed: 500,
      autoplay: {
        delay: 3500, // slide after 3.5 seconds
        disableOnInteraction: false,
      },
    });
  });

//Scroll to the top button
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
  // mobile menu toggle
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
  //Menu dropdown show and hide on hove
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


   // Get references to the ticket type and quantity fields
    const ticketTypeSelect = document.getElementById("id_ticket_type");
    const quantityInput = document.getElementById("id_number_of_tickets");
    const totalPriceSpan = document.getElementById("total_price");

    // Calculate total price whenever the ticket type or quantity is changed
    function updateTotalPrice() {
        const ticketTypeId = ticketTypeSelect.value;
        const quantity = quantityInput.value;

        // Make an AJAX call to fetch the ticket price based on the selected type
        fetch(`/get_ticket_price/${ticketTypeId}/`)
            .then(response => response.json())
            .then(data => {
                const totalPrice = data.price * quantity;
                totalPriceSpan.textContent = `${totalPrice} KSH`;
            });
    }

    // Add event listeners to update total price on changes
    ticketTypeSelect.addEventListener('change', updateTotalPrice);
    quantityInput.addEventListener('input', updateTotalPrice);

    // Initial update on page load
    updateTotalPrice();
