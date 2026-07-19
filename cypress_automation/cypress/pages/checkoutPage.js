class CheckoutPage {

    clickCheckout() {
        cy.get("#checkout").click();
    }

    enterFirstName(firstName) {
        cy.get("#first-name").clear().type(firstName);
    }

    enterLastName(lastName) {
        cy.get("#last-name").clear().type(lastName);
    }

    enterPostalCode(postalCode) {
        cy.get("#postal-code").clear().type(postalCode);
    }

    clickContinue() {
        cy.get("#continue").click();
    }

    clickFinish() {
        cy.get("#finish").click();
    }

    verifyOverviewPage() {
        cy.url().should("include", "/checkout-step-two.html");
    }

    verifyOrderSuccess() {
        cy.get(".complete-header")
            .should("have.text", "Thank you for your order!");
    }

    completeCheckout(firstName, lastName, postalCode) {

        this.clickCheckout();

        this.enterFirstName(firstName);
        this.enterLastName(lastName);
        this.enterPostalCode(postalCode);

        this.clickContinue();

        this.verifyOverviewPage();

        this.clickFinish();
    }

}

export default CheckoutPage;