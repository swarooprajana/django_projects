import pybase64


def convert(k):
    k = open('/home/vasu/Vasu/freshersbatch4/project1/pics/image2.jpg', "rb")
    h = pybase64.b64encode(k.read())
    return h


