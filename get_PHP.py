# This script will take a file call urls.txt and grab the headers and 
# then if the headers contains the phrase "php" it'll save it to the 
# output.txt file with the url, example output below

# https://portal.digitalbusiness.telstra.com
# {'Date': 'Mon, 22 Oct 2018 04:35:27 GMT', 'Server': 'Apache/2.2.3 (Red Hat)', 'X-Powered-By': 'PHP/5.3.3', etc, etc, etc

import requests
import re

urls = open("urls.txt", "r")
output = open("output.txt", "w+")

for lines in urls:
    try:
        lines = lines.strip('\n')
        r = requests.get(lines)
        head = str(r.headers)
        result = re.findall(r'.*(php|PHP)', head)

        if result is not None and len(result) > 0:
            output.writelines(lines + '\n')
            output.writelines(head + '\n' + '\n')
    except:
        print('')

urls.close()
output.close()
