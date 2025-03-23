---
title: OC光学工具
date: 2024-09-05 14:03:59
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_LightingTools2.webp'
tags: 
    - 累进式笔记
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---
# 问题
在Lighting过程中，可能出现需要模拟远景地面的雾气、遮光板、丁达尔光效、gobos等光学工具，来达到更好的画面效果表达。

## 目标-灯光组
有些时候需要先明确打光的点，再把灯光对准这个点。
（印象里c4d好像也有一个类似“指哪打哪”的功能，有朋友好像也把摄像机绑定到灯光片上来做类似的功能。出于个人习惯和拓展性，我还是使用target标签优先）
![target目标标签](/assets/blog/CG/Render/OC_LightingTools1.webp)
类似的还可以拓展成多个灯光组成有层次的灯光组
![内黄外蓝中间会自然产生紫色调](/assets/blog/CG/Render/OC_LightingTools2.webp)

## gobos
gobos的使用可以参考[如何在OC中使用光影贴图 gobos使用方法Using Light Gobos in Octane _ Greyscalegorilla](https://www.bilibili.com/video/BV1CR4y1s78X/?vd_source=506eb22b8d4810a2b388fa83051ccc83)。
日常准备一些gobos资产还是挺有必要的

## 远景模糊镜片、白雾片
用于营造空间感，替代medium，但是实际操作起来容易穿帮（用dirt连Opacity），效果也没有volume对象那么好。好处就是相对快一些，哪里稀薄哪里浓厚还可以自己控制。
![](/assets/blog/CG/Render/OC_LightingTools3.webp)

## 吸光体
正常的左右侧打光，要突出中间部分的对比
![](/assets/blog/CG/Render/OC_LightingTools4.webp)
使用一个带dirt的吸光体，可以整体降低中间部分的亮度
![](/assets/blog/CG/Render/OC_LightingTools5.webp)
缺点是会对其他物体也产生投影，类似于空间中存在一个隐形的吸光装置，容易穿帮，常用在比较复杂的场景里遮光。
常用在一些需要整体在前期压亮度的空间，使用球体或负空间形状。

24.5修订：可以使用不同颜色的吸光体，做到给空间染色的效果。另，如果吸光、染色效果不明显，则拉高Diffuse/Specular Depth.


## 渐变滤光片（已弃用）
前期叠渐变色滤光片容易让高光白平衡不准确，更多是模拟摄影上的用法。
例如使用偏蓝在上、偏黄在下的滤光片。或者使用上灰下透明的滤光片压低天空高光。
缺点是会明显增加渲染时长

## 不同形态灯光和使用情况
在采样效率看来，正方形比圆形、锐利边比模糊边更快达到噪点消除
从投影的柔和效果上来看，模糊边比锐利边、圆形比正方形要更柔和
低diffuse depth可以营造均匀的噪点感。
![](/assets/blog/CG/Render/OC_LightingTools6.webp)
![](/assets/blog/CG/Render/OC_LightingTools7.webp)
苛刻条件下锐利方形依然有更高的信噪比。

之前有一段时间一直用模糊边的圆形灯，渲染时长拉得好长。故此探索记录一下。
根据对投影和阴影的软硬程度使用不同的灯光。
