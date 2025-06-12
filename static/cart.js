<script>
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  function updateCartStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
  }

  function addToCart(product) {
    const existing = cart.find(item => item.name === product.name);
    if (existing) {
      existing.quantity += 1;
    } else {
      cart.push({ ...product, quantity: 1 });
    }
    updateCartStorage();
    alert("Added to cart!");
  }

  document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const card = e.target.closest('.product-card');
        const name = card.querySelector('.product-title').textContent;
        const price = card.querySelector('.product-price').textContent.replace(/[₹ ]/g, '');
        const product = { name, price: parseFloat(price) };
        addToCart(product);
      });
    });
  });
</script>
