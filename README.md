# hexstr
simple python function for printing a string as little endian words

Works on both Python2 and Python3.

I created this little python module because recently I was using GDB on a 
C program I wrote and wanted an easy way to find my C string when I printed 
the stack with something like:

```gdb
x/100x $sp
```

Therefore, the string returned by this function has a very similar layout: 
columns of little endian hex words in rows of 4, separated by tab.

## Usage

There are two ways to use this...

### As a module in your own python script / program

```python
from hexstr import hexstr
mystr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
words = hexstr(mystr)
print(words)
```

### On the command line as standalone

```bash
$ python hexstr.py 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
```
or
```bash
$ ./hexstr.py 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
```

### Output 

for all 3 above cases:

```
0x64636261	0x68676665	0x6c6b6a69	0x706f6e6d
0x74737271	0x78777675	0x42417a79	0x46454443
0x4a494847	0x4e4d4c4b	0x5251504f	0x56555453
0x5a595857	0x33323130	0x37363534	0x00003938

```
