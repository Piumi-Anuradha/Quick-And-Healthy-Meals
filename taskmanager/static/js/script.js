  document.addEventListener('DOMContentLoaded', function() {
    // Initialize sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Initialize timepicker
    var timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker, {
        showView: 'minutes', // Specify the initial view to show (e.g., 'hours', 'minutes')
        i18n: {done:"Select"}
    });

    //Initializa Select
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});