---
title: OC scatter场景分布（摄像机外剔除）
date: 2022-12-03 22:11:19
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_Scatter3.webp'
tags: 
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---

## 问题

1. 由于场景过大，希望可以剔除摄像机看不到的地方
2. 摄像机会摇，结合定点贴图会导致oc scatter分布闪烁的bug，也就是要在一开始要计算出全部的范围。

（原问题描述：当oc scatter需要铺满一个小山坡的草的时候，山坡背面、摄像机以外的区域在渲染的时候无需使用的情况下，除掉非视野部分。）

## 解决（1阶段）
通过顶点贴图+域排除掉非视野部分。这个方法仅适用于静帧，因为随着摄像机移动，顶点贴图会重新计算，草的位置会不断跳变。

1. 在地形上创建顶点贴图![](/assets/blog/CG/Render/OC_Scatter1.webp)
![使用域控制，并删除冻结](/assets/blog/CG/Render/OC_Scatter2.webp)

2. 使用法线排除某一个方向的，法线方向与摄像机方向相反，使用（effect-falloff）排除非摄像机角度的oc scatter分布
3. 使用跟随摄像机的锥形域，与上述法线域相乘。
4. 使用地平线以上的线性域，与上述相乘
5. 使用一个噪波添加随机。

![](/assets/blog/CG/Render/OC_Scatter3.webp)
这样就仅在摄像机可见范围内、地平线以上的区域出现草，进而减少机器负载

## 解决（2阶段）

在动画上的应用：

可以通过decay记忆画笔+freeze计算出摄像机移动轨迹过程中，所有看到的区域，并记录。

然后只在此区域进行显示，也可以避免过多资源浪费。
![](/assets/blog/CG/Render/OC_Scatter4.webp)
decay用于计算经过的区域，类似画笔。

freeze用于计算缓存结果并保存。

这样就不会因为变换顶点贴图而导致scatter分布各个草的位置跳动了，适用于超大规模场景的优化。