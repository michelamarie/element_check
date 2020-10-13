import requests
import os, sys

# Nagios check to verify that a given div or other code-level element is present in a web page.
# By Michela Toscano
# Usage: 'python browser_page_check.py https://domain.ca/' 


url = sys.argv[1]

# Fetch main page for FKC site
r = requests.get(url)

# Next: search for '<div id="content" class="main clearfix">'.
# If that div id is not found, then throw a 'critical' condition for Nagios, else return an 'okay' status.
if '<div id="content"' in r.text:
    print("OK - Page appears to be normal")
    sys.exit(0)
else:
    print("Critical: Page appears to be broken")
    sys.exit(2)
