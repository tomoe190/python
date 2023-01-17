# -*- coding:UTF-8 -*-

# author:tomoe
# contact: test@test.com
# datetime:2023/1/16 14:12
# software: PyCharm

"""
文件说明：
    
"""
import os
import subprocess

p = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
out = p.stdout.read()
print(out)

# a = os.system("ipconfig")
# print("---------------")
# print(a)


