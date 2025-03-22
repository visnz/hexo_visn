---
title: 亮度与饱和度分开调节的相关探索
date: 2024-03-16 14:01:03
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_HSV4.webp'
tags: 
    - 后期合成
    - AfterEffects
    - OctaneRender
    - 多通道
describe: ''
categories: "CG通用相关"
comments: false
---

1. 颜色有亮度，调整亮度会影响到饱和度、调整饱和度会影响到亮度。
2. 有些时候只希望Looks的颜色效果只产生颜色影响，而不产生亮度影响。

![上半为原图，下左侧为以normal混合的curve，下右侧以Lumin混合](/assets/blog/CG/Comp/AE_HSV1.webp)
直接用normal混合，可以整体压低饱和度达到一个和谐状态，
但是破坏了本身的饱和度关系，在这个基础上做色彩tint和色偏都是失真的。
这个差别，虽然可能很小。随着工程的复杂程度增多，失真会越来越严重。


# 解决
把色彩和明度分开调整，是借鉴来自手绘和摄影调色中Lab模式调色。

将两个各司其职的调整图层，以Color和Luminosity模式混合，分别管理画面饱和度和亮度
![](/assets/blog/CG/Comp/AE_HSV2.webp)

![相同的色彩调节，分开的调整更明确思路，宽容空间也更大](/assets/blog/CG/Comp/AE_HSV3.webp)

# 饱和度调节优化方案
基于前面大致了解到，调节明度会影响饱和度的值，反之调节饱和度也会影响明度值。
![使用饱和度-100% 与 tint黑白对比](/assets/blog/CG/Comp/AE_HSV4.webp)
在实践中，对于饱和度调整的图层，只使用Color模式混合，可以较好排除明度对饱和度的影响

![同样+30%的饱和度，金属暗部、画面亮部在Color模式下更自然](/assets/blog/CG/Comp/AE_HSV5.gif)

# 自然饱和度

压低Sat饱和度，提高Vib自然饱和度，再以色彩混合，获得较为自然的饱和度提升。

调整色相、饱和度的时候，添加一个高斯模糊，可以有效缓解因为色块选区/过高饱和导致的断层问题。