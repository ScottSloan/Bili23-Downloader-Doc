import os
import json
import requests
from urllib.parse import urlencode

class CloudreveAPI:
    def __init__(self, api_url: str, email: str, password: str, version: str):
        self.api_url = api_url
        self.email = email
        self.password = password
        self.version = version

        self.access_token = ""

        self.get_access_token()

    def get_access_token(self):
        url = f"{self.api_url}/session/token"

        body = {
            "email": self.email,
            "password": self.password
        }

        resp = requests.post(url, headers = self.get_headers(), json = body)
        resp_json: dict = json.loads(resp.text)

        if resp_json["code"] == 0:
            self.access_token = resp_json["data"]["token"]["access_token"]

    def query_file_direct_link(self, file_name: str):
        params = {
            "uri": f"cloudreve://my/Bili23_Downloader/{self.version}/{file_name}",
            "extended": "true",
            "folder_summary": "false"
        }

        url = f"{self.api_url}/file/info?{urlencode(params)}"

        req = requests.get(url, headers = self.get_headers())
        req_json: dict = json.loads(req.text)

        if req_json["code"] == 0:
            return req_json["data"]["extended_info"]["direct_links"][0]["url"]
        
    def get_headers(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
        }

        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
            
        return headers

class GitHubAPI:
    def __init__(self, token: str):
        self.token = token

    def get_latest_release(self):
        url = f"https://api.github.com/repos/ScottSloan/Bili23-Downloader/releases/latest"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        resp = requests.get(url, headers = headers)
        resp_json: dict = json.loads(resp.text)

        return resp_json

    def save_project_info(self, resp_json: dict):
        tag_name = resp_json.get("tag_name")
        version = tag_name.lstrip("v")

        cloudreve_api = os.getenv("CLOUDREVE_API")
        cloudreve_email = os.getenv("CLOUDREVE_EMAIL")
        cloudreve_password = os.getenv("CLOUDREVE_PASSWORD")

        self.cloudreve = CloudreveAPI(cloudreve_api, cloudreve_email, cloudreve_password, version)

        sha256_dict = {entry.get("name"): entry.get("digest").removeprefix("sha256:") for entry in resp_json.get("assets")}

        self.update_project_json(version)
        self.update_download_table_json(version, sha256_dict)

    def update_project_json(self, version: str):
        with open("project.json", "w", encoding = "utf-8") as f:
            data = {
                "version": version,
            }

            f.write(json.dumps(data, ensure_ascii = False, indent = 4))

    def update_download_table_json(self, version: str, sha256_dict: dict):
        with open("download_table.json", "r", encoding = "utf-8") as f:
            download_table = json.loads(f.read())

        with open("download_table.json", "w", encoding = "utf-8") as f:
            for entry in download_table:
                name = entry.get("name").replace("{version}", version)

                if name in sha256_dict.keys():
                    entry["sha256"] = sha256_dict.get(name)
                    entry["onedrive_url"] = self.cloudreve.query_file_direct_link(name)

            f.write(json.dumps(download_table, ensure_ascii = False, indent = 4))

    def update_info(self):
        release_info = self.get_latest_release()

        self.save_project_info(release_info)

if __name__ == "__main__":
    github_token = os.getenv("ACCESS_TOKEN")

    api = GitHubAPI(github_token)
    latest_release = api.update_info()