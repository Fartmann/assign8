from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

NETWORK_PROFILES = {
    "WiFi": {
        "offline": False,
        "latency": 20, #ms
        "downloadThroughput": 10 * 1024 * 1024 / 8,
        "uploadThroughput": 5 * 1024 * 1024 / 8
    },
    "4G": {
        "offline": False,
        "latency": 50,
        "downloadThroughput": 4 * 1024 * 1024 / 8,
        "uploadThroughput": 2 * 1024 * 1024 / 8
    },
    "3G": {
        "offline": False,
        "latency": 100,
        "downloadThroughput": 1.5 * 1024 * 1024 / 8,
        "uploadThroughput": 0.75 * 1024 * 1024 / 8 
    }
}

def test_network(condition_name):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(options=options)

    try:
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd(
            "Network.emulateNetworkConditions",
            NETWORK_PROFILES[condition_name]
        )

        start = time.time()
        driver.get("https://reqres.in/")
        end = time.time()

        print(f"[{condition_name}] Load time: {end - start:.2f} sec")

    finally:
        driver.quit()


if __name__ == "__main__":
    for condition in NETWORK_PROFILES.keys():
        test_network(condition)
