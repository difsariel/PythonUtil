import xlrd
import json
import codecs
import os


def read_xls(file_path):
    xls_file = xlrd.open_workbook(file_path)
    xls_sheet = xls_file.sheets()[0]
    rows = xls_sheet.get_rows()
    lines = []
    skip = 0
    for row in rows:
        if skip == 0:
            skip += 1
            continue
        cur_dict = dict()
        for i in range(len(row)):
            if i == 1:
                cur_dict["title"] = row[i].value
            if i == 2:
                cur_dict["url"] = row[i].value
            if i == 3:
                cur_dict["media"] = row[i].value
        if len(cur_dict) != 3:
            print(cur_dict)
            continue
        lines.append(cur_dict)

    lines = [json.dumps(r, ensure_ascii=False) for r in lines]
    return lines


def write_lines(lines, file_path):
    with codecs.open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.writelines(line + "\n")


def main():
    dir_path = "D:\Downloads\yuqingtong"
    output_path = "D:\Downloads\yuqingtong.json"
    files = os.listdir(dir_path)
    result = []
    for file in files:
        cur = read_xls(os.path.join(dir_path, file))
        result.extend(cur)
    write_lines(result, output_path)


if __name__ == "__main__":
    main()
