
# API Discovery Process

The API endpoints were discovered by observing the requests made by the web dashboard using the browser's Developer Tools (DevTools → Network).

## 1. Login Endpoint

- **How discovered:** Opened the Network tab and submitted the login form.
- **Observation:** A POST request was sent to `/api/login`.
- **Purpose:** Authenticates the user using a username and password.
- **Authentication:** No authentication token is available before login. The server returns a token after successful authentication.

## 2. Get Logs Endpoint

- **How discovered:** After logging in, observed the repeated requests made by the dashboard to retrieve logs.
- **Observation:** A GET request was sent to `/api/logs`.
- **Purpose:** Fetches system logs from the server.
- **Authentication:** Requires a valid token in the Authorization header using the Bearer scheme.

## 3. Get Controls Endpoint

- **How discovered:** Observed the network requests associated with loading the devices and controls information.
- **Observation:** A GET request was sent to `/api/controls`.
- **Purpose:** Retrieves the available devices and related control information.
- **Authentication:** Requires a valid authentication token.

## 4. Toggle Device Endpoint

- **How discovered:** Opened the Network tab, switched a device OFF from the dashboard, and identified the request that changed its state.
- **Observation:** A POST request was sent to `/api/controls/{device_id}/toggle`.
- **Purpose:** Changes the ON/OFF state of a specific device.
- **Authentication:** Requires a valid authentication token. The device ID is included in the URL path.

## Tools Used

- Browser Developer Tools → Network tab
- HTTP/HTTPS request method and URL inspection
- Request headers and response inspection
- Python Requests library for implementing the discovered API calls

### Why server refuses requests that carry no valid reason because:
The server requires a valid secret to verify that the request comes from an authenticated user. If the secret is missing or invalid, the server cannot authenticate the requester, so it rejects the request to protect the API and its resources.




