import argparse
import json
import random
import string
import requests
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
user = dict()
superuser = 
password = 
HOST_KIB = ''
HOST_ELS = ''
#superuser = ''
#password = ''
#HOST_KIB = ''
#HOST_ELS = ''
spaces = {
          }

BASE_KIBANA_ENDPOINT = 'https://' + HOST_KIB + ':5601'
BASE_ELS_ENDPOINT = 'https://' + HOST_ELS + ':9200'
HEADERS_ARR = {'kbn-xsrf': 'true', 'Content-Type': 'application/json'}

# @@@@@@@@@@@@@@ SPACES @@@@@@@@@@@@@@


def createSpaces():
    # Setting up BASE_ENDPOINT and HEADERS_ARR for SPACES
    SPACE_ENDPOINT = BASE_KIBANA_ENDPOINT + '/api/spaces/space'
    HEADERS_ARR = {'kbn-xsrf': 'true', 'Content-Type': 'application/json'}

# Checking if spaces exist
    for space in spaces.keys():
        SPACE_ID = space.lower()
        SPACE_ID_CAP = space.capitalize()
        SPACE_ID_ENDPOINT = SPACE_ENDPOINT + '/' + SPACE_ID
        response = requests.get(SPACE_ID_ENDPOINT, auth=(superuser, password),
                                headers=HEADERS_ARR, verify=False)
        # print(response.text)
        if response.status_code != 200:  # IF SPACE does not exist, create the new SPACE.
            payload = {"id": SPACE_ID,  "name": SPACE_ID_CAP,  "description": "This is the " + SPACE_ID_CAP + " Space",  "color": "#aabbcc",  "initials": space[:3],
                       "disabledFeatures": ["savedObjectsManagement", "savedObjectsTagging", "enterpriseSearch", "logs", "infrastructure", "apm", "uptime", "siem", "dev_tools", "advancedSettings", "fleet", "actions", "stackAlerts", "monitoring"],  "imageUrl": ""}
            payloadJson = json.dumps(payload)
            response = requests.post(SPACE_ENDPOINT, auth=(superuser, password),
                                     data=payloadJson, headers=HEADERS_ARR, verify=False)
            # print(response.text)


# @@@@@@@@@@@@@@ INDEX_PATTERNS @@@@@@@@@@@@@@


def createIndexPatterns():
    # space_id is provided in the spaces dictionary and needs to be capitalized. Index_pattern is also provided
    BASE_INDPATT_ENDPOINT = BASE_KIBANA_ENDPOINT + \
        '/api/index_patterns/index_pattern'
    BASE_INDPATT_ID_ENDPOINT_ELS = BASE_ELS_ENDPOINT + '.kibana/_search?'

    # Creating all index_patterns for Default space
    for space_id in spaces.keys():
        for index_pattern in spaces[space_id]["kib_index_pattern"]:
            BASE_INDPATT_ID_ENDPOINT = BASE_INDPATT_ENDPOINT + \
                '/' + index_pattern[:-1]
            response = requests.get(BASE_INDPATT_ID_ENDPOINT, auth=(superuser, password),
                                    headers=HEADERS_ARR, verify=False)
            if response.status_code != 200:  # If the id_pattern does not exist
                payload = {"refresh_fields": 'true', "index_pattern": {
                    "id": index_pattern[:-1], "title": index_pattern}}
                payloadJson = json.dumps(payload)
                response = requests.post(BASE_INDPATT_ENDPOINT, auth=(superuser, password),
                                         data=payloadJson, headers=HEADERS_ARR, verify=False)

    # Creating all index_patterns for each space
    for space_id in spaces.keys():
        SPACE_ID = space_id.lower()
        SPACE_INDPATT_ID_ENDPOINT = BASE_KIBANA_ENDPOINT + \
            '/s/' + SPACE_ID + '/api/index_patterns/index_pattern'
        for index_pattern in spaces[space_id]["kib_index_pattern"]:
            SPACE_INDPATT_ID_ENDPOINT_TEMP = SPACE_INDPATT_ID_ENDPOINT + \
                '/' + index_pattern[:-1]
            response = requests.get(SPACE_INDPATT_ID_ENDPOINT_TEMP, auth=(superuser, password),
                                    headers=HEADERS_ARR, verify=False)
            if response.status_code != 200:
                payload = {"refresh_fields": 'true', "index_pattern": {
                    "id": index_pattern[:-1], "title": index_pattern}}
                payloadJson = json.dumps(payload)
                response = requests.post(SPACE_INDPATT_ID_ENDPOINT, auth=(superuser, password),
                                         data=payloadJson, headers=HEADERS_ARR, verify=False)


