---
title: AE制作不过曝不灰蒙蒙的deepglow效果
date: 2023-10-21 19:21:02
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_Deepglow1.webp'
tags: 
    - 后期合成
    - AfterEffects
categories: "后期合成"
---
![gif演示效果](/assets/blog/CG/Comp/AE_Deepglow1.webp)

## 问题

单一一张图片来做后期，直接开deepglow（500%threshold，参数如图）会感觉整体都很过曝，整体看起来灰蒙蒙的，原因是暗部虽然已经被过滤但不够完全保留亮部

![](/assets/blog/CG/Comp/AE_Deepglow2.webp)

## 解决

1. 尝试把图片的亮部提取出来，只对这部分进行发光，再叠加回去
2. 再把图片的最高光部分做保护，以看起来不要像失误过曝，保留层次感。

## 操作
1. 复制一层图片，用曲线和色阶等工具，把最亮部分提取出来，并施加deepglow。![](/assets/blog/CG/Comp/AE_Deepglow3.webp)
2. 再把这张图以screen叠回去，然后发现高光部分过曝![](/assets/blog/CG/Comp/AE_Deepglow4.webp)
3. 复制一份原图，把更更更高光的部分（想要保留细节的部分）提取出来，这里叠了三个一样的曲线，把最高光部分提取出来![](/assets/blog/CG/Comp/AE_Deepglow5.webp)
4. 再把这张图的原图以这个亮度相乘，叠放在最上面![](/assets/blog/CG/Comp/AE_Deepglow6.webp)

结果如最上图，高光发光但不过曝保留细节
![](/assets/blog/CG/Comp/AE_Deepglow1.webp)

## 其他
1. deepglow层使用明度混合能达到更真实的效果
2. oc的post processing还是会比这种后期加的效果更好一些。
3. 可以单独对Ref层使用。