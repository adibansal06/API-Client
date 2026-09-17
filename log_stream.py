
import time

from api_client import get_logs


# ============================================================
# LOG STREAMING
# ============================================================
# Purpose:
#   Continuously fetches logs from the server and prints them
#   as part of the log streaming functionality.
#
# Authentication:
#   Requires a valid authentication token, which is passed
#   to the get_logs() function.
#
# Discovery:
#   The dashboard repeatedly requests the logs endpoint.
#   This behavior was observed in DevTools -> Network.
#
# How it works:
#   1. Fetch logs from the server.
#   2. Print each log entry.
#   3. Wait for 4 seconds.
#   4. Repeat the process.
#
# Why polling?
#   The dashboard checks for new logs at regular intervals
#   instead of maintaining a continuous connection.
#
# Note:
#   This function runs continuously until the script
#   is stopped by the user.
# ============================================================

def stream_logs(base_url, token):

    # Keep fetching logs repeatedly.
    while True:

        # Call the reusable API function to fetch logs.
        logs = get_logs(base_url, token)

        # Print each log entry received from the server.
        for log in logs:
            print(log)

        # Wait 4 seconds before making the next request.
        # This prevents sending requests continuously
        # without any delay.
        time.sleep(4)
        #what if we do not have here a sleep?
        #we will be making requests to the server every 4 seconds,
        #which could lead to rate limiting or excessive load on the server. 
        #The sleep function helps to space out the requests and reduce the frequency of API calls, 
        #allowing for a more manageable and efficient log streaming process.
        #is this comment correct?Yes, your comment is correct. Without the `time.sleep(4)` call, the `stream_logs` function would continuously make requests to the server without any delay, which could lead to several issues:
        #1. Rate Limiting: Many APIs have rate limits to prevent abuse. If you exceed these limits, the server may start rejecting your requests or temporarily block your IP address.
        #2. Excessive Load: Continuously making requests without any delay can put unnecessary load on the server, potentially affecting its performance and the experience of other users. 