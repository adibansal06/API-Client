
import requests


# ============================================================
# 1. LOGIN
# ============================================================
# Purpose:
#   Authenticates the user using a username and password.
#
# Authentication:
#   No token is required initially because this endpoint
#   is used to obtain the authentication token.
#
# Discovery:
#   Found by observing the login request in
#   DevTools -> Network.
#
# Returns:
#   The authentication token received from the server.
# ============================================================

def login(base_url, username, password):

    url = f"{base_url}/api/login"

    # Data sent to the server in the request body.
    data = {
        "username": username,
        "password": password
    }

    # Send a POST request to authenticate the user.
    response = requests.post(url, json=data)

    # Status code 401 means authentication failed.
    if response.status_code == 401:
        raise Exception(
            "Login failed: wrong username or password."
        )

    # Raise an exception for other unsuccessful responses.
    response.raise_for_status()

    # Convert the JSON response into a Python dictionary.
    result = response.json()

    # Return the token for use in protected requests.
    return result["token"]


# ============================================================
# 2. GET LOGS
# ============================================================
# Purpose:
#   Fetches system logs from the server.
#
# Authentication:
#   Requires a valid authentication token.
#   The token is sent in the Authorization header.
#
# Discovery:
#   Found by observing the dashboard's log request
#   in DevTools -> Network.
#
# Returns:
#   The logs received from the server.
# ============================================================

def get_logs(base_url, token):

    url = f"{base_url}/api/logs"

    # Attach the token using the Bearer authentication scheme.
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Send a GET request to fetch the logs.
    response = requests.get(url, headers=headers)

    # Status code 401 means the token was rejected.
    if response.status_code == 401:
        raise Exception(
            "Authentication failed: token was rejected."
        )

    # Raise an exception for other unsuccessful responses.
    response.raise_for_status()

    # Return the server's JSON response.
    return response.json()


# ============================================================
# 3. GET CONTROLS
# ============================================================
# Purpose:
#   Fetches the devices and profile information
#   available to the authenticated user.
#
# Authentication:
#   Requires a valid authentication token.
#
# Discovery:
#   Found by observing the controls request
#   in DevTools -> Network.
#
# Returns:
#   The controls data received from the server.
#   The response contains the devices information
#   and other data such as the profile.
# ============================================================

def get_controls(base_url, token):

    url = f"{base_url}/api/controls"

    # Attach the token to authenticate the request.
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Send a GET request to fetch the controls data.
    response = requests.get(url, headers=headers)

    # Status code 401 means the token was rejected.
    if response.status_code == 401:
        raise Exception(
            "Authentication failed: token was rejected."
        )

    # Raise an exception for other unsuccessful responses.
    response.raise_for_status()

    # Return the server's JSON response.
    return response.json()


# ============================================================
# 4. TOGGLE DEVICE
# ============================================================
# Purpose:
#   Changes the ON/OFF state of a specific device.
#
# Authentication:
#   Requires a valid authentication token.
#
# Discovery:
#   Found by observing the device toggle request
#   in DevTools -> Network.
#
# Parameters:
#   base_url  -> Base URL of the portal.
#   token     -> Authentication token.
#   device_id -> ID of the device to toggle.
#
# Returns:
#   The server's response after the toggle request.
# ============================================================

def toggle_device(base_url, token, device_id):

    # The device ID is included in the URL path.
    url = f"{base_url}/api/controls/{device_id}/toggle"

    # Attach the authentication token.
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Send a POST request to toggle the device.
    response = requests.post(url, headers=headers)

    # Status code 401 means authentication failed.
    if response.status_code == 401:
        raise Exception(
            "Authentication failed: token was rejected."
        )

    # Status code 403 means the server refused
    # the request because the user is not permitted
    # to perform the requested action.
    if response.status_code == 403:
        raise Exception(
            "You are not allowed to control this device."
        )

    # Raise an exception for other unsuccessful responses.
    response.raise_for_status()

    # Return the server's JSON response.
    return response.json()