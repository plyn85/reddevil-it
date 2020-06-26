$(document).ready(function () {
  /* added so flashed messages disappear after ten seconds */

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
            updateText(this_, newLikes, "downvote");
          } else {
            // remove one like
            var newLikes = likeCount - 1;
            updateText(this_, newLikes, "upvote");
          }
        },
        error: function (error) {
          console.log(error);
          console.log("error");
        },
      });
    }
  });
  function addOption() {
    optionText = "Ultimate";
    optionValue = "ultimate";

    $("#id_sizes").append(new Option(optionText, optionValue));
  }
});
