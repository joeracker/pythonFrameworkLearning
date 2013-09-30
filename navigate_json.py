import json, os
from pprint import pprint
#(item for item in auth["access"]["serviceCatalog"] if item["name"] == "cloudServersOpenStack").next()


def get_compute_public_URL(service_name, region, auth_json):
    for x in auth_json["access"]["serviceCatalog"]:
        if x['name'] == service_name:
            for y in x["endpoints"]:
                #pprint(y)
                if y["region"] == region:
                    #pprint()
                    return y["publicURL"]

def get_token_id(auth_json):
    return auth_json["access"]["token"]["id"]

def get_tenant_id(auth_json):
    return auth_json["access"]["token"]["tenant"]["id"]

def get_image_ID(dict):
    return dict["image_ID"]
    
def get_flavor_ID():
    return ["debian", "ubuntu"]
    
def update_cached_auth_response(dict, auth_object):
    new_auth = dict["auth_response"] = auth_object
    return dict

# Load json
f = open('sample_auth_response.json', 'r')
auth = json.load(f)

# #####################################
# a. get DFW cloud server endpoint
endpoint = get_compute_public_URL("cloudServersOpenStack", "DFW", auth)
print(endpoint)

# #####################################
# b. New dict called compute_api_info
file_path = "compute_api_info.json"
os.remove(file_path)
compute_api_info = {
                    "auth_response":None,
                    "image_ID":"PooOnAStick",
                    "flavors": [
                            {"flavor_ID":"ubuntu1"},
                            {"flavor_ID":"debian1"}
                        ]
                    }
f = open(file_path, 'w')
json.dump(compute_api_info, f)

# #####################################
# c. get token and tenant ids
print("Token = %s" % get_token_id(auth))
print("Tenant = %s" % get_tenant_id(auth))




# #####################################
# d. return image, flavor and update auth
print("ImageID = %s" % get_image_ID(compute_api_info))
print("flavorID = %s" % get_flavor_ID())
print("New dict with updated Auth = %s" % update_cached_auth_response(compute_api_info, 12345))