import random
import time
import webbrowser


def flash_web():
    url_list = ["http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58464",
        "http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58493",
        "http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58549",
        "http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58350",
        "http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58454",
        "http://www.zunyiol.com/index.php?m=content&c=index&a=show&catid=10&id=58421"]
    while True:
        url = random.choice(url_list)
        webbrowser.open_new_tab(url)
        time.sleep(3)


if __name__ == '__main__':
    flash_web()
