function validateForm() {
    const email = document.forms[0]["email"].value;
    const password = document.forms[0]["password"].value;

    if (!email.includes("@")) {
        alert("Invalid email format!");
        return false;
    }

    if (password.length < 15) {
        alert("Password must be at least 15 characters.");
        return false;
    }

    return true;
}
