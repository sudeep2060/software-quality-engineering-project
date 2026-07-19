import LoginPage from "../pages/loginPage";

describe("Login Tests", () => {

    const loginPage = new LoginPage();

    beforeEach(() => {
        cy.fixture("users").as("users");
    });

    it("TC001 - Valid Login", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        loginPage.verifyLoginSuccess();
    });

    it("TC002 - Invalid Login", () => {

        loginPage.login(
            "invalid_user",
            "wrong_password"
        );

        loginPage.verifyLoginFailure();
    });

    it("TC003 - Logout", function () {

        loginPage.login(
            this.users.standardUser.username,
            this.users.standardUser.password
        );

        loginPage.logout();

        cy.url().should("eq", "https://www.saucedemo.com/");
    });

});