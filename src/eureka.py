from py_eureka_client.eureka_client import EurekaClient

def initialize_eureka_client() -> EurekaClient:
    client = EurekaClient(eureka_server="http://localhost/eureka/v1", 
                          app_name="fleam-recommender", 
                          instance_port=8000)
    client.start()
    return client

eureka_client = initialize_eureka_client()