---
title: C4D使用Standard渲染器渲染Mask
date: 2021-03-09 19:24:01
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/C4D/C4D_mask5.webp'
tags: 
    - Blender
    - CG相关
    - OctaneRender
categories: "Blender相关"
---
## 问题
oc跑完了，发现忘记设置mask
## 解决
1. 给物体设置渲染标签![](/assets/blog/CG/C4D/C4D_mask1.webp)
2. 设置object buffer (2/3/4...)![](/assets/blog/CG/C4D/C4D_mask2.webp)
3. 渲染设置-默认渲染器，多通道，添加Object buffer![](/assets/blog/CG/C4D/C4D_mask3.webp)![](/assets/blog/CG/C4D/C4D_mask4.webp)
4. 上面regular image可以不保存，看需求。渲染视图选单通道查看渲染效果![](/assets/blog/CG/C4D/C4D_mask5.webp)
## 后记
1. 不会像oc的Cstm一样带反射信息和折射信息，跟Cryptomatte的选区接近。
2. 抗锯齿效果较差，尺寸记得开大一些，后期再加个模糊或FXAA