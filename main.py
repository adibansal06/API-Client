
import requests

from api_client import login, get_controls, toggle_device
from log_stream import stream_logs


# ============================================================
# MAIN PROGRAM
# ============================================================
# Purpose:
#   Acts as the entry point of the application.
#   Takes input from the user and connects the API functions
#   with the interactive menu.
#
# Responsibilities:
#   1. Collect login credentials.
#   2. Authenticate the user.
#   3. Display the available operations.
#   4. Stream logs or toggle a device.
#   5. Handle errors with clear messages.
#
# Module responsibilities:
#   api_client.py  -> Handles HTTP requests.
#   log_stream.py  -> Repeatedly fetches and prints logs.
#   main.py        -> Handles user interaction and program flow.
# ============================================================


def main():

    # --------------------------------------------------------
    # STEP 1: GET USER INPUT
    # --------------------------------------------------------
    # Collect the portal URL and login credentials.
    # input() allows the user to enter values in the terminal.

    base_url = input("Portal URL: ").rstrip("/")
    username = input("Username: ")
    password = input("Password: ")


    # --------------------------------------------------------
    # STEP 2: ERROR HANDLING
    # --------------------------------------------------------
    # The try block contains the main application logic.
    #
    # If an error occurs, the appropriate except block
    # displays a clear message instead of an unhandled
    # traceback.
    #
    # Note:
    #   The program handles errors that occur inside
    #   the try block.

    try:

        # ----------------------------------------------------
        # STEP 3: LOGIN
        # ----------------------------------------------------
        # Call the login() function from api_client.py.
        # The function sends the credentials to the server
        # and returns an authentication token.

        print("\nLogging in...")

        token = login(base_url, username, password)

        print("Login successful.")


        # ----------------------------------------------------
        # STEP 4: INTERACTIVE MENU
        # ----------------------------------------------------
        # Keep displaying the menu until the user selects Exit.
        #
        # while True creates a loop that allows the user
        # to perform multiple operations in one session.

        while True:

            print("\nChoose an option:")
            print("1. Stream logs")
            print("2. Toggle device")
            print("3. Exit")

            choice = input("Enter choice: ")


            # ------------------------------------------------
            # OPTION 1: STREAM LOGS
            # ------------------------------------------------
            # Call stream_logs() from log_stream.py.
            #
            # The function repeatedly fetches logs and
            # prints them with a 4-second delay.
            #
            # Note:
            #   stream_logs() contains an infinite loop,
            #   so the menu will not be displayed again
            #   until the streaming function stops or returns.

            if choice == "1":

                stream_logs(base_url, token)


            # ------------------------------------------------
            # OPTION 2: TOGGLE DEVICE
            # ------------------------------------------------
            # First fetch the available controls.
            # Then display the devices and ask the user
            # which device they want to toggle.

            elif choice == "2":

                # Fetch devices and control information
                # using the authenticated API request.

                controls = get_controls(base_url, token)

                # Extract the devices list from the response.

                devices = controls["devices"]

                print("\nDevices:")

                # Display each device so the user can
                # identify the device they want to control.

                for device in devices:
                    print(device)

                # Ask the user to enter the selected device ID.

                device_id = input(
                    "\nEnter device ID to toggle: "
                )

                # Call the toggle endpoint with the selected
                # device ID and authentication token.

                result = toggle_device(
                    base_url,
                    token,
                    device_id
                )

                # Display the response returned by the server.

                print("\nToggle result:")
                print(result)


            # ------------------------------------------------
            # OPTION 3: EXIT
            # ------------------------------------------------
            # Break the while loop and terminate the program.

            elif choice == "3":

                print("Goodbye.")
                break


            # ------------------------------------------------
            # INVALID OPTION
            # ------------------------------------------------
            # If the user enters something other than
            # 1, 2, or 3, display an error message.

            else:

                print("Invalid choice.")


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    # --------------------------------------------------------
    # 1. CONNECTION ERROR
    # --------------------------------------------------------
    # Occurs when the client cannot connect to the server,
    # for example, due to a network issue or unreachable host.
    #
    # This exception is a subclass of RequestException,
    # so it is handled before the more general exception.

    except requests.exceptions.ConnectionError:

        print("Server is unreachable.")


    # --------------------------------------------------------
    # 2. OTHER REQUEST ERRORS
    # --------------------------------------------------------
    # Handles other HTTP-related errors raised by Requests,
    # including errors caused by unsuccessful HTTP responses
    # when raise_for_status() is called.

    except requests.exceptions.RequestException as error:

        print(f"Request failed: {error}")


    # --------------------------------------------------------
    # 3. OTHER APPLICATION ERRORS
    # --------------------------------------------------------
    # Handles other exceptions raised by the application,
    # such as missing response fields or custom exceptions
    # from api_client.py.

    except Exception as error:

        print(error)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# __name__ is "__main__" when this file is executed directly.
#
# This prevents main() from running automatically when
# another file imports this module.
# ============================================================

if __name__ == "__main__":

    main()