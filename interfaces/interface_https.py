        import requests
        try:
            r = requests.post("https://example.com/endpoint", json={"data": formatted})
            print("[HTTPS] Status:", r.status_code)
        except Exception as e:
            print("[HTTPS ERROR]", e)
