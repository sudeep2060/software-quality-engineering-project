class LoginPage {

    visit() {
        cy.visit("https://www.saucedemo.com/");
    }

    enterUsername(username) {
        cy.get("#user-name").clear().type(username);
    }

    enterPassword(password) {
        cy.get("#password").clear().type(password);
    }

    clickLogin() {
        cy.get("#login-button").click();
    }

    login(username, password) {
        this.visit();
        this.enterUsername(username);
        this.enterPassword(password);
        this.clickLogin();
    }

    verifyLoginSuccess() {
        cy.url().should("include", "/inventory.html");
    }

    verifyLoginFailure() {
        cy.get('[data-test="error"]').should("be.visible");
    }

    logout() {
        cy.get("#react-burger-menu-btn").click();
        cy.get("#logout_sidebar_link").click();
    }
}

export default LoginPage;