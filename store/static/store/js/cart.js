$(document).ready(function () {
  // click function for add to cart button
  $(".update-cart").click(function () {
    //  setting data-product and data action buttons from ckeckout.html to variables
    let productId = this.dataset.product;
    let action = this.dataset.action;
    /* if non logged In user call function from below */
    if (user === "AnonymousUser") {
      addCookieItem(productId, action);
    } else {
      /* if logged In user call function from below */
      upDateUserOrder(productId, action);
    }
  });
  /*cookie created in script tag in base html 
  adds an item to the cookie in the cart 
  if it those not exist if the item already 
  exists increase quantity by one  */
  function addCookieItem(productId, action) {
    console.log("not logged In");
    if (action == "add") {
      if (cart[productId] == undefined) {
        cart[productId] = { quantity: 1 };
      } else {
        cart[productId]["quantity"] += 1;
      }
    }
    /* decrease item by one or if its equal or less then zero remove */
    if (action == "remove") {
      cart[productId]["quantity"] -= 1;
      if (cart[productId]["quantity"] <= 0) {
        console.log("item deleted");
        delete cart[productId];
      }
    }

    document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
    location.reload();
  }

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

      location.reload();
    }
    // calling async await function and adding catch error function
    postUserOrder().catch((error) => {
      console.log("error");
      console.error(error);
    });
  }
});
