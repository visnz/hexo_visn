---
title: OC/AE 后期法线光
date: 2024-06-27 11:23:46
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_NormalLighting3.webp'
tags: 
    - 后期合成
    - AfterEffects
    - OctaneRender
    - 多通道
categories: "后期合成"
---
## 问题
![](/assets/blog/CG/Comp/AE_NormalLighting1.webp)
海底场景已经足够复杂，现在需要勾勒底部的立体感，担心再添加灯光，会加大计算量，且效果调整较难控制。

于是尝试使用世界法线Shading进行后期打光塑形

## 解决
1. 渲染设置选择Normal(shading)通道，以及需要调整的部分单独传送到一个CustomAOV通道
    ![](/assets/blog/CG/Comp/AE_NormalLighting2.webp)
2. 得到的三个RGB通道，分别对应三个坐标轴的单向光
    ![](/assets/blog/CG/Comp/AE_NormalLighting3.webp)
3. 根据需求提取不同方向需要加强的光，以softlight混合以强化光影
    ![](/assets/blog/CG/Comp/AE_NormalLighting4.webp)
4. 这样可以避开原本不容易打出光感的空间，在后期单独加强空间感和光。
    ![](/assets/blog/CG/Comp/AE_NormalLighting5.webp)

