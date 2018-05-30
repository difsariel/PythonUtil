# -*- encoding: utf-8 -*-
import re
from bosonnlp import BosonNLP
import json


def boson_cluster(nlp, docs):
    clusters = nlp.cluster(docs)
    clusters = sorted(clusters, key=lambda cluster: cluster['num'], reverse=True)
    return clusters


def print_cluster(docs, idx, result):
    print('=' * 50)
    print('第%d个聚类中共有%s份文档,如下:' % (idx + 1, result['num']))
    for doc in result['list']:
        print(docs[doc])
    print('-' * 20)
    print('本聚类的中心文档为:')
    print(docs[result['_id']])


if __name__ == "__main__":
    # 注意：在测试时请更换为您的API token
    nlp = BosonNLP('Pf9PQqVF.15107.z0WLjI-dZeOu')

    with open("/Users/lsx/Desktop/文本聚类/data.json/part-00000", "r") as input_file:
        lines = input_file.readlines()[0:10]
        text_list = [json.loads(line)["text"] for line in lines]
        print(text_list[0])
        cluster_result = boson_cluster(nlp, text_list)
        for idx, cluster in enumerate(cluster_result):
            print_cluster(text_list, idx, cluster)

