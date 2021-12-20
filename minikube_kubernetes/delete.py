from kubernetes import client, config
from kubernetes.client.rest import ApiException
config.load_kube_config() # or config.load_kube_config()

configuration = client.Configuration()
api_instance = client.CoreV1Api()
    
try:
    api_response = api_instance.delete_namespaced_pod(name="jj4", namespace="default")
    print(api_response)
except ApiException as e:
    print("Exception when calling CoreV1Api->delete_namespaced_pod: %s\n" % e)