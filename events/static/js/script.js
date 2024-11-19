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
    // Toggle the dark mode class on the body
    document.body.classList.toggle("darkmode");

    // Save the user's preference to localStorage
    if (document.body.classList.contains("darkmode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Apply the saved theme on page load
function applyTheme() {
    const savedTheme = localStorage.getItem("theme");
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;

    if (savedTheme === "dark" || (!savedTheme && prefersDarkScheme)) {
        document.body.classList.add("darkmode");
    } else {
        document.body.classList.remove("darkmode");
    }
}
// Run applyTheme on page load
applyTheme();

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


document.addEventListener("DOMContentLoaded", function () {
    const userDropdown = document.getElementById("user-dropdown");
    const dropdownItems = document.getElementById("user-dropdown-items");
     userDropdown.addEventListener("click", function (e) {
        e.stopPropagation(); // Prevent clicking elsewhere from closing immediately
        dropdownItems.classList.toggle("hidden");
    });
    // Close dropdown when clicking outside
    document.addEventListener("click", function () {
        dropdownItems.classList.add("hidden");
    });
});
//tickets add for user
document.addEventListener("DOMContentLoaded", () => {
    const addTicketButton = document.getElementById("add-ticket");
    const ticketFormsContainer = document.getElementById("ticket-forms");
    const totalForms = document.getElementById("id_form-TOTAL_FORMS"); // Hidden field tracking total forms
    const emptyFormTemplate = ticketFormsContainer.dataset.emptyForm;

    // Add a new ticket form
    addTicketButton.addEventListener("click", () => {
        const currentFormCount = parseInt(totalForms.value, 10); // Current form count
        const newFormHtml = emptyFormTemplate.replace(/__prefix__/g, currentFormCount);
        const newForm = document.createElement("div");
        newForm.classList.add("ticket-form");
        newForm.innerHTML = `
            <h3>Ticket ${currentFormCount + 1}</h3>
            ${newFormHtml}
            <button type="button" class="delete-ticket">Delete Ticket</button>
        `;
        ticketFormsContainer.appendChild(newForm);
        totalForms.value = currentFormCount + 1; // Increment form count
    });

    // Delete a ticket form
    ticketFormsContainer.addEventListener("click", (e) => {
        if (e.target.classList.contains("delete-ticket")) {
            const ticketForm = e.target.closest(".ticket-form");
            if (ticketForm) ticketForm.remove();
        }
    });
});