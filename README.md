# Performance Testing Report
## GOALS
Test frontend and API performance under:
- Browser variations (Chrome, Firefox, Edge)
- Network speeds (3G, 4G, Wi-Fi)
- API load (with Locust)
## TOOLS
- Selenium (UI tests)
- Locust (API stress testing)
- CDP (network simulation)
## RUNNING THE CODE
Firstly, run the `pip install selenium locust`

Then to run `locust.py`, type `locust -f locust.py --host=https://example.com`. You can change the `example.com` to your preferable website.

To run `browser.py` and `network.py`, type `python browser.py` and `python network.py`. If you use VSCode just press "Run the code"
## RESULTS
- You can find the results of the code in results folder. There are .csv file with all of the information and screenshots folder as well.
