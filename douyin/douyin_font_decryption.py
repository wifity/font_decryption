#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : wifity

class DouYinFontDecryption(object):
    '''
    解密类
    API：
    '''

    #字体版本对应密码，与百度字体工具对应
    _version = "9eb9a50"
    _decryption_map = {"9eb9a50":
                          {"58882": 1, "58894": 1, "58904": 1,
                            "58883": 0, "58893": 0, "58902": 0,
                            "58884": 3, "58897": 3, "58906": 3,
                            "58885": 2, "58896": 2, "58903": 2,
                            "58886": 4, "58892": 4, "58905": 4,
                            "58887": 5, "58895": 5, "58907": 5,
                            "58888": 6, "58898": 6, "58911": 6,
                            "58889": 9, "58901": 9, "58910": 9,
                            "58890": 7, "58899": 7, "58908": 7,
                            "58891": 8, "58900": 8, "58909": 8,
                            "46": ".", "119": "w"
                           }
                      }

    def __init__(self):
        pass

    def decryption_num(self,data,version = "9eb9a50"):
        '''
        对外API函数，解密抖音web字符串
        :param data: 加密数字列表
        :param version: 字体版本
        :return: 解密后的数字
        '''

        if version not in self._decryption_map :
            raise ValueError("NO VERSION")
        else:
            self._version = version

            #把当前加密的数字转化成十进制字符形式
            temp = []
            for y in data:
                if ord(y) > 33:
                    temp.append(str(ord(y)))

            #每个位置单独解密
            dtemp = []
            for x in temp:
                res = self.one_d(x)
                dtemp.append(res)

            #字符计算成数字，主要考虑web版本抖音“万”位置的表示方法有很多种
            ans = .0

            #如果存在万位，乘数基准调整
            if "w" in dtemp:
                base = 10000
                dtemp = dtemp[:-1]
            else:
                base = 1

            if "." in dtemp:
                count = -1
                for zz in dtemp[::-1]:
                    # print(zz*pow(10,count))
                    if zz != ".":
                        ans = ans + pow(10, count) * zz
                        count = count + 1
            else:
                count = 0
                for zz in dtemp[::-1]:
                    ans = ans + pow(10, count) * zz
                    count = count + 1

            ans = ans * base
            ans = int(ans)

            return ans

    def one_d(self,strnum):
        '''
        单个数字解密
        :param strnum: 单个加密数字或者. 或者 w （万）
                格式是十六进制的转十进制在转成字符串形式，主要方便字典查询
        :return:
        '''
        return self._decryption_map[self._version][strnum]


if __name__ == '__main__':
    dyfd = DouYinFontDecryption()
    print("关注数：",dyfd.decryption_num("    "))
    print("粉丝数：",dyfd.decryption_num("        .  w "))
    print("点赞数：",dyfd.decryption_num("          .  w "))
    ##测试为 啊纯的主页，本文件夹下查看写代码时候的截图