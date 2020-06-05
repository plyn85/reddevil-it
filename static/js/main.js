$(document).ready(function () {
  /* added so flashed messages disappear after ten seconds */

  setTimeout(function () {
    $("#flashed-message").hide("slow");
  }, 10000);

  /* this will hide an show the comments */
  $(".comments-btn").click(function () {
    $(".comments").toggle();
  });

  /* adding ajax for like button 
   taken from a tutorial at https://www.youtube.com/watch?v=pkPRtQf6oQ8&t=678s */

  /*  function added here then passed into success function update text when like/unlike button clicked */

  function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb);
    // this prevents num of likes displaying as a negitive value
    btn.attr("data-likes", newCount);
  }

  $(".like-btn").click(function (e) {
    // prevent default behaviour of the button
    e.preventDefault();
    // this is the .like-btn class
    var this_ = $(this);
    // adding get_like_api_url to variable
    var likeUrl = this_.attr("data-href");
    // getiing the likes count and changing it to a variable
    var likeCount = parseInt(this_.attr("data-likes"));

    if (likeUrl) {
      $.ajax({
        url: likeUrl,
        method: "GET",
        data: {},
        success: function (data) {
          console.log(data);
          var newLikes;
          if (data.liked) {
            //add one like
            var newLikes = likeCount + 1;
            updateText(this_, newLikes, "unlike");
          } else {
            // remove one like
            var newLikes = likeCount - 1;
            updateText(this_, newLikes, "like");
          }
        },
        error: function (error) {
          console.log(error);
          console.log("error");
        },
      });
    }
  });
  // overriding default carousel speed
  $(".carousel").carousel({
    interval: 2500,
  });

  /* The following function are copying from
   https://docs.djangoproject.com/en/dev/ref/csrf/#ajax 
   Its being used to set make csrf token across all pages*/
  function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getToken("csrftoken");

  /* the following was taken from https://tutorialebooks.com/code-snippets/js-cookie-example-2/* Its being used to search for and parse a cookie stored in the browser*/

  function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for (var i = 0; i < cookieArr.length; i++) {
      var cookiePair = cookieArr[i].split("=");

      /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
      if (name == cookiePair[0].trim()) {
        // Decode the cookie value and return
        return decodeURIComponent(cookiePair[1]);
      }
    }

    // Return null if not found
    return null;
  }
  // converting cart into JSON object
  let cart = JSON.parse(getCookie("cart"));
  // If the browser doesnt contain a cart cookie create one
  if (cart == undefined) {
    cart = {};
    console.log("Cart created", cart);
    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  }
  console.log("Cart:", cart);
});
