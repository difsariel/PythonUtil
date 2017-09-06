import os
import re

import bs4
import pandas as pd
import pymysql

if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect("108.108.108.244", "root", "root", "dc_article")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()

    input_path = u"C:\\Users\lsx\dchtml\zonghe"
    folder_regex = re.compile(u".+dchtml\\\[a-z]+\\\system\\\\2017\\\.+")
    file_dict_list = list()
    for folder_name, sub_folders, file_names in os.walk(input_path):
        matcher = folder_regex.search(folder_name)
        if matcher is None:
            continue
        if len(file_names) > 0:
            for file_name in file_names:
                if not file_name.endswith("html"):
                    continue
                try:
                    with open(folder_name + u"\\" + file_name, encoding="gbk") as f:
                        lines = f.read()
                        soup = bs4.BeautifulSoup(lines)
                        tag_p_list = soup.select("p")
                        title = soup.select("title")[0].getText()
                        content = ""
                        path_parts = folder_name.split(u"system\\")
                        date_parts = path_parts[1].split(u"\\")
                        publish_date = u"-".join(date_parts)
                        doc_id = folder_name.split("lsx\\")[1] + u"\\" + file_name
                        for tag in tag_p_list:
                            tag_text = tag.getText()
                            content += tag_text
                        if len(content) < 1:
                            continue
                        content = content.replace(u"\n", "")
                        content = content.replace(u"\r", "")
                        file_dict = dict(
                            [("docId", doc_id), ("title", title), ("content", content), ("publishDate", publish_date)])
                        file_dict_list.append(file_dict)
                        print(folder_name + u"\\" + file_name + " was parsed successfully!")
                except:
                    pass
    file_df = pd.DataFrame(file_dict_list)
    file_df.to_csv(u"C:/Users/lsx/dchtml.csv", index=False, encoding="utf-8")
    print(file_df)
