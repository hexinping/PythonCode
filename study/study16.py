# #_*_ coding:utf-8 _*_

# object为父类
class Song(object):

    def __init__(self, lyrics):

        self.lyrics = lyrics

    def sing_me_a_song(self):
        for letter in self.lyrics:
            print letter


class PopSong(Song):
    def __init__(self, ly):
        super(PopSong, self).__init__(ly)  # 调用父类的方法

    def sing_me_a_song(self):              # 重载父类的方法
        print "我不喜欢唱歌-----"


def class_func():

    song = Song("hexinping")
    song.sing_me_a_song()


if __name__ == "__main__":

    print "class---------"
    class_func()