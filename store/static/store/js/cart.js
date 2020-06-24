// click function for add to cart button
$(".update-cart").click(function () {
  //  setting data-product and data action buttons from ckeckout.html to variables
  let productId = this.dataset.product;
  let action = this.dataset.action;
  if (action == "add") {
  }
  addCookieItem(productId, action);
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
