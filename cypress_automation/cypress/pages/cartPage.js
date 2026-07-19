class CartPage {

    clickCheckout() {
        cy.get("#checkout").click();
    }

    clickContinueShopping() {
        cy.get("#continue-shopping").click();
    }

    verifyProduct(productName) {
        cy.contains(productName).should("be.visible");
    }

    verifyCartPage() {
        cy.url().should("include", "/cart.html");
    }

}

export default CartPage;