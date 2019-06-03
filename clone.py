import requests

import json

import os

import sys

if(len(sys.argv) < 4):
	
	print("Please provide suitable arguments in the form 'python clone.py <gitlab home url> <private token> <group_name>'. All arguments are mandatory")
	
	quit()

gitlab_home = sys.argv[1]

api_token = sys.argv[2]

group = sys.argv[3]

url = '{}/api/v4/groups/{}/projects?per_page=100'.format(gitlab_home,group)

response = requests.get(url, headers={'PRIVATE-TOKEN':api_token})

total = len(response.json());

print("Found "+str(total)+" repos.")

projects = json.loads(response.content)

print('Cloning all repositories under group {} visible to the current user'.format(group));

for project in projects:
    
    project_name = project['name']
    
    http_url = project['http_url_to_repo'][8:]
    
    auth_appended_url = 'https://gitlab-ci-token:'+api_token+'@'+http_url
    
    os.system('git clone '+ auth_appended_url)
    
    print('Cloned ' + project_name)
	
print('Done...')
    
    
    
    

    

