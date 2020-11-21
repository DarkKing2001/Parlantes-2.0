document.addEventListener('DOMContentLoaded', () => {
    const elems = document.querySelectorAll('.carousel');
    M.Carousel.init(elems, {
        duration: 1500,
        dist: -88,
        shift: 5,
        padding: 5,
        numVisible: 5,
        indicators: true
    });
});

//navBar

//const elemsDropdown = document.querySelectorAll(".dropdown-trigger");
//const instanceDropdown = M.Dropdown.init(elemsDropdown);

//document.addEventListener('DOMContentLoaded', function() {
//    var elems = document.querySelectorAll('select');
//    var instances = M.FormSelect.init(elems, options);
//});

$(document).ready(function(){
   $('select').formSelect();
});