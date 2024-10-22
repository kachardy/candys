document.addEventListener('DOMContentLoaded', () => {
    const shippingCost = 19.99;

    function updateTotal() {
        const boxes = document.querySelectorAll('.box');
        const subtotalElement = document.getElementById('subtotal');
        const shippingElement = document.getElementById('shipping');
        const totalElement = document.getElementById('total');
        let subtotal = 0;
        boxes.forEach(box => {
            const price = parseFloat(box.getAttribute('data-price'));
            const quantityInput = box.querySelector('.quantity');
            let quantity = parseInt(quantityInput.value, 10);

            if (quantity < 1 || isNaN(quantity)) {
                quantity = 1;
                quantityInput.value = quantity;
            }
            subtotal += price * quantity;
        });
        const shipping = boxes.length > 0 ? shippingCost : 0;
        const total = subtotal + shipping;
        subtotalElement.textContent = `R$${subtotal.toFixed(2).replace('.', ',')}`;
        shippingElement.textContent = `R$${shipping.toFixed(2).replace('.', ',')}`;
        totalElement.textContent = `R$${total.toFixed(2).replace('.', ',')}`;
    }

    document.querySelectorAll('.btn-area').forEach(button => {
        button.addEventListener('click', function() {
            const box = this.closest('.box');
            box.remove();
            updateTotal();
        });
    });

    document.querySelectorAll('.quantity').forEach(input => {
        input.addEventListener('input', function() {
            let quantity = parseInt(this.value, 10);

            if (quantity < 1 || isNaN(quantity)) {
                quantity = 1;
                this.value = quantity;
            }
            updateTotal();
        });
    });
    
    updateTotal();
});
