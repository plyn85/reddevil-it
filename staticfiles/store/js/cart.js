
$(document).ready(function () {

  
$(".update-cart").click(function () {
  
  // setting variables
  
  let productId = this.dataset.product;
  let action = this.dataset.action;
  
  addCookieItem(productId, action);
});

/*

  cookie created in script tag in base html 
  adds an item to the cookie in the cart 
  if it those not exist if the item already 
  exists increase quantity by one  
  
  */
function addCookieItem(productId, action) {
  console.log("not logged In");
  if (action == "add") {
    alert("You added one Item to your cart!");
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }
  
  /* decrease item by one or if its equal or 
  less then zero remove */
  if (action == "remove") {
    alert("You deleted  one Item to your cart!");
    cart[productId]["quantity"] -= 1;
    if (cart[productId]["quantity"] <= 0) {
      delete cart[productId];
    }
  }

   document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
   location.reload();
}

})