# @@@@@@@@@@@@@@ ROLES @@@@@@@@@@@@@@

def createRoles():
    BASE_ROLES_ENDPOINT = BASE_KIBANA_ENDPOINT + '/api/security/role'

# For each space - applicant create RW and R roles
    for space_id in spaces.keys():
        RWroleName = space_id.lower() + "RWrole"
        RroleName = space_id.lower() + "Rrole"
        # For RW roles
        ROLE_ENDPOINT = BASE_ROLES_ENDPOINT + '/' + RWroleName
        response = requests.get(ROLE_ENDPOINT, auth=(superuser, password),
                                headers=HEADERS_ARR, verify=False)
        # print(response.text)
        if response.status_code != 200:
            # print(spaces[space_id]["kib_index_pattern"][:-1])
            payload = {"elasticsearch": {"cluster": [],    "indices": [{
                "names": spaces[space_id]["kib_index_pattern"][:-1],
                "privileges": ["read", "write", "view_index_metadata"]
            }, {
                "names": [spaces[space_id]["kib_index_pattern"][-1]],
                "privileges": ["read", "view_index_metadata"]
            }
            ]
            },
                "kibana": [
                {
                    "base": [],
                    "feature": {"discover": ["all"],
                                "dashboard": ["all"],
                                "canvas": ["all"],
                                "maps": ["all"],
                                "ml": ["all"],
                                "visualize": ["all"],
                                "indexPatterns": ["all"]},
                    "spaces": [space_id.lower()]
                }
            ]
            }
            payloadJson = json.dumps(payload)
            response = requests.put(ROLE_ENDPOINT, auth=(superuser, password),
                                    data=payloadJson, headers=HEADERS_ARR, verify=False)

            # print(response.text)

        ROLE_ENDPOINT = BASE_ROLES_ENDPOINT + RroleName
        response = requests.get(ROLE_ENDPOINT, auth=(superuser, password),
                                headers=HEADERS_ARR, verify=False)
        if response.status_code != 200:
            payload = {"elasticsearch": {"cluster": [],    "indices": [{
                "names": spaces[space_id]["kib_index_pattern"],
                "privileges": ["read", "view_index_metadata"]
            }]
            },
                "kibana": [
                {
                    "base": [],
                    "feature": {"discover": ["all"],
                                "dashboard": ["all"],
                                "canvas": ["all"],
                                "maps": ["all"],
                                "ml": ["all"],
                                "visualize": ["all"],
                                "indexPatterns": ["all"]},
                    "spaces": [space_id.lower()]
                }
            ]
            }
            payloadJson = json.dumps(payload)
            response = requests.put(ROLE_ENDPOINT, auth=(superuser, password),
                                    data=payloadJson, headers=HEADERS_ARR, verify=False)


# @@@@@@@@@@@@@@ USERS @@@@@@@@@@@@@@


def createUsers():
    BASE_USER_ENDPOINT = BASE_ELS_ENDPOINT + '/_security/user/'
    for userid in users.keys():
        USERID_ENDPOINT = BASE_USER_ENDPOINT + userid
        response = requests.get(USERID_ENDPOINT, auth=(superuser, password),
                                headers=HEADERS_ARR, verify=False)
        if response.status_code == 404:
            payload = {"password": users[userid]["password"],
                       "roles": users[userid]["role"],
                       "full_name": users[userid]["Fullname"],
                       "email": users[userid]["email"],
                       "metadata": {}
                       }
            payloadJson = json.dumps(payload)
            response = requests.post(USERID_ENDPOINT, auth=(superuser, password),
                                     data=payloadJson, headers=HEADERS_ARR, verify=False)


# Executing functions for space, role, index_pattern, user creation for centralized deployment.
def createKibana_RBAC():
    createSpaces()
    createIndexPatterns()
    createRoles()
    createUsers()


createKibana_RBAC()
