class InventoryPage {

    addBackpack() {
        cy.get("#add-to-cart-sauce-labs-backpack").click();
    }

    removeBackpack() {
        cy.get("#remove-sauce-labs-backpack").click();
    }

    openCart() {
        cy.get(".shopping_cart_link").click();
    }

    verifyCartCount(count) {
        cy.get(".shopping_cart_badge").should("have.text", count);
    }

    verifyProductName(name) {
        cy.get(".inventory_item_name").first().should("have.text", name);
    }
}

export default InventoryPage;