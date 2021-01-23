---
author: 111qqz
date: 2017-06-08 13:03:51+00:00
draft: false
title: conda升级anaconda　ValueError的解决办法
type: post
url: /2017/06/how-to-fix-conda-upgrade-valueerror/
categories:
- 其他
tags:
- anaconda
- python
---

conda update anaconda　后提示
    
    ValueError: unsupported format character ')' (0x29) at index 49


查到了这个：[anaconda update issue](https://github.com/conda/conda/issues/564)


<blockquote>I have narrowed this down to the following packages:
<table >

<tr >
package
build
</tr>

<tbody >
<tr >

> <td >psutil-1.2.1
> </td>

> <td >py27_0 hard-link
> </td>
</tr>
<tr >

> <td >pycparser-2.10
> </td>

> <td >py27_0 hard-link
> </td>
</tr>
<tr >

> <td >pykit-0.1.0
> </td>

> <td >np18py27_2 hard-link
> </td>
</tr>
<tr >

> <td >pyparsing-2.0.1
> </td>

> <td >py27_0 hard-link
> </td>
</tr>
</tbody>
</table>
by calling "conda install anaconda" and then successfully installing everything else one at a time.
These four packages consistently exhibit the described behaviour.
(note: pykit depends on pycparser so may itself be ok - can't tell)</blockquote>




我先把psutil卸载掉，重新update了一下，成功。

    
    conda remove psutil



