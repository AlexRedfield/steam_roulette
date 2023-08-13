from datetime import datetime

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# users表结构
class GameSession(Base):
    __tablename__ = 'steam_sessions'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    app_id = Column(VARCHAR(256), nullable=False)
    start_time = Column(DATETIME(), nullable=False)
    end_time = Column(DATETIME(), nullable=False)
    duration = Column(INTEGER, nullable=False)

    def __init__(self, app_id, start_time, end_time, duration):
        self.app_id = app_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration


def init_db(base):
    engine = create_engine(
        "mysql+pymysql://root:mysql877@localhost:3306/steam",
        encoding="utf-8",
        echo=True
    )
    base.metadata.create_all(engine)
    print('Create table successfully!')


def insert_data(new_session: GameSession):
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:mysql877@localhost:3306/steam", encoding="utf-8")
    # 创建DBSession类型
    dbs_ession = sessionmaker(bind=engine)

    # 创建session对象
    session = dbs_ession()
    # 插入单条数据
    # 创建新User对象

    # 添加到session
    session.add(new_session)
    # 提交即保存到数据库
    session.commit()

    # 关闭session
    session.close()
    print('insert into db successfully!')


def insert_data_all(params_list: list):
    # 初始化数据库连接
    engine = create_engine("mysql+pymysql://root:mysql877@localhost:3306/steam", encoding="utf-8")
    # 创建DBSession类型
    dbs_ession = sessionmaker(bind=engine)

    # 创建session对象
    session = dbs_ession()
    # 插入单条数据
    # 创建新User对象

    # 添加到session
    session.add_all(params_list)
    # 提交即保存到数据库
    session.commit()

    # 关闭session
    session.close()
    print('insert into db successfully!')


if __name__ == '__main__':
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_session = GameSession(app_id='Jack', start_time=now_time, end_time=now_time, duration=1)
    insert_data(new_session)
