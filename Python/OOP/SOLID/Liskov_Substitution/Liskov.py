# liskov substitution
# --> 상속에서 쓸 때 인터페이스(함수 시그니처) 명세 좀 따라
# = 리턴값을 맞춰라

class FileManager:
    def __init__(self, new_filename, fr_obj):
        self.f=open(new_filename, 'wt')
        self.fr = fr_obj

    def read_and_write(self):
        buf = self.fr.readline()
        if buf != 'eof':
            self.f.write(buf)
            return len(buf)
        else:
            print("end of file")

        
    def close(self):
        self.f.close()


class FileReader:
    def __init__(self, filename):
        self.f=open(filename, 'rt')

    def read(self):
        """
        fr.read() -> string
        ret -> 있으면 그 값
        아니면 'eof' : 
        """
        buf = self.f.readline()
        if buf:
            return buf
        else:
            return 'eof'


class NameReader(FileReader):
    def read(self):
        buf = self.f.readline()
        if buf:
            return 'name[' + buf[:-1] + ']' 
        else:
            return None


if __name__ == "__main__":
    fr = FileReader('text.txt')
    fm = fileManager('new_content1.txt', fr)
    
    res = fm.read_and_write()
    while res:
        