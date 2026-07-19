import LoginPage from "../pages/loginPage";
import InventoryPage from "../pages/inventoryPage";
import CartPage from "../pages/cartPage";
import CheckoutPage from "../pages/checkoutPage";

describe("Checkout Tests", () => {

    const loginPage = new LoginPage();
    const inventoryPage = new InventoryPage();
    const cartPage = new CartPage();
    const checkoutPage = new CheckoutPage();

    beforeEach(() => {
        cy.fixture("users").as("users");
    });

    it("TC010 - Complete Checkout", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.openCart();

        cartPage.verifyCartPage();

        checkoutPage.completeCheckout(
            "Sudeep",
            "Bhattarai",
            "44600"
        );

        checkoutPage.verifyOrderSuccess();

    });

    it("TC011 - Verify Order Success Message", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.openCart();

        checkoutPage.completeCheckout(
            "Test",
            "User",
            "12345"
        );

        checkoutPage.verifyOrderSuccess();

    });

});