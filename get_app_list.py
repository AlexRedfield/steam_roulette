import json
from db_utils import init_db,insert_data_all
from sqlalchemy import Column, INTEGER
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import requests
Base = declarative_base()
def download_page(url): # 下载页面
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }).text

class GameInfo(Base):
    __tablename__ = 'game_info'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    app_id = Column(VARCHAR(256), nullable=False)
    name = Column(VARCHAR(256), nullable=False)

    def __init__(self, app_id, name):
        self.app_id = app_id
        self.name = name

def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]

if __name__ == '__main__':
    app_str=download_page("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
    json_app=json.loads(app_str)
    app_list=json_app['applist']['apps']

    for subgroup in list_split(app_list,1000):
        game_list=[]
        for dict_info in subgroup:
            game_list.append(GameInfo(dict_info['appid'], dict_info['name']))
        insert_data_all(game_list)
