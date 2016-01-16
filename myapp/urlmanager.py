# encoding=utf8
import datetime
import copy

from myapp.db_operation import ShelveOperation

# 存储， 更新，比对


def update_url(url, status=None):
    """
        两种情况：
        1. 第一次， 没有记录， 则保存记录， 默认status=0
        2. 有记录更新记录，如果指定了status的值，则使用指定的值，没有的话，则使用默认值0
    """
    with ShelveOperation() as S:
        if status is not None:  # 指定了强制刷新status的值，则更新status
            new_value = {"url": url, "status": status, "last_update": datetime.datetime.now()}
        else:
            value = S.get_value_by_key(url)  # 没有指定， 只更新时间戳
            if value:  # 之前存在记录
                _value = copy.deepcopy(value)
                _value.update({"late_update": datetime.datetime.now()})
                new_value = _value
            else:  # 第一次记录，默认认为没有访问过
                new_value = {"url": url, "status": 0, "last_update": datetime.datetime.now()}
        S.update_db(key=url, value=new_value)
    return True


def get_non_visited_urls():
    non_visited_urls = []
    with ShelveOperation() as S:
        all_urls = S.get_all_values()
        for key, value in all_urls:
            if value["status"] == 0:
                non_visited_urls.append(key)
            else:
                continue
    return non_visited_urls



