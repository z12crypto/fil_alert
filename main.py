import os
import time
import urllib3

POST_ALERT_API="https://fwalert.com/66dbf8ba-c6f6-4e47-b400-69116db4b659"

def main():
    faults = 100
    while True:
        current_faults = os.popen("fil_faults_count").readlines()
        int(current_faults)
        if current_faults > faults:
            FWAlert(ALERT_API=POST_ALERT_API)
            faults = current_faults
        time.sleep(300)

def FWAlert(ALERT_API):
    http = urllib3.PoolManager()
    r = http.request("GET",ALERT_API)
    return 0