# Python简介和环境搭建

于 20世纪80年代末，Guido van Rossum发明了Python，初衷据说是为了打发圣诞节的无趣。1991年首次发布，是ABC语言的继承，同时也是一种脚本语言。取名时，Guido van Rossum认为它应该“短小，独特，还有一点神秘感”，他是英国著名剧团Monty Python的忠实粉丝，所以就取名Python了。

![](img/1.jpg)

图1 Monty Python剧团

牛人的世界我们无法企及，随便玩玩就玩出门流行的语言来。

编程语言众多，Python按照分类来讲，首先是动态语言，无需编译，然后是脚本语言。当然脚本语言这个特性在逐渐淡化，Python可以在Web、桌面、后台服务各种应用类型中占有一席之地。

Python从创建之后，到2000年发布了2.0版本，到2008年发布了3.0版本。到目前为止，2.*版本仍然是使用最广泛的版本，有一部分原因要归咎于3.0版本对2.*版本的不兼容。本系列教程会尽量使用最新的3.*版本来开发示例。

Python本身是开源的，我们可以从[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/) 下载Python从2.0.1开始到当前最新版（3.7.0）各个版本的的源码。

![python下载](img/2.png)
图2 Python源码下载

Python的跨平台特性，可以让开发者放心的选择自己喜欢的操作系统和开发工具来开发代码。Python
不仅可以在Windows、Mac OS X、Linux/Unix运行，也可以运行在移动设备上，后面我们会有单独的章节来具体介绍。

Python有很多值得我们称道的特性，这里就先不展开介绍了，“绝知此事要躬行”，我们先搭建出开发环境来，实现我们的第一个“Hello world”。

## 1.1.1  安装Python

我们可以到 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows//)下载windows下的Phthon安装文件，我们下载独立的安装文件进行安装。

![Python 安装文件下载](img/3.png)
Python安装文件下载（windows）

到[https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)下载Mac OS X的安装文件，
![Python 安装文件下载](img/4.png)
Python安装文件下载（Mac OS X）

