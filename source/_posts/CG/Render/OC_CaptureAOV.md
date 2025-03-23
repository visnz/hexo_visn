---
title: OC使用captureAOV捕获材质选区
date: 2024-04-21 15:51:29
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_CaptureAOV1.webp'
tags: 
    - 多通道
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---

## 问题

  对于某一个材质，被上在不同的材质分区、不同的物体，想要把这一整个材质作为选区输出进行调整（比如提亮整个材质）

## 解决过程
  Cryptomatte输出的pin matID通道时，无法选中带有运动模糊和对焦外、透射以及反射部分的选区。
  oc标签上在物体上，Cstm通道会连同整个物体通道输出。

## 解决

![原本结构](/assets/blog/CG/Render/OC_CaptureAOV1.webp)
添加一个captureAOV，将Albedo信息传递到AOV，然后再传回Albedo。（其实传Opacity更好，可以配合Rayswitch做更多的操作）
![如右上角连接](/assets/blog/CG/Render/OC_CaptureAOV2.webp)

另外，可以配合Gradient到RGB，塞进Custom的单一通道里
![省点硬盘空间小能手](/assets/blog/CG/Render/OC_CaptureAOV3.webp)

剩下的就输出再在后期以Mask相乘调整即可