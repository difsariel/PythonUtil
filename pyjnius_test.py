import jnius_config

jnius_config.add_classpath(u"D:\pyjnius\MyAwesomeSpark.jar")

import jnius

if __name__ == "__main__":
    class_path = jnius_config.get_classpath()
    print(class_path)
    Test = jnius.autoclass('Test')
    Test.test()
