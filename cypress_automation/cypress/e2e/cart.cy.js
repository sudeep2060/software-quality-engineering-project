import LoginPage from "../pages/loginPage";
import InventoryPage from "../pages/inventoryPage";
import CartPage from "../pages/cartPage";

describe("Cart Tests", () => {

    const loginPage = new LoginPage();
    const inventoryPage = new InventoryPage();
    const cartPage = new CartPage();

    beforeEach(() => {
        cy.fixture("users").as("users");
    });

    it("TC007 - Open Cart", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.openCart();

        cartPage.verifyCartPage();

    });

    it("TC008 - Verify Product in Cart", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.openCart();

        cartPage.verifyProduct("Sauce Labs Backpack");

    });

    it("TC009 - Continue Shopping", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.openCart();

        cartPage.clickContinueShopping();

        cy.url().should("include", "/inventory.html");

    });

});