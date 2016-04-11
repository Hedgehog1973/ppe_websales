/* Bootstrap Tabs Code */
$('#mainTab a').click(function(){
    $(this).tab('show');
})

// $('#mainTab a[href="#inicio"]').tab('show')
// $('#mainTab a[href="#reporte"]').tab('show')

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function navigatorFunction() {
    document.getElementsByClassName("topnav")[0].classList.toggle("responsive");
}