Owner: 						Ani Movsisyan
TC short description: 		Search results with existing and non existing data
Creation Date: 				23/Dec/2021
_______________________________________________________________________________________________
Steps` for install appropriate libs and frameworks
1. Install Python
2. Install Selenium
3. Install Pytest
4. Install Allure
_______________________________________________________________________________________________
                              TC  history
_______________________________________________________________________________________________
Steps:
1. Open the 'https://courses.ultimateqa.com/' page
2. Click on the 'Sign In' button
3. Click on the 'Create a new account' link
4. Fill in all required fields and sign up
5. Check if the user can sign in with registered data
6. Entered the existing data in the 'Search' field on the homepage

Expected Results(Validation):
1. The appropriate result data should be returned
2. Verify that the searched word is contained in all returned results

7. Entered the non existing data in the 'Search' field

Expected Results(Validation):
1. Check that the 'No results were found' message is displayed on the page
_______________________________________________________________________________________________