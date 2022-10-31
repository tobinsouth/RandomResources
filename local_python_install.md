# Installing a local python on a linux server

I don't want to use the global python because problems arise.

Download the python version to the user directory.

```bash
mkdir ~/python      
cd ~/python
wget https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tgz
tar zxfv Python-3.10.6.tgz
find ~/python -type d | xargs chmod 0755
cd Python-3.10.6

```

We then compile the python.

```bash
./configure --prefix=$HOME/python --enable-optimizations --with-system-ffi
make && make install

```


We then need to edit the `~/.bashrc_profile` to include:
```bash
export PATH=$HOME/python/Python-3.10.6.tgz/:$PATH
export PYTHONPATH=$HOME/python/Python-3.10.6.tgz
```
Don't forget the `source ~/.bashrc_profile`


```bash
echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc_profile
```



If you get the ctypes issue then install libffi and remake