到[https://www.python.org/download/other/](https://www.python.org/download/other/)下载其他平台的安装文件。
![Python 安装文件下载](img/5.png)
Python安装文件下载（其他平台）

Linux 下安装Python一般采用源码或则软件包管理器安装的方式。  下面分别介绍在不同操作系统下Python的安装方法。

### 1.1.1.1 Windows下安装Python

我们从下载安装文件之后，打开exe文件。

![Python windows安装](img/6.png)

注意上图中的标记的选项。通常我们会把Python安装的系统的PATH系统变量中，这样我们就可以在任何地方直接调用Python。当然也可以不安装，需要到Python的安装目录里调用python.exe。
选择自定义安装。

![Python windows安装](img/7.png)

这里注意pip一定要勾选上，这是默认的Python包管理工具，后面我们会继续介绍。点击下一步。

![Python windows安装](img/8.png)

这里我们可以自定义安装目录，添加环境变量等选项。点击安装。

![Python windows安装](img/9.png)

允许安装。
![Python windows安装](img/10.png)

安装完成之后，如果提醒我们修改系统PATH最大字符数限制的话，点击更改。
![Python windows安装](img/11.png)

安装成功后，关闭对话框。
![Python windows安装](img/12.png)

现在我们可以进行简单的测试了。如果你选择了将Python安装到PATH，直接命令行输入Python启动运行时，否则到Python的安装目录启动python.exe。

![Python windows安装](img/13.png)

输入简单的语句测试下。

![Python windows安装](img/14.png)

到此为止，Python在widonws上的安装完成了，下面我们看看在Mac OS X上如何安装。

### 1.1.1.2 Mac OS X 安装Python

目前Mac OS X 默认安装Python2.7，我们下载最新的安装包。

![Python Mac安装](img/15.png)

点击继续。

![Python Mac安装](img/18.png)

![Python Mac安装](img/19.png)

![Python Mac安装](img/21.png)

点击“安装”。

![Python Mac安装](img/22.png)

安装成功之后，如果要求我们安装SSL根证书的话，需要点击链接跳转到下载页面下载安装。其实，也可以直接通过pip来安装。

在使用pip之前，我们先对pip进行更新。

```shell
pip3 install --upgrade pip
```
![Python Mac安装](img/24.png)

之后执行命令安装certifi。

```shell
pip install certifi
```

下面我们来验证新安装的Python。

直接输入python，使用的还是Python2.7.

![Python Mac安装](img/25.png)

默认的环境变量，我们不去动，这里使用python3来启动。

![Python Mac安装](img/27.png)

### 1.1.1.3 Linux下 安装Python

__安装python__

在Linux下安装Python，一般采用源码安装的方式。首先下载源码。

```shell
$ sudo mkdir /usr/local/python3 # 创建安装目录

# 下载 Python 源文件
$ wget --no-check-certificate https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
# 注意：wget获取https的时候要加上：--no-check-certificate

$ tar -xzvf Python-3.7.0.tgz # 解压缩包

$ cd Python-3.7.0 # 进入解压目录
```

第二步是编译安装。

```shell
$ sudo ./configure --prefix=/usr/local/python3 # 指定创建的目录

$ sudo make

$ sudo make install
```

第三步是配置链接。因为很多Linux系统自带Python2.7，所以这里要配置一下软连接，使得我们可以使用python3 命令来启动Python3.7.

```shell
$ sudo ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```

如果使用 的是apt软件包管理器的系统，可以直接使用如下命令来安装：

```shell
apt-get install python3
```

__安装pip__

可以使用命令直接安装pip。

```shell
sudo yum install python-pip
```
或者

```shell
sudo apt-get install python-pip
```

简单测试同上。

### 1.1.2 包管理

在实际开发过程中，不可能所有功能都基于Python原生API来进行开发，很多第三方软件包为我们提供了很好的便利条件。安装和管理软件包分为手动和工具两种方式，下面我们简单介绍这两种方式。软件包管理工具为大家介绍pip和easy_install。


#### 1.1.2.1  手动安装

第一种方法是手动下载软件包，运行安装程序来安装。

比如我们想要使用Python-nmap组件去解析nmap的扫描结果，我们先手动下载安装包。

```shell
wget http://xael.org/pages/python-nmap-0.6.0.tar.gz
```

![Python 模块安装](img/28.jpg)

解压：

```shell
root@kali:~# tar xzf python-nmap-0.6.0.tar.gz
root@kali:~# cd python-nmap-0.6.0/
root@kali:~/python-nmap-0.6.0# ls
root@kali:~/python-nmap-0.6.0#
```
![Python 模块安装](img/29.jpg)

安装：

```shell
python setup.py install
```
![Python 模块安装](img/30.jpg)


#### 1.1.2.2 pip

上面安装Python的讲解中已经讲解了如何安装pip。pip是Python安装包默认的包管理工具，下面举例说明基本用法。

通过 pip 来安装github3模块：

```shell
pip install github3.py
```

![Python 模块安装](img/31.jpg)

如果要安装特定版本的package，通过使用==, >=, <=, >, <来指定一个版本号。例如：

```shell
pip install 'Markdown<2.0'
pip install 'Markdown>2.0,<2.0.3
```

我们也可以将所有的依赖放到一个requirement文件中，一次性安装。例如新建内容如下的requirements.txt文件：

![Python 模块安装](img/32.jpg)

执行命令：

```shell
pip install -r requirements.txt
```

卸载软件包，使用uninstall选项：

```shell
pip uninstall SomePackage 
```

更新软件包：

```shell
pip install --upgrade SomePackage 
```

显示已经安装的文件:

```shell
pip show --files SomePackage
```

显示过期的安装包：

```
pip list --outdated 
```

#### 1.1.2.3 easy_intall

easy_install 是Python setuptools系列工具的中的一个工具，可以用来自动查找、下载、安装、升级依赖包。

在Kali Linux中Python setuptools默认已经被安装，其他Linux系统中使用apt-get或者yum都可以安装。

apt-get 安装命令为：

```shell
sudo apt-get install python-setuptools
```
yum 安装命令为：

```shell
yum install setuptool
```

这里再介绍一个通用的方法，适合所有操作系统。首先下载ez_setup.py （https://bootstrap.pypa.io/ez_setup.py） 文件，然后执行下面的命令即可：

```shell
python ez_setup.py
```

下面我们使用easy_install 来安装Python的一个模块，可以用来对dpf进行解析和安全测试的pyPdf。

```shell
easy_install pyPdf
```

![Python 模块安装](img/33.jpg)

easy_install当然也提供了卸载模块/包的功能。但是必须要注意的是，该模块/包必须要在easy-install.pth 有相关信息，换句话说，也就是要使用easy_install安装的，才可进行卸载。比如命令:

```shell
 easy_install -m redis
```

这样就会将redis模块卸载。

### 1.1.3 virtualenv

virtualenv是可以用来创建独立Python环境的工具, 来解决依赖、版本以及间接权限
问题. 比如一个应用依赖Python 2.7  而另一个应用依赖Python 3.0，或者一个项目依赖Django1.3 而当前全局开发环境为Django1.7, 版本跨度过大, 导致不兼容使项目无法正在运行, 使用virtualenv可以解决这些问题.基本原理为：

> virtualenv创建一个拥有自己安装目录的环境, 这个环境不与其他虚拟环境共享库, 能够方便的管理python版本和管理python库.

1) 安装Virtualenv

