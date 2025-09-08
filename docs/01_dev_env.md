#  开发环境

## python安装



### python下载

进入[python官网](https://www.python.org/)

![image-20250822101938032](01_dev_env_assets/image-20250822101938032.png)



选择合适的系统版本，这里以windows系统为例。

![image-20250822102053525](01_dev_env_assets/image-20250822102053525.png)



选择python版本，3.9<=**版本**<最新版。

![image-20250822102340317](01_dev_env_assets/image-20250822102340317.png) 



### python安装

下载installer之后，点击安装。

![image-20250822102519729](01_dev_env_assets/image-20250822102519729.png)

**如果没装过python**，可以点击勾选下方的Add python.exe tp PATH。

![image-20250822102654356](01_dev_env_assets/image-20250822102654356.png)

然后点击自定义安装。

![image-20250822102732819](01_dev_env_assets/image-20250822102732819.png)

点击Next。

![image-20250822102809841](01_dev_env_assets/image-20250822102809841.png)



这里选项保持默认即可，可更换下方python的安装位置。点击Install安装。

![image-20250822103018766](01_dev_env_assets/image-20250822103018766.png)



安装完成之后，关闭窗口。

![image-20250822103126746](01_dev_env_assets/image-20250822103126746.png)



### python验证

安装完成之后，打开命令行终端（以window为例），按下键盘WIN+R，屏幕左下方会显示一个输入框，输入cmd确定后，会打开命令行终端。

![image-20250822103354944](01_dev_env_assets/image-20250822103354944.png)

![image-20250822103436623](01_dev_env_assets/image-20250822103436623.png)

或者在搜索中输入cmd打开。

![image-20250822103533404](01_dev_env_assets/image-20250822103533404.png)



在终端输入python，回车，终端会显示当前使用的python版本。

![image-20250822103702323](01_dev_env_assets/image-20250822103702323.png)



### 配置环境变量

若在终端输入python之后提示“不是内部或外部命令，也不是可运行的程序”，需要将python.exe配置到PATH环境变量中。



搜索“环境变量”，点击打开“**编辑系统环境变量**”

![image-20250822103920767](01_dev_env_assets/image-20250822103920767.png)



点击“环境变量”

![image-20250822104039075](01_dev_env_assets/image-20250822104039075.png)



在“系统变量”中找到“Path”一行，点击编辑。

![image-20250822104119967](01_dev_env_assets/image-20250822104119967.png)



点击“新建”，找到python的安装路径，以及该路径下的Scripts文件夹，把这两个文件夹的完整路径分别填到新建的变量中。

可添加多个python，点击右侧的“上移”“下移”移动变量的位置，优先使用在上面的变量。

![image-20250822104205404](01_dev_env_assets/image-20250822104205404.png)

![image-20250822104628010](01_dev_env_assets/image-20250822104628010.png)

![image-20250822104823462](01_dev_env_assets/image-20250822104823462.png)





点击确定。打开终端再次输入python，即可显示版本信息。

![image-20250822105150436](01_dev_env_assets/image-20250822105150436.png)



### 创建虚拟环境

不同版本的python、第三方库会依赖不同的库，直接使用pip会在全局python环境中安装库，这会导致不同版本库之间的兼容问题，所以建议为每一个项目单独创建一个虚拟环境，在虚拟环境中安装所需的库。

进入项目目录，在终端输入

```shell
python -m venv .venv
```

创建虚拟环境

![image-20250825144516736](01_dev_env_assets/image-20250825144516736.png)



### 激活虚拟环境

终端进入到.venv/Scripts目录，输入

```shell
./activate
```

激活环境，激活后，路径前面会显示虚拟环境名称。

![image-20250825144858324](01_dev_env_assets/image-20250825144858324.png)



输入

```
deactivate
```

取消激活环境。

![image-20250825145036973](01_dev_env_assets/image-20250825145036973.png)







## Nodejs安装

nodejs是javaScript的运行环境，后续课程使用的mcp需要nodejs环境。



### 下载

进入[nodejs官网](https://nodejs.org)，点击download。

![image-20250822151136899](01_dev_env_assets/image-20250822151136899.png)



选择合适的系统以及长期支持的版本（LTS），点击下载Window Installer。

![image-20250822151327875](01_dev_env_assets/image-20250822151327875.png)



### 安装

点击下载完成的安装包，保持默认选项，点击下一步，选择安装位置完成安装。

![image-20250822151554406](01_dev_env_assets/image-20250822151554406.png)

### 验证

安装完成后打开终端输入node，显示版本信息即安装成功。

![image-20250822151741245](01_dev_env_assets/image-20250822151741245.png)



### 配置运行权限

 **PowerShell 的执行策略 (Execution Policy)** 限制了脚本运行。默认情况下，Windows 可能会禁止运行 `.ps1` 脚本。

在powershell输入

```powershell
Get-ExecutionPolicy
```

默认情况下的输出为：**Restricted**

![image-20250822160720325](01_dev_env_assets/image-20250822160720325.png)



**修改运行策略**

在powershell输入：

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Get-ExecutionPolicy
```

显示RemoteSigned代表修改成功。

![image-20250822160946406](01_dev_env_assets/image-20250822160946406.png)



## GIT安装

git是一个代码管理工具。[官网](https://git-scm.com/downloads)

![image-20250822110601008](01_dev_env_assets/image-20250822110601008.png)



### 下载

选择合适的版本。

![image-20250822110826556](01_dev_env_assets/image-20250822110826556.png)

![image-20250822110858749](01_dev_env_assets/image-20250822110858749.png)



### 安装

下载完成后，点击安装包开始安装。

![image-20250822111702271](01_dev_env_assets/image-20250822111702271.png)

选择安装位置，点击下一步。

![image-20250822111745415](01_dev_env_assets/image-20250822111745415.png)

全都保持默认选项，点击下一步。

![image-20250822111829419](01_dev_env_assets/image-20250822111829419.png)

安装完成后关闭窗口即可。

![image-20250822112300353](01_dev_env_assets/image-20250822112300353.png)



### 验证

打开终端，输入git，会显示一下内容，说明安装成功。

![image-20250822112429505](01_dev_env_assets/image-20250822112429505.png)







## VSCode安装

Visual Studio code 是微软开发的一款IDE集成开发环境软件，后续课程的代码演示使用该软件。也可以使用其它软件如pycharm、cursor、trae等。



### 下载

进入[vscode官网](https://code.visualstudio.com/)，直接点击下载即可，其它系统点击右上方的下载，选择合适的版本。

![image-20250822113059091](01_dev_env_assets/image-20250822113059091.png)

![image-20250822113132724](01_dev_env_assets/image-20250822113132724.png)



### 安装

下载完成之后，点击安装。点击同意，下一步。

![image-20250822113253883](01_dev_env_assets/image-20250822113253883.png)



选择安装位置，点击下一步。后续选项保持默认即可，点击下一步。

![image-20250822113319904](01_dev_env_assets/image-20250822113319904.png)



点击安装。

![image-20250822113425937](01_dev_env_assets/image-20250822113425937.png)



点击完成。

![image-20250822113509685](01_dev_env_assets/image-20250822113509685.png)

![image-20250822113549703](01_dev_env_assets/image-20250822113549703.png)





### 语言设置

打开vscode，点击左侧的插件按钮，输入chinese，可安装汉化插件，安装完成后重启即可。

![image-20250822113846408](01_dev_env_assets/image-20250822113846408.png)



### 创建文件夹

在电脑上创建一个文件夹，打开vscode，点击左上方的文件按钮，点击打开文件夹，选择刚才创建的文件夹打开。

![image-20250822114747972](01_dev_env_assets/image-20250822114747972.png)

![image-20250822114808771](01_dev_env_assets/image-20250822114808771.png)

![image-20250822114838632](01_dev_env_assets/image-20250822114838632.png)



点击信任作者。

![image-20250822114913611](01_dev_env_assets/image-20250822114913611.png)



打开文件夹后，左上方会显示文件夹名称。

![image-20250822114948709](01_dev_env_assets/image-20250822114948709.png)

点击文件夹名称，右侧会显示操作图标，可以创建文件、文件夹等。

![image-20250822115117635](01_dev_env_assets/image-20250822115117635.png)

### 安装python插件

创建一个hello.py文件，打开，右下角会出现下载python插件的提示，直接安装即可。

![image-20250822115157862](01_dev_env_assets/image-20250822115157862.png)

![image-20250822115425910](01_dev_env_assets/image-20250822115425910.png)

![image-20250822115450599](01_dev_env_assets/image-20250822115450599.png)



如果没有出现提示，直接在插件中搜索python，手动安装 Python Debugger、Python Environments、Python即可。

![image-20250822115603786](01_dev_env_assets/image-20250822115603786.png)



点击允许访问。

![image-20250822115707602](01_dev_env_assets/image-20250822115707602.png)



安装完成后，打开hello.py文件，右上角会显示一个三角形。

![image-20250822115916915](01_dev_env_assets/image-20250822115916915.png)



### 运行python程序

在hello.py文件中编写示例代码。

```python
if __name__ == "__main__":
    print("hello vscode")
```

点击右上角面板显示按钮，可以显示/隐藏终端。

![image-20250822122313332](01_dev_env_assets/image-20250822122313332.png)



点击右上角允许该程序，下方的终端会输出"hello vscode"。

![image-20250822120206453](01_dev_env_assets/image-20250822120206453.png)



观察终端输出的上一行：

```shell
 C:/Users/lsn/AppData/Programs/Python/Python312/python.exe c:/Users/lsn/Desktop/teste1/hello.py
```

+ ...python.exe ：这个就是之前安装的python
+ ...hello.py ：这个是我们编写的程序

这个命令就是终端执行python程序的命令

```shell
python xxx.py
```

因为我们添加了python的环境变量，所以可以不输入完整的python路径。

在终端输入：

```shell
python hello.py
```

![image-20250822120850834](01_dev_env_assets/image-20250822120850834.png)

可以看到程序正常运行了。不过python后面的hello.py文件也不是完整路径，因为当前终端所在的路径是...\test01，也就是hello.py文件所在的路径，那么执行命令的时候，python会在当前文件寻找hello.py文件进行执行，所以不需要完整路径。

我们在终端输入：

```shell
cd ..
```

![image-20250822121332309](01_dev_env_assets/image-20250822121332309.png)

可以看到当前路径变成了test01的上一级目录。

我们再次执行hello.py文件。

![image-20250822121446286](01_dev_env_assets/image-20250822121446286.png)

可以看到执行出现错误：没有这个文件或者目录。

我们在终端输入ls来查看当前目录下的文件和文件夹：

```shell
ls
```

![image-20250822121702454](01_dev_env_assets/image-20250822121702454.png)

可以看到，当前目录下确实没有hello.py这个文件，所以执行错误。

那么，我们在终端输入：

```python
python ./test01/hello.py
```

![image-20250822121928881](01_dev_env_assets/image-20250822121928881.png)

可以看到程序再次成功运行。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

综上，在终端运行python程序时，你可以cd到程序所在的目录下后，执行程序；或者输入完整/相对路径来执行。



### Copilot

copilot是vscode自带的一个AI插件，打开vscode点击右上方的机器人图标，即可打开对话框。

![image-20250822114436532](01_dev_env_assets/image-20250822114436532.png)



使用github登录copilot。

![image-20250822141144098](01_dev_env_assets/image-20250822141144098.png)



登录后可在输入框输入文本进行对话，对话框下方可以选择模型。

![image-20250822143404039](01_dev_env_assets/image-20250822143404039.png)



输入#hello，copilot会匹配对应的文件，选择需要的文件可以将其添加为上下文。

![image-20250822143615298](01_dev_env_assets/image-20250822143615298.png)

![image-20250822143637662](01_dev_env_assets/image-20250822143637662.png)



输入文本让它添加功能。

![image-20250822143738029](01_dev_env_assets/image-20250822143738029.png)

![image-20250822143756710](01_dev_env_assets/image-20250822143756710.png)

模型输出了结果，但是没有添加到文件中，因为当前的模式是“Ask”（对话框左下角），将模式改为Edit/Agent后，让它把新内容添加到文件中。

![image-20250822143925247](01_dev_env_assets/image-20250822143925247.png)

模型执行完成后，hello.py文件中出现了新的内容。可以检测内容是否是需要的，然后选择Keep/Undo。

![image-20250822144215992](01_dev_env_assets/image-20250822144215992.png)



每段对话上方都有一个checkpoint，点击后可以将操作撤销，回到执行这个操作之前。

![image-20250822144935083](01_dev_env_assets/image-20250822144935083.png)

![image-20250822145054911](01_dev_env_assets/image-20250822145054911.png)



### Lingma

通义灵码是阿里开发的一个AI插件。在插件中搜索lingma安装。

![image-20250822145506794](01_dev_env_assets/image-20250822145506794.png)



注册登录阿里云账号后使用。

![image-20250822145716218](01_dev_env_assets/image-20250822145716218.png)



与copilot类似，可在对话框左下角调整模式、模型

![image-20250822145952861](01_dev_env_assets/image-20250822145952861.png)

![image-20250822150213700](01_dev_env_assets/image-20250822150213700.png)



#### 语言设置

点击右上角的设置按钮，将settings中最底下的三个语言设置为中文即可。

![image-20250822150422204](01_dev_env_assets/image-20250822150422204.png)



## CUDA+cuDNN安装

> 目前下载对应cuda版本的pytorch时，会包含cuda与cuDNN，若不进行cuda相关的编程，不再需要单独下载cuda与cuDNN。

> 这部分的进行，需要电脑安装了英伟达Nvidia的显卡

### Nvidia显卡驱动安装

查看任务栏中是否有英伟达显卡驱动的图标，如果有说明已经安装了驱动，跳过显卡驱动安装这一步。

![image-20250822165226039](01_dev_env_assets/image-20250822165226039.png)

进入[Nvidia官网](https://www.nvidia.cn/geforce/campaigns/back-to-school/?ncid=pa-srch-baid-450176)，点击驱动程序。

![image-20250822165400645](01_dev_env_assets/image-20250822165400645.png)



#### 确认显卡型号

按下Ctrl+Alt+Delete，或者右键点击任务栏，打开任务管理器。

![image-20250822165527822](01_dev_env_assets/image-20250822165527822.png)

在“性能”栏下找到对应的显卡，查看显卡型号。

![image-20250822165603521](01_dev_env_assets/image-20250822165603521.png)



或者在搜索中搜索“设备管理器”，打开

![image-20250822165745215](01_dev_env_assets/image-20250822165745215.png)



在“显示适配器”下找到显卡，确认型号。

![image-20250822165815625](01_dev_env_assets/image-20250822165815625.png)



#### 下载显卡驱动

填入相关信息，搜索驱动程序。

![image-20250822170026457](01_dev_env_assets/image-20250822170026457.png)



选择最新版本的驱动下载，GeForce Game Ready和NVIDIA Studio都可以。

![image-20250822170345928](01_dev_env_assets/image-20250822170345928.png)



点击立即下载，下载完成后点击安装，选择默认选项，点击下一步完成安装即可。

![image-20250822170503761](01_dev_env_assets/image-20250822170503761.png)

![image-20250822170546349](01_dev_env_assets/image-20250822170546349.png)



#### 验证CUDA Version

安装完成后，在终端输入：

```shell
nvidia-smi
```

控制台会输出显卡信息：CUDA Version：12.9 --》就是当前最高支持的CUDA版本。

![image-20250822170807436](01_dev_env_assets/image-20250822170807436.png)



### CUDA安装



#### 下载

进入[Nvidia开发者平台](https://developer.nvidia.com/)，点击Platforms and Tools——Developer Tools Catalog

![image-20250825111452958](01_dev_env_assets/image-20250825111452958.png)

![image-20250825111601430](01_dev_env_assets/image-20250825111601430.png)

点击搜索框，输入CUDA Tool，选择CUDA Toolkit，点击下载。

![image-20250825111715840](01_dev_env_assets/image-20250825111715840.png)

![image-20250825111807055](01_dev_env_assets/image-20250825111807055.png)

点击Archive of Previous CUDA Releases。

![image-20250825111904876](01_dev_env_assets/image-20250825111904876.png)



由前面[验证](#验证CUDA Version)已知，CUDA Version为12.9，所以小于12.9版本的都可以下载，不过一般使用稳定的版本，如11.8、12.8（可以下载多个版本CUDA）。

![image-20250825112023420](01_dev_env_assets/image-20250825112023420.png)

选择一个版本，选择合适的系统版本，点击下载。

![image-20250825113137336](01_dev_env_assets/image-20250825113137336.png)



#### 安装

下载完成点击运行，选择解压位置。

![image-20250825113451066](01_dev_env_assets/image-20250825113451066.png)

![image-20250825113532949](01_dev_env_assets/image-20250825113532949.png)



点击同意继续，

![image-20250825113728467](01_dev_env_assets/image-20250825113728467.png)



点击“自定义”，下一步，保持默认选项，下一步

![image-20250825113809860](01_dev_env_assets/image-20250825113809860.png)



可以更换位置，点击下一步，然后等待安装完成。

![image-20250825113906408](01_dev_env_assets/image-20250825113906408.png)



安装完成，进入安装目录，可以看到以下内容：

![image-20250825114107055](01_dev_env_assets/image-20250825114107055.png)



#### 配置环境变量

打开系统环境变量。如果CUDA安装成功，在“系统变量”中会生成两个变量：

+ CUDA_PATH：使用的CUDA的路径，可以更改这个路径来更换CUDA版本。
+ CUDA_PATH_V版本： 具体版本CUDA的安装路径。

![image-20250825114342224](01_dev_env_assets/image-20250825114342224.png)



在“系统变量”找到Path，编辑，找到含有安装CUDA路径的变量，这里我安装了两个版本CUDA，所以分别有两个版本的变量，如果没有，手动添加即可。可以移动需要使用的版本到上面来切换CUDA版本。

![image-20250825114740281](01_dev_env_assets/image-20250825114740281.png)

![image-20250825114834022](01_dev_env_assets/image-20250825114834022.png)



#### 验证CUDA

打开终端输入，可以看到输出的对应cuda版本：

```shell
nvcc -V
```

![image-20250825115601885](01_dev_env_assets/image-20250825115601885.png)



#### 切换CUDA版本

按照之前安装教程，安装两个不同版本。

打开终端输入：

```shell
nvcc -V
```

或

```shell
nvcc --version
```



![image-20250825115530075](01_dev_env_assets/image-20250825115530075.png)



打开系统环境变量，查看CUDA_PATH，可以看到路径对应的是CUDA11.8，把它改为12.8

![image-20250825115705464](01_dev_env_assets/image-20250825115705464.png)

![image-20250825115815707](01_dev_env_assets/image-20250825115815707.png)

![image-20250825115825456](01_dev_env_assets/image-20250825115825456.png)



点击编辑path，将cuda12.8的两个变量移动到最上方（相对其他cuda版本变量），或者直接添加新的变量，点击确认。

![image-20250825115942674](01_dev_env_assets/image-20250825115942674.png)

![image-20250825120018585](01_dev_env_assets/image-20250825120018585.png)



打开**新的**终端，查看cuda版本，可以看到，版本已切换为12.8：

![image-20250825120113065](01_dev_env_assets/image-20250825120113065.png)





### cuDNN安装

Nvidia开发者平台搜索cudnn，点击进入。

![image-20250825121145241](01_dev_env_assets/image-20250825121145241.png)





点击下载cuDNN

![image-20250825121241868](01_dev_env_assets/image-20250825121241868.png)



点击Archive of Previous Releases，

![image-20250825121308526](01_dev_env_assets/image-20250825121308526.png)



<span style="color:#0B99FF"> 这里cuDNN 9.x版本均为12.x版本CUDA可用的cuDNN </span>，可以直接点击下载，

![image-20250825121511360](01_dev_env_assets/image-20250825121511360.png)

<span style="color:#FF5263">点击cuDNN 8.x可以下载以前的版本，</span>点击下载合适的版本即可。

![image-20250825121916538](01_dev_env_assets/image-20250825121916538.png)



点击下载，需要登录，正常注册登录即可。

![image-20250825121959850](01_dev_env_assets/image-20250825121959850.png)

![image-20250825122019979](01_dev_env_assets/image-20250825122019979.png)



下载完成后解压

![image-20250825123336289](01_dev_env_assets/image-20250825123336289.png)



打开解压的文件夹，可以看到三个文件夹

![image-20250825123800765](01_dev_env_assets/image-20250825123800765.png)



打开cuda安装的路径，可以看到也有三个对应的文件夹。

![image-20250825123950471](01_dev_env_assets/image-20250825123950471.png)



需要将cuDNN三个文件夹中的内容分别复制到cuda对应的三个文件夹中：

#### bin

![image-20250825124234586](01_dev_env_assets/image-20250825124234586.png)



#### include

![image-20250825124328668](01_dev_env_assets/image-20250825124328668.png)



#### lib

![image-20250825124454028](01_dev_env_assets/image-20250825124454028.png)









## Pytorch安装

pytorch是一个深度学习框架，在后续的yolo模型训练推理中会使用到。



### 下载

进入[pytorch官网](https://pytorch.org/)，点击get started

![image-20250822164545249](01_dev_env_assets/image-20250822164545249.png)



选择合适的系统版本，复制pip下载命令在终端执行即可（建议单独创建一个虚拟环境），

![image-20250825145401225](01_dev_env_assets/image-20250825145401225.png)



点击 install previous versions of PyTorch下载以前版本，选择合适的系统与版本，复制pip命令在终端执行即可。

![image-20250825145559280](01_dev_env_assets/image-20250825145559280.png)

![image-20250825145940382](01_dev_env_assets/image-20250825145940382.png)



查看已安装包，终端输入

```shell
pip list
```

![image-20250825150224300](01_dev_env_assets/image-20250825150224300.png)



### 验证pytorch

创建一个python文件，编写代码，执行，能够输出版本号并且正常执行，说明安装成功。

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("cuDNN enabled:", torch.backends.cudnn.enabled)
print("cuDNN version:", torch.backends.cudnn.version())

# 构造一个卷积运算（会调用 cuDNN）
x = torch.randn(10, 3, 224, 224).cuda()  # batch=10, 3通道, 224x224
conv = torch.nn.Conv2d(3, 32, 3).cuda()

y = conv(x)
print("Conv2D output shape:", y.shape)

```

![image-20250825150356256](01_dev_env_assets/image-20250825150356256.png)





## 远程连接工具（任选）

### windows自带ssh工具

[官网](https://learn.microsoft.com/zh-cn/windows/terminal/tutorials/ssh)

![image-20250825154117066](01_dev_env_assets/image-20250825154117066.png)



在“设置”》“可选功能”中搜索并添加openssh

![image-20250825154239568](01_dev_env_assets/image-20250825154239568.png)

![image-20250825154326810](01_dev_env_assets/image-20250825154326810.png)

![image-20250825154343407](01_dev_env_assets/image-20250825154343407.png)



打开终端输入ssh

![image-20250825154554907](01_dev_env_assets/image-20250825154554907.png)



远程连接

```shell
ssh 用户名@ip
```

![image-20250825154728858](01_dev_env_assets/image-20250825154728858.png)



输入yes，输入密码，即可连接。

![image-20250825154801843](01_dev_env_assets/image-20250825154801843.png)



### FinalShell

FinalShell集成远程连接与文件传输。[官网](https://www.hostbuf.com/t/988.html)，选择合适版本下载安装即可

![image-20250825154939470](01_dev_env_assets/image-20250825154939470.png)



安装后打开，点击文件夹

![image-20250825155157575](01_dev_env_assets/image-20250825155157575.png)



创建SSH连接

![image-20250825155241696](01_dev_env_assets/image-20250825155241696.png)



输入信息，确认

![](01_dev_env_assets/image-20250825155346859.png)

![image-20250825155413710](01_dev_env_assets/image-20250825155413710.png)



双击打开连接

![image-20250825155432551](01_dev_env_assets/image-20250825155432551.png)



还有其他工具如xshell等，自行选择



## 文件传输

### FinalShell

打开一个连接，将文件直接拖动到需要传输的位置即可传输。

![image-20250825155731950](01_dev_env_assets/image-20250825155731950.png)



### FileZilla

[官网](https://filezilla-project.org/)，点击下载安装。

![image-20250825160122313](01_dev_env_assets/image-20250825160122313.png)



输入配置信息连接，拖动文件即可传输。

![image-20250825160019147](01_dev_env_assets/image-20250825160019147.png)





### WinSCP

[官网](https://winscp.net/eng/index.php)，点击下载安装。

![image-20250825160243908](01_dev_env_assets/image-20250825160243908.png)



打开，创建连接，输入配置信息，连接后拖拽文件即可传输。

![image-20250825160438577](01_dev_env_assets/image-20250825160438577.png)

![image-20250825160522664](01_dev_env_assets/image-20250825160522664.png)

![image-20250825160554113](01_dev_env_assets/image-20250825160554113.png)
