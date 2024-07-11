## Flask Application Design for an Interactive Pythagoras Theorem Learning Game

### HTML Files

- **index.html**: The main HTML file that acts as the landing page of the application. It will contain the form for user input and a display area for the result.
- **result.html**: This HTML file will show the step-by-step calculation of the Pythagorean theorem based on the user's input from the index.html file.

### Routes

- **index**: The route for the index.html file. It displays the input form to the user.

- **calculate**: The route that handles the user's input from the index page, performs the calculation, and renders the result.html file with the calculated values.