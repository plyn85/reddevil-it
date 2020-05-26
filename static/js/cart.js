$(document).ready(function () {
  $(".update-cart").click(function (e) {
    let productId = this.dataset.product;
    let action = this.dataset.action;
    console.log("productId:", productId, "action:", action);
  });
});
