import http.client as httplib

class Connectivity():

    @classmethod
    def internet_access(self) -> bool:
        conn = httplib.HTTPSConnection("1.0.0.2", timeout=5)
        try:
            conn.request("HEAD", "/")
            return True
        except Exception:
            return False
        finally:
            conn.close()

    