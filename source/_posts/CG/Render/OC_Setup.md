---
title: OC个人起始设置与资产处理
date: 2022-07-05 11:13:39
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_Setup2.webp'
tags: 
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---
> 此篇为个人习惯的参数总结，不具备普遍参考意义

## 渲染核心面板
![](/assets/blog/CG/Render/OC_Setup1.webp)
修订：D65为标准6500K，legacy可能好看一些，D65更标准一些

## imager面板
![NEUTRAL RESPONSE 默认相机会带一个tint，需要勾选自然反射获得自然效果](/assets/blog/CG/Render/OC_Setup2.webp)

## 工程结构

![](/assets/blog/CG/Render/OC_Setup3.webp)

## Stage相关：模型Phong

1. 出现过的问题：有些网上模型、自己建模的，Angle Limit没打开，或角度过大、过小。
![Angle Limit过低（特殊需要除外）着色有锯齿](/assets/blog/CG/Render/OC_Setup4.webp)
![没有打开Phong标签产生不真实光影](/assets/blog/CG/Render/OC_Setup5.webp)

2. 全选平滑着色打开：便于用较低细分实现平滑效果，避免棱角感
![](/assets/blog/CG/Render/OC_Setup6.webp)

3. 整体的模型尽量检查实例替代模型，以减少后续负载