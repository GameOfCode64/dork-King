import time
import random
from googlesearch import search
from art import *

# List of User-Agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/53.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/14.14393 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
]

# List of Proxies
proxies = [
    "http://51.15.166.107:3128",
    "http://51.15.228.225:3128",
    "http://51.15.166.107:8888",
    "http://51.15.228.225:8888",
    "http://54.38.218.209:6582",
    "http://91.188.247.38:8085",
    "http://200.105.215.18:33630",
    "http://193.200.151.69:8080",
    "http://128.199.202.122:8080",
    "http://103.250.153.203:8080",
    "http://47.251.4.174:1080",
    "http://103.250.153.203:8080"
]
def get_random_user_agent():
    return random.choice(user_agents)

def get_random_proxy():
    return random.choice(proxies)

def google_dork_search(domain, dorks, num_results=10):
    results = {}
    for dork in dorks:
        query = dork.replace("example.com", domain)
        results[query] = []
        print(f"Searching for: {query}")

        try:
            for result in search(query, num_results=num_results, user_agent=get_random_user_agent(), verify_ssl=False):
                print(result)
                results[query].append(result)
                time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds
        except Exception as e:
            print(f"Error searching for {query}: {e}")
    
    return results

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as file:
        for query, urls in results.items():
            file.write(f"Query: {query}\n")
            for url in urls:
                file.write(f"{url}\n")
            file.write("\n")

if __name__ == "__main__":
    tprint("Dork King")
    print("By Game of Code")

    domain = input("Enter the domain name: ")
    output_file = "dork_results.txt"

    # Prompt user to enter dorks
    print("Enter Google dorks (enter 'done' to finish):")
    dorks = [
        "site:example.com -www -shop -share -ir -mfa",
        "site:example.com ext:php inurl:?",
        "site:example.com inurl:api | site:*/rest | site:*/v1 | site:*/v2 | site:*/v3",
        "site:\"example.com\" ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess | ext:json",
        "site:example.com inurl:conf | inurl:env | inurl:cgi | inurl:bin | inurl:etc | inurl:root | inurl:sql | inurl:backup | inurl:admin | inurl:php site:example.com",
        "site:example.com inurl:\"error\" | intitle:\"exception\" | intitle:\"failure\" | intitle:\"server at\" | inurl:exception | \"database error\" | \"SQL syntax\" | \"undefined index\" | \"unhandled exception\" | \"stack trace\" site:example.com",
        "site:example.com inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:example.com",
        "site:example.com inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:& inurl:http site:example.com",
        "site:example.com inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:example.com",
        "site:example.com inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain=  | inurl:page= inurl:& site:example.com",
        "site:example.com inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:& site:example.com",
        "site:example.com inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read=  | inurl:ping= inurl:& site:example.com",
        "site:example.com inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read=  | inurl:ping= inurl:& site:example.com",
        "site:example.com ”choose file”",
        "site:example.com inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:\"example.com\"",
        "site:example.com inurl:login | inurl:signin | intitle:login | intitle:signin | inurl:secure site:example.com",
        "site:example.com ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx",
        "intext:\"confidential\" | intext:\"Not for Public Release\" | intext:\"internal use only\" | intext:\"do not distribute\"",
        "site:example.com inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:& site:example.com",
        "site:example.com inurl:/content/usergenerated | inurl:/content/dam | inurl:/jcr:content | inurl:/libs/granite | inurl:/etc/clientlibs | inurl:/content/geometrixx | inurl:/bin/wcm | inurl:/crx/de site:example.com",
        "site:openbugbounty.org inurl:reports intext:\"example.com\"",
        "site:pastebin.com \"example.com\"",
        "site:jsfiddle.net \"example.com\"",
        "site:codebeautify.org \"example.com\"",
        "site:codepen.io \"example.com\"",
        "site:s3.amazonaws.com \"example.com\"",
        "site:blob.core.windows.net \"example.com\"",
        "site:googleapis.com \"example.com\"",
        "site:drive.google.com \"example.com\"",
        "site:dev.azure.com \"example.com\"",
        "site:onedrive.live.com \"example.com\"",
        "site:digitaloceanspaces.com \"example.com\"",
        "site:sharepoint.com \"example.com\"",
        "site:s3-external-1.amazonaws.com \"example.com\"",
        "site:s3.dualstack.us-east-1.amazonaws.com \"example.com\"",
        "site:dropbox.com/s \"example.com\"",
        "site:box.com/s \"example.com\"",
        "site:docs.google.com inurl:\"/d/\" \"example.com\"",
        "site:jfrog.io \"example.com\"",
        "site:firebaseio.com \"example.com\"",
        "site:\"example.com\"/server-status apache",
        "site:\"example.com\" intext:\"Powered by\" & intext:Drupal & inurl:user",
        "site:*/joomla/login"
    ]

    while True:
        dork = input()
        if dork.lower() == 'done':
            break
        dorks.append(dork)

    results = google_dork_search(domain, dorks)
    save_results_to_file(results, output_file)
    print(f"Results saved to {output_file}")

