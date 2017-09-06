from jnius import autoclass


if __name__ == "__main__":
    autoclass('java.lang.System').out.println('Hello world')
    Test = autoclass('Test')
    Test.test()
