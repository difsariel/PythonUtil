import codecs


def main():
    with codecs.open("D:\Downloads\98五笔单字全码拆分表\98拆分.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = ["\t".join(l.strip().split("\t")[:2]) for l in lines]

    with codecs.open("D:\Downloads\98wubi.txt", "w", encoding="utf-8") as f:
        f.writelines("\n".join(lines))


if __name__ == "__main__":
    main()
