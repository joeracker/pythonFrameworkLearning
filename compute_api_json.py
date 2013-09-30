import json, os
from pprint import pprint


def get_token_id():
    return 12345

def get_tenant_id():
    return 90987

def get_image_ID():
    return 23523

def get_flavor_ID():
    return ["debian", "ubuntu"]
    
def update_cached_auth_response(dict, auth_object):
    return 334333666

def get_compute_public_URL(service_name, region, auth_json):
    for x in auth_json["access"]["serviceCatalog"]:
        if x['name'] == service_name:
            for y in x["endpoints"]:
                #pprint(y)
                if y["region"] == region:
                    #pprint()
                    return y["publicURL"]

# Load json
f = open('sample_auth_response.json', 'r')
auth = json.load(f)

# #####################################
# a. get DFW cloud server endpoint
endpoint = get_compute_public_URL("cloudServersOpenStack", "DFW", auth)
print(endpoint)
