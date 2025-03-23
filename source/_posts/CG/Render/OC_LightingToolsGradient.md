---
title: OC光学工具：屏幕空间渐变实现裁切+屏幕空间光
date: 2024-04-10 21:23:19
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_LightingToolsGradient2.webp'
tags: 
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---

# 
## 问题

1. 有一个场景，需要把圆圈以外的区域去除掉。通常也可以在AE后期直接处理。
    ![](/assets/blog/CG/Render/OC_LightingToolsGradient1.webp)
2. 不过这里希望去除这些物件的情况下，依然保留背景，即为前期进行以“屏幕空间”角度的Opacity裁切。一定程度可以减少计算量。
## 解决
OC的材质球里，有一个节点可以实现获取screen空间的功能：
![](/assets/blog/CG/Render/OC_LightingToolsGradient2.webp)
![](/assets/blog/CG/Render/OC_LightingToolsGradient3.webp)
![](/assets/blog/CG/Render/OC_LightingToolsGradient4.webp)

## 其他
1. 类似原理可以用在比如某一个alpha的图案上，减少渲染量，但是还没有发现imageTexture可以在screen上投射。
2. 这个是基于screen空间的投射，而不是基于摄像机投射的效果，所以会一直跟随摄像机。使用摄像机投射贴图也可以做到比较奇幻的效果

## 屏幕空间渐变应射的实践
原来的灯都是D65，现在需要营造左边黄右边紫的灯。
1. 如果在左右两侧再打两盏色彩灯，光比本身就破坏了。
2. 在后期添加也可以，只不过像是车厢内部、反射细节就没有那么丰富和自然。
3. 选择把灯的颜色，按照屏幕空间投射上去。（左边黄，右边紫）这样，靠屏幕右侧的灯会渐变为紫色，靠屏幕左边渐变为黄色。

![](/assets/blog/CG/Render/OC_LightingToolsGradient5.webp)

适合某一些镜头一直在动，但持续要求画面不同角度为指定色光、或者要自然压暗的情况，不用处理灯光跟随镜头持续运动