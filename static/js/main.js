$(document).ready(function () {
  /* added so flashed messages disappear after ten seconds */
  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);
  // this will hide an show the comments
  $(".comments-btn").click(function () {
    $(".comments").toggle();
  });
});
