import requests

REST_PORT = 8332
REST_HOST = "localhost"
REST_URL = f"http://{REST_HOST}:{REST_PORT}/rest/"
REST_METHOD_BLOCK = "block"
REST_METHOD_HASHBYHEIGHT = "blockhashbyheight"
REST_METHOD_CHAININFOS = "chaininfo.json"

def get_chaininfos():
    url = f"{REST_URL}{REST_METHOD_CHAININFOS}"
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    raise Exception("get_chaininfos failed with", req.text)

def get_block_for_height(height):
    hash = get_hash_for_height(height)
    url = f"{REST_URL}{REST_METHOD_BLOCK}/{hash}.json"
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    raise Exception("get_block_for_height failed with", req.text)

def get_hash_for_height(height):
    url = f"{REST_URL}{REST_METHOD_HASHBYHEIGHT}/{height}.json"
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()["blockhash"]
    raise Exception("get_hash_for_height failed with", req.text)
