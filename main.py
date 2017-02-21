import Parser as p
import File as f


uri = "http://careercenter.am/ccidxann.php"
data = p.Parser.Parse(uri)
f.File.Save("C:\\tmp\\test.txt",data)
print(f.File.Read("C:\\tmp\\test.txt"))
print("Done !!!!")


