# -*- coding: utf-8 -*- 
# @Time : 2022/4/1 9:28 
# @Author : crow
# @File : connection.py

import pymysql

from config import log

connect = pymysql.connect(
    host='192.168.111.112',  # 服务器名字
    port=3306,  # 端口号
    user='sqladm',  # 登录名
    passwd='&3yVer!0fVuiYx1j',  # 密码
    db='hc_exfollowup_center',  # 数据库名
    charset='utf8'
)

if __name__ == '__main__':
    # 创建游标对象
    cursor = connect.cursor()  # cursor当前的程序到数据之间的链接管道
    # 组装sql语句，需要查询的MySQL语句
    sql = 'SELECT * FROM t_fuc_doctor WHERE id =186'
    # 执行sql语句
    log.info(cursor.execute(sql))
    results = cursor.fetchall()
    for result in results:
        log.info(result)
    connect.close()
