# Hello World

我们可以从输出一段“Hello World”文字开始，以此作为了解和学习MicroPython的第一步。

> 本文所述操作基于Thonny IDE，需要先完成对Thonny IDE的配置，与开发板建立连接。[Thonny IDE运行环境搭建参见wiki](https://wiki.banana-pi.org/Micropython_%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)。

## 使用REPL

**REPL**即**Read-Eval-Print-Loop**的缩写名词，译为 **读取-求值-输出-循环**。

我们可以通过实际操作来明白它的意思。

将已经安装了MicroPython固件的开发板连接电脑，运行Thonny IDE并正确配置后，在Shell窗口中将出现这样的文本内容：

```
MicroPython v1.17 on 2022-01-09; ESP32S3 module with ESP32S3
Type "help()" for more information.
>>> 
```

注意最后一行的`>>>`提示符，我们可以直接在这后面输入算式或是代码，按下键盘`enter`回车键就会立即在下一行得到输出结果。

```python
>>> 1+2
3
>>> print("Hello World")
Hello World
>>> 
```

现在可以很直观的理解了，它会读取我们输入的信息，执行运算求值，输出结果，然后等待我们后续的输入，一直循环这个过程，这也是**REPL**又被译为**交互式解释器**的原因，我们可以直接通过输入代码来和硬件交互，没有像传统的C语言那样需要在中间执行编译的过程，我们输入的信息没有经过编译就传输给芯片自行解释并运行了，这本是Python语言的一大重要特性，MicroPython完美继承了它。

如果仅仅是使用MicroPython REPL，很多具有串口信息收发功能的软件都可以操作，感兴趣的话可以试试各种串口工具，这可以令人更深刻的理解 “没有中间执行编译的过程” 的意思。

>关于REPL的应用，更详尽全面的内容可以参考[MicroPython文档：REPL](https://docs.micropython.org/en/latest/reference/repl.html)

## 代码编辑器

Thonny IDE当然不仅仅可以进行REPL的操作，作为python代码编辑器，本职功能还是有的。

新建一个文件并在其编辑区内输入代码。

```python
print(1+2)
print("Hello World")
```

完成代码编辑后，点击**保存**，可以选择将文件保存到MicroPython设备中，这将直接将整个文件的数据传输到flash中。可将文件命名为`main.py`，设备会在每次上电或复位后执行有这个文件名的程序，而其他名称的文件仅在被`main.py`调用时或是我们在Thonny中点击**运行**时被执行。

![](https://i.imgur.com/tn9Fi3W.png)

现在点击**运行**，同样是无需编译的，在Shell中会立即得到结果。

```
3
Hello World
```

另外也可以尝试REPL的键盘控制快捷键**ctrl+D**软件复位，可以看到复位后程序立即执行并打印出信息。