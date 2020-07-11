$( document ).ready(function() {
var download = new RegExp('Downloading https:\/\/elib\.nlu\.org\.ua\/files\/Disk\d\/\/\d\d\d\d\d\d\d\d\d\d\d\d\/jpg\/\d\d\d\d\.jpg');
if ($("p:contains('creating djvu files...')").length>0 || $("p:contains('Creating final file...')").length>0  || $("p:contains('Deleting unnecessary crap')").length>0 || $("p:contains('All Done!')").length>0 || download.test($('.check').value)) {
if ($("p:contains('creating')").length>0) {
 $('.text-change').text('Converting');
 }
if ($("p:contains('!')").length>0) {
$('.text-change').text('Done');
$( "div.spinner-border" ).replaceWith( "<i class='fa fa-check fa-4x' aria-hidden='true'></i>");
$( '#visit' ).text('Download New Books');
$( '#visit' ).attr('href', '/');
}
}
else {
$('.alert-primary').attr('class', 'alert-danger');
$('.text-change').text('Oops, something went wrong!');
$( "div.spinner-border" ).replaceWith( "<i class='fa fa-warning fa-4x' aria-hidden='true'></i>");
$( '#visit' ).text('Try Again');
$( '#visit' ).attr('href', '/');

}
}
);