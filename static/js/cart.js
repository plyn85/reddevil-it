$(document).ready(function () {
  // click function for add to cart button
  $(".update-cart").click(function () {
    //  setting data-product and data action buttons to variables
    let productId = this.dataset.product;
    let action = this.dataset.action;
    console.log("productId:", productId, "action:", action, user);
    // conditional for non logged In user
    if (user === "AnonymousUser") {
      console.log("not logged In");
    }
    // if logged In user
    else console.log("user is logged In");
  });
});
