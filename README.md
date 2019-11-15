# Automated-Keyring-Credentials
A basic regime for deploying Keyring options for locally encrypting login credentials (string Username, string Password).

Many APIs and requests modules will require you to pass a Tuple of (Username, Password) combinations.
The Keyring library allows you to store locally encrypted passwords such that they do not need to appear as "plain-text"
in the source code allowing for secure automation. This module creates a standardized regime for how to deploy Keyring such that users
can choose to manually enter their credentials, update existing encrypted credentials, set new encrypted credentials, or to use a default
set of encrypted credentials.

********* HOW TO USE INSIDE MAIN FUNCTION *************

basic_auth: Tuple[str, str] = check_credentials(
        ARGS.manualCredentials,
        ARGS.updateCredentials,
        "Service Name"
    )
    
Will create a basic_auth Tuple which can be passed anywhere expecting one
