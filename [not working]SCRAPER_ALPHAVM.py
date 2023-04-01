import json
import requests
import metadata_parser
from time import sleep
from datetime import datetime

#BEFORE STARTING RUN tor.exe !!!

#defining query keywords 
yourquery = r"..."
keywords = "%22" + yourquery.replace(" ","%20") + "%22"
url = f"http://alphvmmm27o3abo3r2mlmjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion/search?text={keywords}"
print(f"\nCurrently querying '{yourquery}' on ALPHAVM collections.")

#scraping .onion website
print("\nAccessing ALPHAVM collections...")
session = requests.session()
session.proxies = {"http":  "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
content = session.get(url, timeout=60)
print("\nVerifying connection...")
sleep(300)
text = content.text
content_metadata = metadata_parser.MetadataParser(html=text, force_doctype=True, search_head_only=False, support_malformed=True)

#saving text in .xml file
savepath = r"C:\Users\nicol\d2web-scraping\scraping-output\\"
xml_file = "onion_scraping_results" + "_" + str(datetime.now().strftime("%Y-%m-%d") + "_" + datetime.now().strftime("%H.%M.%S")) + ".xml"
with open(savepath + xml_file,"w+") as newfile:
    print("")
with open(savepath + xml_file,"w+", encoding="UTF-8") as file:
    file.write(text)
print(f".onion content saved into '{xml_file}'")

#saving metadata in .json file
json_file = "onion_scraping_results" + "_" + str(datetime.now().strftime("%Y-%m-%d") + "_" + datetime.now().strftime("%H.%M.%S")) + ".json"
with open(savepath + json_file,"w+") as newfile:
    print("")
with open(savepath + json_file,"w+", encoding="UTF-8") as file:
    json.dump(content_metadata.metadata, file)
print(f".onion metadata saved into '{json_file}'\n")