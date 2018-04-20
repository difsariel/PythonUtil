# -*- coding: utf-8 -*-

import docx

doc = docx.Document("D:\分析项目\智慧法院\法院标准\\2015人民法院案件信息业务标准\【原始文件】人民法院案件信息业务标准（2015）印发最终稿.docx")
fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)
    print(para.text)
