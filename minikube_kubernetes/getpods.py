import requests
import json




URL = "http://localhost:8088/api/v1/namespaces/default/pods/"

resp = requests.get(url=URL)
pod_json = json.loads(resp.content)

pods = pod_json["items"]
for i in pods:
    name = i["metadata"]["name"]
    uid = i["metadata"]["uid"]
    print("Pod details:\nName: " +name+ " \nUID: " +uid)