```shell
sudo pip install virtualenv
```

2) 创建项目的虚拟环境

```
mkdir testvenv #名字随便取
cd testvenv
virtualenv venv # venv 可替换为别的虚拟环境名称
```

执行后，在本地会生成一个与虚拟环境同名的文件夹，包含 Python 可执行文件和 pip 库的拷贝，可用于安装其他包。但是默认情况下，虚拟环境中不会包含也无法使用系统环境的global site-packages。比如系统环境里安装了 requests 模块，在虚拟环境里 import requests 会提示 ImportError。如果想使用系统环境的第三方软件包，可以在创建虚拟环境时使用参数–system-site-packages。

![virtualenv](img/34.png)

```shell
virtualenv --system-site-packages venv
```

另外，你还可以自己指定虚拟环境所使用的 Python 版本，但前提是系统中已经安装了该版本：

```shell
virtualenv -p /usr/bin/python2.7 venv
```

3) 使用虚拟环境

进入虚拟环境目录，启动虚拟环境：

```
cd venv
source bin/activate # Windows 系统下运行 Scripts\
python -V
```

如果未对命令行进行个性化，此时命令行前面应该会多出一个括号，括号里为虚拟环境的名称。启动虚拟环境后安装的所有模块都会安装到该虚拟环境目录里。

退出虚拟环境：

```shell
deactivate
```
![virtualenv](img/35.png)

## 1.1.4 基于VS Code 搭建开发环境

可以用来开发Python的开发工具很多，选择 Visual Studio Code是因为它轻量，开源，跨平台，方便我们在不同的操作系统上开发和调试代码。

在 官方网站 https://code.visualstudio.com/#alt-downloads ，可以知道它提供的各种系统的安装包。

![vs code](img/36.png)

windows 和 Mac下的安装都很简单，下面简单介绍Linux下的安装方法。

基于Debian/Ubuntu发行版的Linux，我们下载.deb安装包，然后执行以下命令：

```shell
sudo dpkg -i <file>.deb
sudo apt-get install -f # Install dependencies
```

基于RHEL, Fedora 和 CentOS 发行版的Linux，下载.rpm安装包进行安装。

