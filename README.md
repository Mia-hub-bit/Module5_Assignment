Robust Contact Manager
This is a robust, command-line application for managing a simple contact list. It is designed with a focus on fault tolerance, utilizing custom exceptions and structured error handling to ensure a smooth user experience.

Features
The application provides the following core functions, each with built-in error handling:

Add Contact (1): Stores a contact's name and phone number. Raises a custom DuplicateContactError if the name already exists.

Find Contact (2): Looks up a phone number by name. Handles KeyError if the contact is not found.

Delete Contact (3): Removes a contact by name. Handles KeyError if the contact does not exist.

Exit (4): Program quits with a message

Prerequisites
Python: This application requires Python 3.x to run.

How to Run the Application
Ensure you have both contact_manager.py and the corresponding unit test file (test_contact_manager.py) saved in the same directory.

Open your terminal or command prompt.

Navigate to the directory where the files are saved.

Execute the application:

python contact_manager.py

Running the Unit Tests
To verify the fault tolerance and functionality of the application, run the unit tests using the standard Python unittest module:

python -m unittest test_contact_manager.py

If successful, the output in terminal will show OK and confirm that all error handling, including the custom exception, are working as intended.
