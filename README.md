一款用于linux下隐藏进程的工具
=============================

源代码在 https://github.com/gianlucaborello/libprocesshider ，这里是我优化版本




libprocesshider
===============

Hide a process under Linux using the ld preloader.

Full tutorial available at [https://www.sysdig.com/blog/hiding-linux-processes-for-fun-and-profit](https://www.sysdig.com/blog/hiding-linux-processes-for-fun-and-profit)


# 第一步
首先编辑processhider.c文件，修改process_to_filter变量的内容，所有具有此名称的进程都将被隐藏。所以，必须提供命令中的字符。

比如 对于 /usr/bin/python3 test.py 1000 进程：

（1）process_to_filter变量的内容为 python3 时，能实现隐藏。为 python 时 ，不能隐藏。

（2）process_to_filter变量的内容为 test.py 时，不能隐藏

# 第二步
In short, compile the library:

```
gianluca@sid:~/libprocesshider$ make
gcc -Wall -fPIC -shared -o libprocesshider.so processhider.c -ldl
gianluca@sid:~/libprocesshider$ sudo mv libprocesshider.so /usr/local/lib/
```

# 第三步
Load it with the global dynamic linker

```
root@sid:~# touch /etc/ld.so.preload
root@sid:~# echo /usr/local/lib/libprocesshider.so >> /etc/ld.so.preload
```

这一步可以用 export LD_PRELOAD=/usr/local/lib/libprocesshider.so 来代替，但export的方式仅在该终端中有用，其它终端无效。

And your process will be off the radar 

```
# 第四步。看效果
gianluca@sid:~$ sudo ps aux
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
...

gianluca@sid:~$ sudo lsof -ni
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
...
```

# 总结
（1）总的来说，确实有用。在执行上述操作后，已有的进程不被影响，不会隐藏。在上述操作后，新建的进程，则会被隐藏。
（2）第三步，最好是用修改 /etc/ld.so.preload 的方式，将在所有的终端中生效。


