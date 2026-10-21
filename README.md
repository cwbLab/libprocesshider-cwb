libprocesshider
===============

Hide a process under Linux using the ld preloader.

Full tutorial available at [https://sysdigcloud.com/hiding-linux-processes-for-fun-and-profit/](https://www.sysdig.com/blog/hiding-linux-processes-for-fun-and-profit)


# 第一步
首先编辑processhider.c文件，修改process_to_filter变量的内容，所有具有此名称的进程都将被隐藏。

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
root@sid:~# echo /usr/local/lib/libprocesshider.so >> /etc/ld.so.preload
```

And your process will be off the radar 

```
gianluca@sid:~$ sudo ps aux
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
...

gianluca@sid:~$ sudo lsof -ni
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
...
```
