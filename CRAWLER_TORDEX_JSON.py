import re
import json
import requests
import metadata_parser
from datetime import datetime

#BEFORE STARTING RUN tor.exe !!!

#defining query keywords
yourquery = r"..."
keywords = yourquery.replace(" ","+")
query_url = f"http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/search?query={keywords}"
print(f"\nCurrently querying '{yourquery}' on SPACE search engine.")

#crawling .onion links
print("\nCrawling .onion links...")
session = requests.session()
session.proxies = {"http":  "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
content = session.get(query_url, timeout=100).text
regexquery = "\w+\.onion" #\w+\.onion.* to get also subdomains (does not work properly with Torch)
search_results = re.findall(regexquery, content)
onion_links = list(dict.fromkeys(search_results))

#saving results in .csv
savepath = r"C:\Users\nicol\d2web-scraping\crawling-output\\"
json_file = "space_crawling_results" + "_" + str(datetime.now().strftime("%Y-%m-%d") + "_" + datetime.now().strftime("%H.%M.%S")) + ".json"
with open(savepath + json_file,"w+") as newfile:
    print("")
with open(savepath + json_file,"w+", encoding="UTF-8") as file:
    for link in onion_links:
        onion = session.get("http://" + link, timeout=100).text
        content_metadata = metadata_parser.MetadataParser(html=onion, force_doctype=True, search_head_only=False, support_malformed=True)
        data = {}
        data['keyword'] = keywords
        data['engine'] = "Space"
        data['date'] = str(datetime.now().strftime("%Y/%m/%d") + "_" + datetime.now().strftime("%H:%M:%S"))
        data['onion'] = link.replace(">", "").replace("<", "").replace('"', '').replace(" ", "")
        data['metadata'] = content_metadata.metadata
        json_data = json.dumps(data)
        parsed = json.loads(json_data)
        file.write(json.dumps(parsed, indent=4) + "\n")

print(f".onion metadata saved into '{json_file}'\n")