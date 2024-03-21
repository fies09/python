os.rename('修改的文件名', '修改后的文件名')
os.remove('要删除的文件')

# os.mkdir（目录名）：创建目录，若目录已存在则报错
os.mkdir(r".\testA")

# 创建多级目录，若目录存在则报错
os.makedirs(r".\a\b\c")

# os.rmdir(目录名)：删除目录
os.rmdir(r".\testA")

# os.path.exists(目录或文件名)：判断目录或文件是否存在，返回布尔结果
isExists = os.path.exists(r".\testA")
print(isExists)     # 输出结果：False


# os.path.isdir(目录路径)：判定是否是目录，返回布尔结果
result = os.path.isdir(r".")
print(result)   # 输出结果：True


# os.listdir(目录路径)：以列表的形式返回指定目录下的所有文件名
listPath = os.listdir('.')  # 返回当前目录下所有文件名
print(listPath)     # 输出结果：['.git', '.idea', 'aaa.py', 'bbb.py', 'README.md', 'test.py']


# os.getcwd()：获取当前所在目录路径
curPath = os.getcwd()
print(curPath)  # 输出结果：D:\_git\cdzg-platform


# os.chdir(目录路径)：修改工作目录
os.chdir(r"..")
print(os.getcwd())  # 输出结果：D:\_git
os.chdir(r".\cdzg-platform")


# 获取当前运行文件的真实全路径，而非链接路径
curRelPath = os.path.realpath(__file__)
print(curRelPath)   # 输出结果：D:\_git\cdzg-platform\bbb.py

# 分割文件目录路径与目录名，返回元组结果
pathSplit = os.path.split(curRelPath)
print(pathSplit)    # ('D:\\_git\\cdzg-platform', 'bbb.py')


# 在当前进程中打开一个子shell（子进程）来执行系统命令，类似于在cmd命令行执行命令。
cmd = os.system("dir")
print(cmd)  # 返回当前目录的文件信息


