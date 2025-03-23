---
title: ACES操作简记
date: 2021-06-12 20:43:12
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Aces3.webp'
tags: 
    - ACES
    - CG相关
    - AfterEffects
    - OctaneRender
    - 后期合成
categories: "CG通用相关"
---

> 使用最新AE 请直接看第三部分修订稿

# 1 OC（实践摘录）

> octane>2020.2

oc设置里先载入配置，将oc色空间调整到aces2065-1，将ocio文件选择为aces下的aces2065-1标准，这样才能在标准2065色空间下正常运行

![](/assets/blog/CG/Aces1.webp)

渲染设置里选择色空间，输出到sRGB，也可以输出到aces2065以保持更大的色空间，需要在ae里同步设置下读取aces2065色空间

![](/assets/blog/CG/Aces2.webp)


选择摄像机视口投射到sRGB色空间，才跟渲染一致
![](/assets/blog/CG/Aces3.webp)

# 2 AE

[OpenColorIO.aex](https://www.alipan.com/s/RAn98NsED2L) 提取码: kh66

工程设置：16/32位 + sRGB（这里指最后需要输出的空间）

如上oc输出的是aces2065-1，线性空间无需勾选（因为aces里就是线性空间了，这里线性空间是一层gamma转换）
![](/assets/blog/CG/Aces4.webp)

素材设置解释：保持原本色彩空间（RS不需要设置解释）
![](/assets/blog/CG/Aces5.webp)

进行调整
![](/assets/blog/CG/Aces6.webp)

最顶层添加较准效果器 ：使用对应色域如 ACES2065-1 to OutputsRGB

![](/assets/blog/CG/Aces7.webp)

# 3 修订

AE2023之后，已经开始内置了aces流程，无需加载插件

![](/assets/blog/CG/Aces8.webp)

对应的素材解释记得调整成前期渲染的色彩空间

然后，再在输出序列的界面，把输出设置里的颜色改为以sRGB输出
![](/assets/blog/CG/Aces9.webp)

另外，ae2023的色空间默认是Adobe sRGB 会跟默认输出的sRGB有细微差别。

# 4 参考资料
1. [起底C4D的ACES工作流](https://www.bilibili.com/video/BV1Ni4y1K7Ty/)