---
title: 使用Diffuse(filter info)通道在后期校准颜色
date: 2022-05-16 15:13:30
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_Diffi_title.png'
tags: 
    - 后期合成
    - AfterEffects
    - OctaneRender
    - 多通道
categories: "后期合成"
---
# 问题
角色本身的颜色受到空间光的影响，与原本设定颜色不符
灯光部分较难修改，且影响周围已处理好的场景内容
希望直接对主体进行色彩校准
# 解决
渲染Diffuse Filter info通道，将携带Diffuse色彩信息
将信息以Color混合即可还原颜色（配合物体Mask）

![](/assets/blog/CG/Comp/AE_Diffi_title.png)

# 其他
携带玻璃之类折射的区域，以及折射后面的Diffuse区域是不会被记录在Diffuse(filter info)的，也不会有折射曲率本身的计算结果。
这个通道营造的效果更像是绘画中不包含光影效果时候的固色层，是三渲二的一个路径步骤。

# 拓展
![](/assets/blog/CG/Comp/AE_Diffi.jpg)
Diffuse(filter info)配合长焦，可以浮世绘风格效果