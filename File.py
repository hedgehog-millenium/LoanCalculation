class File:
    @classmethod
    def Save(cls,path,text):
        with open(path, 'w') as f:
            f.write(str(text))

    @classmethod
    def Read(cls,path):
        with open(path, 'r') as f:
            return f.read();