$(document).ready(function () {
  // click function for add to cart button
  $(".update-cart").click(function () {
    //  setting data-product and data action buttons to variables
    let productId = this.dataset.product;
    let action = this.dataset.action;
    // console.log("productId:", productId, "action:", action, user);
    // conditional for non logged In user
    if (user === "AnonymousUser") {
      console.log("not logged In");
    }
    // if logged In user
    else {
      upDateUserOrder(productId, action);
    }
  });

  // function will update the user order

  function upDateUserOrder(productId, action) {
    console.log("user is logged In");
    // where we want to send the data to
    var url = "/update_item/";

    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // data we send to the backend as a string
      body: JSON.stringify({ productId: productId, action: action }),
    })
      // once the data is sent to the view return a promise
      .then(function (response) {
        return response.json();
      })
      // then logging the data
      .then(function (response) {
        return response;
      })
      // adding catch statment for errors
      .catch(function (error) {
        console.log(error);
        // adding my own error message
        console.log("error");
      });
  }
});
