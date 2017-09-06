import jnius_config

jnius_config.add_classpath(u"C:\\Users\lsx\pyjnius\yz-guizhou-spellcheck-0.2.0-SNAPSHOT-jar-with-dependencies.jar")

import jnius
import os
import re
import bs4
import pandas as pd
import pymysql

if __name__ == "__main__":
    db = pymysql.connect("90.90.90.101", "root", "1cc886c6c6b8", "dc_news", use_unicode=True, charset="utf8")
    cursor = db.cursor()

    input_path = u"C:\\Users\lsx\dchtml"
    folder_regex = re.compile(u".+\\\system\\\[0-9]+\\\[0-9]+\\\[0-9]+")
    file_dict_list = list()
    SpellCheckerClient = jnius.autoclass("com.yeezhao.guizhou.client.SpellCheckerClient")
    spellCheckerClient = SpellCheckerClient()

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
                        title = soup.select("title")[0].getText()
                        tag_p_list = soup.select("p")
                        content = ""
                        for tag in tag_p_list:
                            tag_text = tag.getText()
                            content += "。" + tag_text
                        if len(content) < 1:
                            continue
                        content = content.replace(u"\n", "")
                        content = content.replace(u"\r", "")
                        path_parts = folder_name.split(u"system\\")
                        date_parts = path_parts[1].split(u"\\")
                        publish_date = u"-".join(date_parts)
                        doc_id = folder_name.split("lsx\\")[1] + u"\\" + file_name

                        title_misspell = spellCheckerClient.query(title)
                        content_misspell = spellCheckerClient.query(content)

                        insert_sql = '''insert into news_spell_check(docId, publishDate, title, content, titleMisspell, contentMisspell) values("%s", "%s", "%s", "%s", "%s", "%s")'''
                        try:
                            cursor.execute(insert_sql % (doc_id, publish_date, title, content, title_misspell, content_misspell))
                            db.commit()
                        except Exception as e:
                            print(e)
                            db.rollback()

                        # file_dict = dict([("docId", doc_id), ("title", title), ("content", content),
                        #                   ("publishDate", publish_date), ("title_misspell", title_misspell),
                        #                   ("content_miss_spell", content_miss_spell)])
                        # file_dict_list.append(file_dict)

                        print(folder_name + u"\\" + file_name + " was parsed successfully!")
                except Exception as e:
                    print(e)

    db.close()
    # file_df = pd.DataFrame(file_dict_list)
    # file_df.to_csv(u"C:/Users/lsx/dchtml.csv", index=False, encoding="utf-8")
    # print(file_df["title_miss_spell", "content_miss_spell"])
