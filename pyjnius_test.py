import jnius_config

jnius_config.add_classpath(u"D:\pyjnius\SpellChecker.jar")

import jnius

if __name__ == "__main__":
    SpellChecker = jnius.autoclass("spellchecker.SpellChecker")
    spellChecker = SpellChecker()
    spellChecker.loadDict(u"D:/分析项目/错别字识别/spellDict.txt")
    print(spellChecker.check(u"贵州省深泰文明委"))
