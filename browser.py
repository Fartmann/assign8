import csv, time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

URL = "https://reqres.in/"
RESULTS_FILE = "results/browser_metrics.csv"
SCREENSHOT_DIR = "results/screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def test_browser(browser_name):
    print(f"\n=== Testing in {browser_name} ===")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError("Unsupported browser")

    start_time = time.time()
    driver.get(URL)
    load_time = time.time() - start_time

    perf = driver.execute_script("return window.performance.timing")
    ttfb = perf['responseStart'] - perf['requestStart']

    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{browser_name}.png")
    driver.save_screenshot(screenshot_path)

    print(f"Page Load: {load_time:.2f}s | TTFB: {ttfb} ms | Saved: {screenshot_path}")
    driver.quit()
    return (browser_name, round(load_time, 2), ttfb)


if __name__ == "__main__":
    rows = [("Browser", "Load Time (s)", "TTFB (ms)")]
    for browser in ["chrome", "firefox", "edge"]:
        try:
            rows.append(test_browser(browser))
        except Exception as e:
            print(f"Error testing {browser}: {e}")

    with open(RESULTS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"\nSaved results to {RESULTS_FILE}")
