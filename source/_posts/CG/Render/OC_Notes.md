---
title: Octane小问题持续记录
date: 2022-10-21 19:51:23
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_Notes1.webp'
tags: 
    - 累进式笔记
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---
# 解决AO通道中隐藏光产生的额外AO
## 问题
![](/assets/blog/CG/Render/OC_Notes1.webp)
发光体在空间里隐藏了，但是无论怎么调整（dirt可见性、边缘可见性、投影可见性），AO通道里都会有灯光的AO

## 解决
AO计算模式，有一种是按照物体的空间存在，另一种是按照物体的透明度计算
![打开一下](/assets/blog/CG/Render/OC_Notes2.webp)
![就好了](/assets/blog/CG/Render/OC_Notes3.webp)
