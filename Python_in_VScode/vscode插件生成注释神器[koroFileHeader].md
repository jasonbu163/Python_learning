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



## 快速上手

### 必须的基础配置: 头部注释模板与函数注释模板

1. **复制**：复制下面给出的模板
2. **插入**：插入模板到全局设置(`setting.json`)中。
3. **简单的更改**：比如把名字换成自己的，不需要的字段可以删掉。
4. 重启编辑器，使用快捷键体验它。

```
// 头部注释
"fileheader.customMade": {
    // Author字段是文件的创建者 可以在specialOptions中更改特殊属性
    // 公司项目和个人项目可以配置不同的用户名与邮箱 搜索: gitconfig includeIf  比如: https://ayase.moe/2021/03/09/customized-git-config/
    // 自动提取当前git config中的: 用户名、邮箱
    "Author": "git config user.name && git config user.email", // 同时获取用户名与邮箱
    // "Author": "git config user.name", // 仅获取用户名
    // "Author": "git config user.email", // 仅获取邮箱
    // "Author": "OBKoro1", // 写死的固定值 不从git config中获取
    "Date": "Do not edit", // 文件创建时间(不变)
    // LastEditors、LastEditTime、FilePath将会自动更新 如果觉得时间更新的太频繁可以使用throttleTime(默认为1分钟)配置更改更新时间。
    "LastEditors": "git config user.name && git config user.email", // 文件最后编辑者 与Author字段一致
    // 由于编辑文件就会变更最后编辑时间，多人协作中合并的时候会导致merge
    // 可以将时间颗粒度改为周、或者月，这样冲突就减少很多。搜索变更时间格式: dateFormat
    "LastEditTime": "Do not edit", // 文件最后编辑时间
    // 输出相对路径，类似: /文件夹名称/src/index.js
    "FilePath": "Do not edit", // 文件在项目中的相对路径 自动更新
    // 插件会自动将光标移动到Description选项中 方便输入 Description字段可以在specialOptions更改
    "Description": "", // 介绍文件的作用、文件的入参、出参。
    // custom_string_obkoro1~custom_string_obkoro100都可以输出自定义信息
    // 可以设置多条自定义信息 设置个性签名、留下QQ、微信联系方式、输入空行等
    "custom_string_obkoro1": "", 
    // 版权声明 保留文件所有权利 自动替换年份 获取git配置的用户名和邮箱
    // 版权声明获取git配置, 与Author字段一致: ${git_name} ${git_email} ${git_name_email}
    "custom_string_obkoro1_copyright": "Copyright (c) ${now_year} by ${git_name_email}, All Rights Reserved. "
    // "custom_string_obkoro1_copyright": "Copyright (c) ${now_year} by 写死的公司名/用户名, All Rights Reserved. "
},
// 函数注释
"fileheader.cursorMode": {
    "description": "", // 函数注释生成之后，光标移动到这里
    "param": "", // param 开启函数参数自动提取 需要将光标放在函数行或者函数上方的空白行
    "return": "",
}
```

#### 如何找到setting.json设置模板

1. 简单的输入命令

- 打开VSCode命令面板: mac: `command + p` window: `ctrl + p`
- 输入`> Open Settings`(注意`>`后面有一个空格)

![搜索设置](https://github.com/OBKoro1/koro1FileHeader/raw/dev/images/docs/command-setting.jpg?raw=true)

2. 从设置中打开

首选项 > 设置 > 搜索`fileheader` > 在右侧中贴上配置 > 做简单的更改

![img](https://camo.githubusercontent.com/ce756f335029dbac485630ed556637c6c8329e0eb95803d8a5e4831e80a06c69/687474703a2f2f7777312e73696e61696d672e636e2f6c617267652f303035593472436f67793166786130667276776f776a333130733069756a77742e6a7067)

### 快捷键使用

#### 文件头部注释快捷键

- 记录文件信息/文件的传参/出参，设置个性签名、留下QQ、微信联系方式、输入空行等等
- 支持用户高度自定义注释选项, 适配各种需求的注释形式。
- 保存文件的时候，自动更新最后的编辑时间和编辑人
- `window`：`ctrl+win+i`, `mac`：`ctrl+cmd+i`, `linux`: `ctrl+meta+i`,`Ubuntu`: `ctrl+super+i`

#### 函数注释注释快捷键

> 更多关于函数参数自动请查阅[配置-函数注释自动提取函数的参数](https://github.com/OBKoro1/koro1FileHeader/wiki/配置#函数注释自动提取函数的参数)文档

- 将光标放在函数行或者将光标放在函数上方的空白行。
- 自动解析函数参数，生成函数参数注释。
- 快捷键：`window`：`ctrl+win+t`,`mac`：`ctrl+cmd+t`,`linux`: `ctrl+meta+t`, `Ubuntu`: `ctrl+super+t`

#### 多行函数参数鼠标选中后函数声明后按快捷键自动提取

1. **鼠标左键选择多行函数声明区域，函数声明区域尽量精准**
2. **按函数注释快捷键**

![多行函数参数自动提取参数](https://github.com/OBKoro1/koro1FileHeader/raw/dev/images/docs/multiLineParamsCreate.gif?raw=true)

#### 函数注释光标移动到下一行，快速添加函数参数描述

```
window`: `win+y`, mac: `cmd+y`, linux: `meta+y
```

生成函数注释之后，使用快捷键移动鼠标到下一行，快速为函数参数添加描述。

可能有很多参数，需要移动鼠标一个一个添加的话，操作起来有点麻烦。

![函数注释光标移动到下一行，快速添加函数参数描述](https://github.com/OBKoro1/koro1FileHeader/raw/dev/images/docs/param-description.gif?raw=true)

#### 快捷键不可用的问题

快捷键不可用很可能是被占用了,[参考这里](https://github.com/OBKoro1/koro1FileHeader/issues/5)

### 关闭自动添加头部注释

插件默认打开自动添加头部注释: [关闭自动添加头部注释](https://github.com/OBKoro1/koro1FileHeader/wiki/配置#2-自动添加文件头部注释)

或许你可以对自动添加头部注释做一些限制：

- 代码行数：文件多少行以内允许自动添加
- 白名单与黑名单：比如只禁止`.json`，只允许`.js`文件添加
- 项目的黑名单：添加公司的项目名，禁止公司项目自动添加头部注释。
- 文件夹的黑名单，比如`node_modules`文件夹禁止、`README.md`文件禁止

### 使用效果

**头部注释和注释图案**

![example.gif](https://raw.githubusercontent.com/OBKoro1/koro1FileHeader/master/images/example.gif)

**函数注释: 自动提取函数参数**

![koroFileHeader函数参数提取](https://github.com/OBKoro1/koro1FileHeader/raw/master/images/function-params.gif?raw=true)

**注释图案**

[支持一键添加佛祖保佑永无BUG、神兽护体等注释图案](https://github.com/OBKoro1/koro1FileHeader/wiki/佛祖保佑永无BUG、神兽护体、注释图案)

![添加注释图案](https://github.com/OBKoro1/koro1FileHeader/raw/master/images/codeDesign.gif?raw=true)https://links.jianshu.com/go?to=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1WV411C7Yc)