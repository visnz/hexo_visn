---
title: OC多通道与AE后期简述
date: 2021-03-21 11:28:16
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_OC_Multi1.webp'
tags: 
    - 后期合成
    - 累进式笔记
    - AfterEffects
    - OctaneRender
    - 多通道
categories: "后期合成"
---
## 常见的三维后期通道

1. 主要使用oc的PT路径追踪，oc通道主要分为以下几类
    1. info信息类通道：无需启用PT计算就可以产出的通道：如Z-depth、UVW、Position等跟场景信息相关的
    2. 路径追踪pt相关通道：跟正片Main渲染相关的通道，如Refl、Refr、Li、ObjMask、Shadow、SSS、Transmission、PostProcessing等跟渲染、灯光效果相关的，**也是主要的计算量所在**。
    3. 特殊合成通道：cryptomatte加密通道、deep深度通道

2. 个人常用通道
    1. 灯光类：SLi、ALi、Li1-8、Shadow（开启Shadow画面会多一些噪点，夜景最好别开）
    2. 材质类：Refl、Refr、SSS、Dif、Dif(infofilter)
    3. info类：Z-depth、UVW、Position、AO
    4. 遮罩类：Custom、Opacity、cryptomatte、Volume

![cryptomatte记得使用pin类，不然每次都是随机](/assets/blog/CG/Comp/AE_OC_Multi1.webp)

## 合成用法
### 配光类
1. 使用Li层-overlay/add/sub：分别加强对比、提亮和减弱对应灯光组的效果
    1. 同时配合deepglow可以完成单组灯光辉光
    2. 调整色相，再使用色相混合可以改变灯光颜色
2. 使用shadow层
    1. 单独调整shadow阴影颜色、作为mask降噪
    2. 乘系混合强化阴影
### 材质加强
1. SSS/Specular/Transmission层-overlay/add/sub：相关材质通道对材质的调整
2. AO、材质通道配合Find edge，以softlight混合，可以提升整体细节质感
### 空间感
1. Z-depth直接加系混合，制造远景雾气效果
### 色彩类
1. 滤镜：Looks、Filmconvert
2. 饱和、对比、亮度、lumetri色调、色彩平衡
3. 暗角：vignette、中间拉亮
4. 遮罩配光
5. 加噪点、锐化add grain/sharpen
6. 边缘色差
### 补充类
1. 发光：Realglow、OpticalFlare（加镜头脏渍、镜头光晕）
2. 动态模糊：RSMB
3. FXAA/FindEdge+Blur抗锯齿
4. 边缘色彩偏移+光学补偿畸变
5. 添加额外素材（雾气、光柱、飞鸟、群星、火、雨、彩虹等） 
6. 烟雾合成：Unmult+Fill场景色，有需要再*Z
7. 后期菲涅尔：FindEdge+tint+Softlight
8. Optical Flare 后期光晕
9. 梦幻感：Glow/Real Glow/Deep Glow
10. 镜头模糊