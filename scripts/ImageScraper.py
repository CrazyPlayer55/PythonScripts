import requests

url = "https://www.reddit.com/"

headers = {}
data = requests.get(url, headers=headers).json()

for ch in data["data"]["children"]:
    pic_url = ch["data"].get("url_overridden_by_dest")
    if pic_url:
        file_name = pic_url.split("/")[-1]
        if not "." in file_name:
            continue
        with open(file_name, "wb") as f_out:
            print("Downloading {}".format(pic_url))
            c = requests.get(pic_url, headers=headers).content
            f_out.write(c)
