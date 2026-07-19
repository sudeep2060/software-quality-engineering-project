import LoginPage from "../pages/loginPage";
import InventoryPage from "../pages/inventoryPage";

describe("Inventory Tests", () => {

    const loginPage = new LoginPage();
    const inventoryPage = new InventoryPage();

    beforeEach(() => {
        cy.fixture("users").as("users");
    });

    it("TC004 - Verify Product Name", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.verifyProductName("Sauce Labs Backpack");
    });

    it("TC005 - Add Product to Cart", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.verifyCartCount("1");
    });

    it("TC006 - Remove Product from Cart", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        inventoryPage.addBackpack();

        inventoryPage.removeBackpack();

        cy.get(".shopping_cart_badge").should("not.exist");
    });

});