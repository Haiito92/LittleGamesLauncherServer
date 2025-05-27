import http.client

def fetch_root():
    conn = http.client.HTTPConnection("localhost", 8000)
    conn.request("GET", "/")
    response: http.client.HTTPResponse = conn.getresponse()
    print("Status:", response.status, response.reason)
    data: bytes = response.read()
    print("Response data:")
    print(data.decode())
    conn.close()

if __name__ == "__main__":
    fetch_root()