以64位安装包为例，首先需要注册更新yum仓库。

```shell
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```

执行安装：

```shell
dnf check-update
sudo dnf install code
```

VS Code安装好之后，打开工具，安装扩展以支持Python开发。

打开扩展管理工具。

![vs code](img/37.png)

输入“python”进行搜索。

![vs code](img/38.png)

选择上图中框选的扩展，点击“安装”按钮。安装完成后，点击“重新加载”。

![vs code](img/39.png)

VS Code重启之后，我们打开一个文件夹，新建一个test.py文件（使用菜单-->文件-->打开;资源管理器-->新建文件）。

![vs code](img/40.png)
![vs code](img/41.png)

新建 “*.py"文件后，在资源管理器左下角，可以切换Python的版本。

![vs code](img/42.png)
![vs code](img/43.png)

选择合适的版本之后， VS Code会提醒我们安装pylint，点击安装即可。我们来安装pylint（Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合编码风格的代码）。

![vs code](img/44.png)

下面我们回到test.py文件，随便加几行代码。

```python
import socket

print("hello\n")
print("world!")
```

切换到调试菜单，点击”配置“按钮。

![vs code](img/45.png)

编辑器会打开launch.json文件，点击下方的添加配置。

![vs code](img/46.png)

选择使用外部终端的Python调试器。

![vs code](img/47.png)

添加的 配置如下：

```json
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "Python: Terminal (external)",
            "type": "python",
            "request": "launch",
            "program": "${file}",//当前激活的文件作为启动项
            "console": "terminal.external.osxExec" //启用外部终端
        }
    ]
}
```

保存配置之后我们切回test.py ,在代码行数标识的左侧单击可以添加断点，方便我们逐行或者逐过程调试代码。

![vs code](img/49.png)

启动调试可以直接点击启动按钮，更多的启动选项可以在调试菜单中看到。

![vs code](img/50.png)

下面我们直接启动调试，程序首先会打开新的终端，然后会在我们的断点处断住。

![vs code](img/51.png)

如上图是启动调试，代码运行到断点处，左侧是调试信息区域，这里我们可以看到变量和堆栈信息。右侧4区域是调试控制按钮，鼠标移上去会有功能提示。5区域是代码区，此时我们可以增加和去掉断点，查看变量。6区域是打开的终端，test.py的测试代码接收用户的输入并打印，我们可以输入任意内容回车查看结果。同时在编辑器下方的调试控制台也可以显示输出内容。

VS Code 编辑器的详细使用细节这里我们就不展开了，后面教程中涉及到的应用点会单独补充。建议读者尽可能全面的阅读官方文档（https://code.visualstudio.com/docs）。

## 1.1.5 小结

本节课我们完成了Python运行环境和开发环境的搭建，完成了第一个“hello world”程序的编写和运行。为了尽可能简单的跨过第一个门槛，我省略了很多细节和原理性的讲述。不过不用担心，后面的章节会逐步将这些内容补充进来。

接下来的章节，我们会快速的过一遍Python编程基础。实践出真知，这里给几点建议：

>1. 创建一个独立的文件夹，每次练习的时候使用VS Code “文件菜单-->打开” 打开该文件夹。 在该文件夹下，每一个小节再独立一个文件夹存放代码和心得。
>2. 将你的代码和心得上传到github上，方便我们后面的共享和交流。

最后是本节的练习题目：

> 1. 完成Windows/Mac OS /Linux 至少2种操作系统的Python环境安装和测试
> 2. 完成Windows/Mac OS /Linux 至少2种操作系统的VS Code安装和测试
>3. 完成“hello world”程序编写，进行调试启动、非调试启动、断点单步调试、断点逐过程调试、中断程序运行、调试过程中重启


            本系列教程全部内容在星球空间内发布，并提供答疑和辅导。

![](img/00.jpeg)  

    欢迎到关注微信订阅号，交流学习中的问题和心得


![](img/0.jpg)   



