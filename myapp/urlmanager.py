# encoding=utf8
import datetime


from db_operation import ShelveOperation

# 存储， 更新，比对


def update_url(url, status):
    S = ShelveOperation()
    S.update_db(key=url, value={"url": url, "status": status, "last_update": datetime.datetime.now()})
    return True


def get_non_visited_urls():
    S = ShelveOperation()
    non_visited_urls = []
    all_urls = S.get_all_values()
    for key, value in all_urls:
        if value["status"] == 0:
            non_visited_urls.append(key)
        else:
            continue
    return non_visited_urls



