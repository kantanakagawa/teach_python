from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import json
import requests

url_1 = "http://localhost/api/threads"
url_2 = "http://localhost/api/checks"

res_1 = requests.get(url_1)
res_2 = requests.get(url_2)

respons_1 = json.loads(res_1.text)
respons_2 = json.loads(res_2.text)

res_1 = len(respons_1)
res_2 = len(respons_2)

urls = []
for i in range(res_1):
    url = respons_1[i]["url"]
    urls.append(url)

user_id_list = []
for i in range(res_1):
    id = respons_1[i]["id"]
    user_id_list.append(id)

checks = []  # チェック
for i in range(res_2):
    check = respons_2[i]["check"]
    checks.append(check)

thread_id_list = []  # スレッドid
for i in range(res_2):
    thread_id = respons_2[i]["thread_id"]
    thread_id_list.append(thread_id)

# チェックとurlを紐付ける

a = defaultdict(list)

for thread_id in thread_id_list:
    for user_id in user_id_list:
        if thread_id == user_id:
            user_index = user_id_list.index(user_id)
            thread_index = thread_id_list.index(thread_id)
            check = respons_2[thread_index]["check"]
            url = respons_1[user_index]["url"]
            index = url.find("day")
            url = url[index:]
            a[check].append(url)


np_check_url = np.array([])

for i in a[1]:
    np_check_url = np.append(np_check_url, i)

# print(np_check_url)

url, counts = np.unique(np_check_url, return_counts=True)

print(url)
print(counts)

x = url
y = counts
plt.barh(x, y)
plt.show()
