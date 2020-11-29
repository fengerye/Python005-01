# Python 基本数据类型

## 1 数值

### 1.1 整数

整数：int 类型

赋值例如：

Num1 = 32

运算：+ - * /

除法运算 (`/`) 永远返回浮点数类型，取整：`//` 、获得余数`%`

乘方：`**`

赋值：`=`





### 1.2 浮点数

浮点数：float 类型

赋值例如：

`number = 13.31`

### 1.3 复数

使用 j 或者 J 表示虚部

如：

`num = 3+5j`

### 1.4 Decimal 对象

decimal - 十进制定点和浮点的运算

decimal 数值是不可变对象。 它由符号，系数和指数位组成。

### 1.5 fractions

fractions - 分数



## 2 字符串

使用单引号或者双引号来定义

特殊字符使用反斜杠来使用转义

```
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
```

字符串字面值可以跨行连续输入。一种方式是用三重引号：`"""..."""` 或 `'''...'''`。

```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

`+` 粘连

`*` 重复

字符串是可以被 *索引* （下标访问）的，第一个字符索引是 0。

负数索引从 -1 开始。



## 3 列表

通过方括号括起、逗号分隔的一组值（元素）得到。一个 *列表* 可以包含不同类型的元素，但通常使用时各个元素类型相同。

例如：

`squares = [1, 4, 9, 16, 25]`

列表也支持索引和切片

所有的切片操作都返回一个新列表，这个新列表包含所需要的元素。

## 4 布尔值

ture or false





