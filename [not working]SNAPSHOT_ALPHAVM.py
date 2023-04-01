from selenium import webdriver
from datetime import datetime
from time import sleep

#BEFORE STARTING RUN tor.exe !!!

#defining query keywords 
yourquery = r"..."
keywords = "%22" + yourquery.replace(" ","%20") + "%22"
url = f"http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion/search?text={keywords}"
print(f"\nCurrently querying '{yourquery}' on ALPHAVM collections.")

#scraping AlphaVM website
print("\nCrawling related links...")
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'socksProxy': '127.0.0.1:9050',
    'socksVersion': 5,
})

options = Options()
options.proxy = proxy 
#options.binary_location = '/home/furas/bin/tor'  # doesn't work
#options.binary_location = '/path/to/normal/firefox'  # works

driver = webdriver.Firefox(options=options)
driver.get(url)
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()