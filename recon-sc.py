#!/usr/bin/python3

import time
import json
import requests
import argparse
from termcolor import colored

logo = """
'########::'########::'######:::'#######::'##::: ##:::::::::::'######:::'######::
 ##.... ##: ##.....::'##... ##:'##.... ##: ###:: ##::::::::::'##... ##:'##... ##:
 ##:::: ##: ##::::::: ##:::..:: ##:::: ##: ####: ##:::::::::: ##:::..:: ##:::..::
 ########:: ######::: ##::::::: ##:::: ##: ## ## ##:'#######:. ######:: ##:::::::
 ##.. ##::: ##...:::: ##::::::: ##:::: ##: ##. ####:........::..... ##: ##:::::::
 ##::. ##:: ##::::::: ##::: ##: ##:::: ##: ##:. ###::::::::::'##::: ##: ##::: ##:
 ##:::. ##: ########:. ######::. #######:: ##::. ##::::::::::. ######::. ######::
..:::::..::........:::......::::.......:::..::::..::::::::::::......::::......:::
..:::::..::....Created By Sherwood Chaser......:::::::::::::::......::::......:::
..:::::..::........:::......::::.......:::..::::..::::::::::::......::::......:::

"""

print(logo)

pr = argparse.ArgumentParser(description="Get Subdomains Tool Using Crt.sh..")
pr.add_argument("--domain", help="Specify Domain Name.")
pr.add_argument("--scan", help="Scan Result For Live Subdomains.", action="store_true")
args = pr.parse_args()


def getSubdomain():
	print(colored("[+] Getting Subdomains of : ", "yellow", attrs=['bold']) + colored( args.domain + "\n", "cyan", attrs=['bold']))
	list_domains = []
	url = requests.get("https://crt.sh/?q=%25.{}&output=json".format(args.domain))
	content = url.text
	json_data = json.loads(content)
	for (key,value) in enumerate(json_data):
		if value['name_value'] not in list_domains:
			list_domains.append(value['name_value'])
	return list_domains

if args.domain:
	searchResult = getSubdomain()
	for i in searchResult:
		print(colored(i, "green", attrs=['bold']))
	print("\n" + colored("[+] Discovered ", "grey", attrs=['bold']) + colored(str(len(searchResult)) + " Subdomains.", "magenta"))
