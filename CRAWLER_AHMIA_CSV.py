import re
import requests
from datetime import datetime

#BEFORE STARTING RUN tor.exe !!!

#defining query keywords
yourquery = r"..."
keywords = yourquery.replace(" ","+")
url = f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={keywords}"
print(f"\nCurrently querying '{yourquery}' on AHMIA search engine.")

#crawling .onion links
print("\nCrawling .onion links...")
session = requests.session()
session.proxies = {"http":  "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
content = session.get(url, timeout=100).text
regexquery = "\w+\.onion" #\w+\.onion.* to get also subdomains (does not work properly with Torch)
search_results = re.findall(regexquery, content)
onion_links = list(dict.fromkeys(search_results))

#saving results in .csv
savepath = r"C:\Users\nicol\d2web-scraping\crawling-output\\"
filename = "ahmia_crawling_results" + "_" + str(datetime.now().strftime("%Y-%m-%d") + "_" + datetime.now().strftime("%H.%M.%S")) + ".csv"
with open(savepath + filename,"w+") as newfile:
    print("")
for link in onion_links:
    with open(savepath + filename,"a") as file:
        row = link.replace(">", "").replace("<", "").replace('"', '').replace(" ", "")
        file.write(keywords + "," + "Ahmia" + "," + str(datetime.now().strftime("%Y-%m-%d") + "_" + datetime.now().strftime("%H:%M:%S")) + "," + row + "\n")
print(f".onion websites saved into '{filename}'\n")