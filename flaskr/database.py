"""
sqlalchemy
直接使用core内核，使用sql直接链接。
直接查询其他配置
!https://docs.sqlalchemy.org/en/14/tutorial/further_reading.html
"""
# !配置db

from sqlalchemy import create_engine

url = 'mysql+pymysql://root:liukai@localhost:3306/flaskr'
# 开启future参数，使用新风格，对链接池进行设置
engine = create_engine(url, future=True, pool_size=20, max_overflow=20)

# !直接封装一个链接，拒绝自动commit()
conn = engine.connect()
"""
手动提交connect()
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()

自动提交begin()
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )

"""
