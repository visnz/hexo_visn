---
title: AE预览卡顿优化
date: 2020-04-11 21:20:16
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_Q3.webp'
tags: 
    - 后期合成
    - AfterEffects
categories: "后期合成"
---
## 问题

随着工程量的增加，AE预览逼近帧速率处理的极限，就开始卡顿了

## 预览卡顿的主要原因
计算时长较长，导致较长的原因有
1. 画面分辨率过大
2. 效果解析需要的计算量过大
3. 逐帧播放要求计算必须要足够快
4. 实时计算，边播放边计算
5. 整个画面进行计算，计算量巨大
---
应对以上几点，分别需要调整
1. 降低合成分辨率（合成设置）、降低预览分辨率
    ![](/assets/blog/CG/Comp/AE_Q1.webp)
2. 暂时关闭部分效果器、暂时关闭（或独显）部分图层。
3. 可以具体了解是否某些效果的计算量过大，避免使用或暂时隐藏（如粒子）。
4. 调整预览的完整度
    ![](/assets/blog/CG/Comp/AE_Q2.webp)
5. 跳过一些帧，可以在preview面板调整Skip数值（跳过帧）
    ![](/assets/blog/CG/Comp/AE_Q3.webp)
6. 主动缓存（直接按播放一遍）
7. 选择部分区域播放计算
    ![](/assets/blog/CG/Comp/AE_Q4.webp)

## 参考链接
[官方的指南](https://helpx.adobe.com/cn/after-effects/using/previewing.html)

