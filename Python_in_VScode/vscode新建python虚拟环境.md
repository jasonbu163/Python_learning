# vscode win10 python venv使用

## 创建虚拟环境
如下所示命令，在你的项目目录下按下 **shift + 右键** 启动powershell，创建虚拟环境，虚拟环境文件夹名字为 .venv

```powershell
python -m venv .venv
```



## 配置VSCode 当前项目 Python  interpreter
按下 **ctrl + shift + p** 弹出命令面板， 如下图所示输入 Python：Select，会弹出下拉选项，选择下图圈出的选项，接下来vscode会显示出当前主机上python环境，如下图二所示，然后选择我们刚才创建的虚拟环境

![img](https://img-blog.csdnimg.cn/20190912100408997.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NhbGFkYm9ibw==,size_16,color_FFFFFF,t_70)

![img](https://img-blog.csdnimg.cn/20190912100609271.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NhbGFkYm9ibw==,size_16,color_FFFFFF,t_70)



## 激活虚拟环境

Windows系统中，是通过.\venv\Scripts\activate命令进入虚拟环境，因为运行了activate.bat后会在同级目录下生成activate.ps1，PowerShell 默认不允许执行*.ps1脚本文件。运行ps1文件会得到下面的错误:

![img](https://img-blog.csdnimg.cn/2019091210115445.png)

要解决这个问题，需要在powershell里面修改policy：

以管理员身份运行PowShell，然后执行 `set-executionpolicy remotesigned` 命令，并选择 **Y** 如下图所示，执行完成后再激活vscode中的terminal，就会默认激活venv虚拟环境，如下图所示：

![img](https://img-blog.csdnimg.cn/20190912101314394.png)

![img](https://img-blog.csdnimg.cn/20190912101523249.png)

   >**注意：**
   >
   >​	在 (.venv)中，可以使用 **activate或者deactivate** 来启动和关闭虚拟环境

