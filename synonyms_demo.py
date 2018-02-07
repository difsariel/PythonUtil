import synonyms

print("人脸: %s" % (synonyms.nearby("人脸")))
print("识别: %s" % (synonyms.nearby("识别")))
print("NOT_EXIST: %s" % (synonyms.nearby("NOT_EXIST")))

print("=" * 50)

sen1 = "发生历史性变革"
sen2 = "发生历史性变革"
r = synonyms.compare(sen1, sen2, seg=True)
print("发生历史性变革 vs 发生历史性变革:", r)

print("=" * 50)

synonyms.display("飞机")
