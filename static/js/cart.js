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
    //  adding async function to make the fetch request

    async function postUserOrder() {
      const response = await fetch("/update_item/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        // data we send to the backend as a string
        body: JSON.stringify({ productId: productId, action: action }),
      });
      // returning the response that comes back Into json
      const data = await response.json();

      console.log("data:", data, "succcess");
    }
    // calling async await function and adding catch error function
    postUserOrder().catch((error) => {
      console.log("error");
      console.error(error);
    });
  }
});
