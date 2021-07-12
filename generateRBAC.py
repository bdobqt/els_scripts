import argparse
import json
import random
import string
import requests
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

users = {"aviateuser01": {"Fullname": "Alex Fourlis", "password": "qJP6jSLxvxT4z$#j", "email": "afourlis@vidavo.eu", "role": "aviateRWrole"},
         "vadiuser01": {"Fullname": "Francesco Saverio Quatrano", "password": "W5Q27S&434bhfY5", "email": "fsquatrano@gmail.com", "role": "vadiRWrole"},
         "vadiuser02": {"Fullname": "Abbas Ogaji", "password": "BxBH8#?_qN79VLem", "email": "abbasogaji@gmail.com", "role": "vadiRWrole"},
         "vadiuser03": {"Fullname": "Pietro Montino", "password": "2QDJ=XwVfw_5FbZ%", "email": "pietro.montino@gmail.com", "role": "vadiRWrole"},
         "vadiuser04": {"Fullname": "Alessandro legnazzi", "password": "b_8CMHTf_t56q!#x", "email": "alessandro.legnazzi01@gmail.com", "role": "vadiRWrole"},
         # "lomtuser01": {"Fullname": "Kirill Vechera", "password": "AZrxSQD2y@HuHhPR", "email": "lomtservice@gmail.com", "role": "lomtRWrole", "space": "Lomt", "indexpattern": "ich.*"},
         # "lomtuser02": {"Fullname": "Kirill Vechera", "password": "HRT8ea9_$YqAjeN7", "email": "lomtservice@gmail.com", "role": "lomtRrole", "space": "Lomt", "indexpattern": "ich.*"},
         # "lomtuser03": {"Fullname": "Kirill Vechera", "password": "%k66Pyy*UCN7$Uhg", "email": "lomtservice@gmail.com", "role": "lomtRrole", "space": "Lomt", "indexpattern": "ich.*"},
         # "kcovriuser01": {"Fullname": "Petri Louhelainen", "password": "qF8sB-mmT2DBj^aV", "email": "petri@kamuhealth.com", "role": "kcovriRWrole", "space": "Kcovri", "indexpattern": "kcovri.*"},
         # "kcovriuser02": {"Fullname": "Aaro Korhonen", "password": "un6Ny&#hrZkN#d=#", "email": "Aaro@kamuhealth.com", "role": "kcovriRWrole", "space": "Kcovri", "indexpattern": "kcovri.*"},
         # "kcovriuser03": {"Fullname": "Seppo Salorinne", "password": "M9_NgLF6m8Uv_#Bu", "email": "seppo@kamuhealth.com", "role": "kcovriRrole", "space": "Kcovri", "indexpattern": "kcovri.*"},
         # "kcovriuser04": {"Fullname": "Anna Lindahl", "password": "g&kVVc$_S?F@#6JP", "email": "anna.lindahl@helsinki.fi", "role": "kcovriRrole", "space": "Kcovri", "indexpattern": "kcovri.*"},
         "captainxuser01": {"Fullname": "Michalis Timoloen", "password": "!FeN5=4_^5gqZ-4j", "email": "mitimo@gmail.com", "role": "captainxRWrole"},
         "captainxuser02": {"Fullname": "Michalis Timoloen", "password": "94nhWWUH!S@AT_^G", "email": "mitimo@gmail.com", "role": "captainxRWrole"},
         "captainxuser03": {"Fullname": "Michalis Timoloen", "password": "KecqL9u?BXgXfp+@", "email": "mitimo@gmail.com", "role": "captainxRrole"},
         "captainxuser04": {"Fullname": "Michalis Timoloen", "password": "a7sNpxkwEA83LK=+", "email": "mitimo@gmail.com", "role": "captainxRrole"},
         "covid@homeuser01": {"Fullname": "Dries Oeyen", "password": "RQKmP5j!@hGtKd_j", "email": "engineering@bewellinnovations.com", "role": "covid@homeRWrole"},
         "covid@homeuser02": {"Fullname": "Dries Oeyen", "password": "4=_URuRWn2-uwW4?", "email": "engineering@bewellinnovations.com", "role": "covid@homeRWrole"},
         "covid@homeuser03": {"Fullname": "Dries Oeyen", "password": "?tr&Z?Df+Vc6a2dk", "email": "engineering@bewellinnovations.com", "role": "covid@homeRWrole"},
         # "cov-artuser01": {"Fullname": "JAKEZ ROLLAND", "password": "Fd##WYe5gN&DLz%d", "email": "jakez.rolland@biologbook.fr", "role": "cov-artRWrole", "space": "Cov-art", "indexpattern": "cov-art.*"},
         # "cov-artuser02": {"Fullname": "MARIE CODE", "password": "Ghy+$p?cP8-4x@2B", "email": "marie.codet@biologbook.fr", "role": "cov-artRWrole", "space": "Cov-art", "indexpattern": "cov-art.*"},
         "care4coviduser01": {"Fullname": "George Labropoulos", "password": "h?23nQtDT%eZ9swY", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRWrole"},
         "care4coviduser02": {"Fullname": "George Labropoulos", "password": "%QU8QtptqF6Y85@U", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRWrole"},
         "care4coviduser03": {"Fullname": "George Labropoulos", "password": "e7&j%7?s4+PAAwdH", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRWrole"},
         "care4coviduser04": {"Fullname": "George Labropoulos", "password": "^^VhJF6!?6dWR@3a", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRWrole"},
         "care4coviduser05": {"Fullname": "George Labropoulos", "password": "Xjd*nKE7dbB@Yan$", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRWrole"},
         "care4coviduser06": {"Fullname": "George Labropoulos", "password": "hF@*7$Gx3g&B9eQ6", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRrole"},
         "care4coviduser07": {"Fullname": "George Labropoulos", "password": "7VkQ7a_!h_q9&UhE", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRrole"},
         "care4coviduser08": {"Fullname": "George Labropoulos", "password": "U5kyM@6ZWVk+GqhR", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRrole"},
         "care4coviduser09": {"Fullname": "George Labropoulos", "password": "VhDcj#pL&ja7?^kS", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRrole"},
         "care4coviduser10": {"Fullname": "George Labropoulos", "password": "yH3@+-vRXXW5zW3j", "email": "glabropoulos@innovationsprint.eu", "role": "care4covidRrole"},
         "trajectuser01": {"Fullname": "Martí Zamora-Casals", "password": "UrktMY$2MCU3=w+J", "email": "marti@amalfianalytics.com", "role": "trajectRWrole"},
         "trajectuser02": {"Fullname": "Martí Zamora-Casals", "password": "fYMR5gU78pk@B9$&", "email": "marti@amalfianalytics.com", "role": "trajectRWrole"},
         "trajectuser03": {"Fullname": "Martí Zamora-Casals", "password": "*kr%_yqQk!AB55Qm", "email": "marti@amalfianalytics.com", "role": "trajectRrole"},
         "trajectuser04": {"Fullname": "Martí Zamora-Casals", "password": "Sw+65Ad@mb-%h4RM", "email": "marti@amalfianalytics.com", "role": "trajectRrole"},
         "c-armuser01": {"Fullname": "Frederik Andersen", "password": "!3PmLp$fTDc+7YYc", "email": "fa@softbrik.com", "role": "c-armRWrole"},
         "c-armuser02": {"Fullname": "Almir Zulic", "password": "9W6Gm5s7*5z6pj=s", "email": "almir@softbrik.com", "role": "c-armRWrole"},
         "c-armuser03": {"Fullname": "Oussema Hedri", "password": "HVdGe5?NV#^q9Q+z", "email": "oh@softbrik.com", "role": "c-armRWrole"},
         "c-armuser04": {"Fullname": "Michael Bøcker-Larsen", "password": "29-wxh6K*rMh4MVG", "email": "mbl@softbrik.com", "role": "c-armRrole"},
         "c-armuser05": {"Fullname": "Romit Choudhury", "password": "WZ325_$gC7^TxATH", "email": "rc@softbrik.com", "role": "c-armRrole"},
         "ddrehabuser01": {"Fullname": "Valentina Simonetti", "password": "YL-B7r5F_^tgV5h^", "email": "valentinasimonetti@ab-acus.eu", "role": "ddrehabRWrole"},
         "ddrehabuser02": {"Fullname": "Walter Baccinelli", "password": "phj3R@T#Q83SrNvV", "email": "walterbaccinelli@ab-acus.eu", "role": "ddrehabRWrole"},
         "ddrehabuser03": {"Fullname": "Laura Giani", "password": "S9PaYQh^_x3e4qvp", "email": "lauragiani@ab-acus.eu", "role": "ddrehabRWrole"},
         "madcapuser01": {"Fullname": "Marko Vujasinovic", "password": "Z2&KF$f+Pd$wst&a", "email": "marko.vujasinovic@gmail.com", "role": "madcapRWrole"},
         "madcapuser02": {"Fullname": "Alessio Gugliotta", "password": "XWE$YftT^3&s_Zn3", "email": "admin@avatr-srl.it", "role": "madcapRWrole"},
         "covid19triage01": {"Fullname": "Alexander Gruschina", "password": "Z^+@qXy3eGjL6v&r", "email": "gruschina@symptoma.com", "role": "covid19triageRWrole"},
         "covid19triage02": {"Fullname": "Roland Ortner", "password": "7Hzg*u6BPZ@gkFRk", "email": "ortner@symptoma.com", "role": "covid19triageRWrole"},
         "covid19triage03": {"Fullname": "Thomas Lutz", "password": "6T?^Su2H_j94AzL3", "email": "lutz@symptoma.com", "role": "covid19triageRWrole"},
         "covid19triage04": {"Fullname": "Laura Rodriguez", "password": "3w^j6ub&uF8yaRBq", "email": "rodriguez@symptoma.com", "role": "covid19triageRrole"},
         "covid19triage05": {"Fullname": "Stefanie Gruarin", "password": "a#UnW&A4hP_qL7&y", "email": "gruarin@symptoma.com", "role": "covid19triageRrole"},
         "covid19triage06": {"Fullname": "Andreas Fötschl", "password": "HpEm3H!Br9?_JA4V", "email": "foetschl@symptoma.com", "role": "covid19triageRrole"},
         "segtnanuser01": {"Fullname": "Eivind Antonsen Segtnan", "password": "z?JyJYB!UCrU28#s", "email": "eivind.antonsen.segtnan@gmail.com", "role": "segtnanRWrole"},
         "segtnanuser02": {"Fullname": "Farzin Kamari", "password": "5%$aQ*JB5Aq&VTTk", "email": "kamari.farzin@gmail.com", "role": "segtnanRWrole"},
         "segtnanuser03": {"Fullname": "Samad Najjar-Ghabel", "password": "M8dykxJbUFUU-MZU", "email": "samad.najjar@gmail.com", "role": "segtnanRWrole"},
         "segtnanuser04": {"Fullname": "Amir Mehdizadeh", "password": "a&#Wf_M7HEsKE#Ky", "email": "amir0mehdizadeh@gmail.com", "role": "segtnanRWrole"},
         "segtnanuser05": {"Fullname": "Mohammad Ghoreishi", "password": "ZsL@J^YtpCbV69Uv", "email": "mohagh22@gmail.com", "role": "segtnanRWrole"}
         # "" : {"Fullname" : "", "password" : "","email" : "", "role" : "", "space" : "", "indexpattern" : ""},
         # "" : {"Fullname" : "", "password" : "","email" : "", "role" : "", "space" : "", "indexpattern" : ""},
         }

superuser = 'elastic'
password = 'Sandb0x2020'
HOST_KIB = 'dmht-kibana'
HOST_ELS = 'dmht-elasticsearch'
#superuser = 'elastic'
#password = 'sandbox-test'
#HOST_KIB = '188.34.202.183'
#HOST_ELS = '188.34.202.183'
spaces = {"Aviate": {"deployment": "c", "kib_index_pattern": ["aviate.*", "opensource.*", "data.catalogue"]},
          "Vadi": {"deployment": "c", "kib_index_pattern": ["vadi.*", "opensource.*", "data.catalogue"]},
          # "Lomt": {"deployment": "ich", "kib_index_pattern": ["ich.*", "opensource.*"]},
          # "Kcovri": {"deployment": "l", "kib_index_pattern": ["kcovri.*", "opensource.*"]},
          "C-at-h": {"deployment": "c", "kib_index_pattern": ["c@h.*", "opensource.*", "data.catalogue"]},
          "Covid-at-home": {"deployment": "c", "kib_index_pattern": ["covid@home.*", "opensource.*", "data.catalogue"]},
          # "Cov-art": {"deployment": "l", "kib_index_pattern": ["cov-art.*", "opensource.*"]},
          # "Gastonscholar": {"deployment": "l", "kib_index_pattern": ["gastonscholar.*", "opensource.*"]},
          "Care4covid": {"deployment": "c", "kib_index_pattern": ["care4covid.*", "opensource.*", "data.catalogue"]},
          "Traject": {"deployment": "c", "kib_index_pattern": ["traject.*", "opensource.*", "data.catalogue"]},
          "Segtnan": {"deployment": "c", "kib_index_pattern": ["sermas.*", "opensource.*", "data.catalogue"]},
          "C-arm": {"deployment": "c", "kib_index_pattern": ["c-arm.*", "opensource.*", "data.catalogue"]},
          "Madcap": {"deployment": "c", "kib_index_pattern": ["madcap.*", "opensource.*", "data.catalogue"]},
          "Covid19triage": {"deployment": "c", "kib_index_pattern": ["covid19triage.*", "opensource.*", "data.catalogue"]},
          "Ddrehab": {"deployment": "c", "kib_index_pattern": ["ddrehab.*", "opensource.*", "data.catalogue"]},
          "Captain-x": {"deployment": "c", "kib_index_pattern": ["captain-x.*", "opensource.*", "data.catalogue"]}
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
