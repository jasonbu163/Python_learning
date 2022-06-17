# vscode 插件生成注释神器[koroFileHeader]

### 安装

##### 1、打开vscode，搜索“koroFileHeader”并安装。

![安装.png](https:////upload-images.jianshu.io/upload_images/8629008-699cc28ffa3cb933.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)



##### 2、安装完成之后重启vscode。



### 使用

##### 1、生成图案注释

① ctrl + shift + p, 输入"codedesign" ，就可以选择你想要的图案了

![codedesign.png](https:////upload-images.jianshu.io/upload_images/8629008-24ebdd356b7dd3c0.png?imageMogr2/auto-orient/strip|imageView2/2/w/867/format/webp)

② 选择想要的图片，效果如下

![喷火龙.png](https:////upload-images.jianshu.io/upload_images/8629008-ea07dc5bd832c68c.png?imageMogr2/auto-orient/strip|imageView2/2/w/798/format/webp)



##### 2、文件头部注释

① 新建文件，然后保存，文件头部会自动生成注释。

![头部注释.png](https:////upload-images.jianshu.io/upload_images/8629008-a54dc4d6a156437d.png?imageMogr2/auto-orient/strip|imageView2/2/w/563/format/webp)

② 头部文件注释的格式，可以通过修改配置来自定义。
 File -> Preferences -> Settings->Extensions->File header Configuration

![自定义.png](https:////upload-images.jianshu.io/upload_images/8629008-729d839a3a0d42fe.png?imageMogr2/auto-orient/strip|imageView2/2/w/838/format/webp)

在配置文件里输入“fileheader.customMade”中定义自己需要的内容

![自定义配置.png](https:////upload-images.jianshu.io/upload_images/8629008-24fcf6dbd68f2202.png?imageMogr2/auto-orient/strip|imageView2/2/w/470/format/webp)

③新建文件，然后保存或者在文件中ctrl+alt +i（ctrl+command+i (mac)） ,生成头部注释，这是就是自定义的格式

![新建文件.png](https:////upload-images.jianshu.io/upload_images/8629008-8f2ee95a0ad863c0.png?imageMogr2/auto-orient/strip|imageView2/2/w/576/format/webp)



##### 3、生成函数注释

在需要注释的函数体上方，按住ctrl + alt + t （ctrl+command+t (mac)）就可生成对应函数体注释，函数体注释样式同样可以通过修改Cursor Mode进行自定义配置

```cpp
    "fileheader.customMade": {} // 头部注释
    "fileheader.cursorMode": {} // 函数注释 
```

![函数注释.png](https:////upload-images.jianshu.io/upload_images/8629008-3f7dcc8da68cac74.png?imageMogr2/auto-orient/strip|imageView2/2/w/531/format/webp)

PS： 取消ctrl +s 保存文件，自动生成头部的注释，只需配置即可

```bash
 "fileheader.customMade": {
        "autoAdd": false
  } 
```



【参考】
 [vscode一键生成注释图案](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1WV411C7Yc)