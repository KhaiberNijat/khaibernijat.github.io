function calculate() {
    // Get the values from the input fields
    var value1 = parseFloat(document.getElementById('value1').value);
    var value2 = parseFloat(document.getElementById('value2').value);

    // Check if the inputs are valid numbers
    if (isNaN(value1) || isNaN(value2)) {
        alert("Please enter valid numbers in both fields.");
        return;
    }

    // Perform the calculation (addition)
    var result = value1 + value2;

    // Display the result in the result input field
    document.getElementById('result').value = result;
}
