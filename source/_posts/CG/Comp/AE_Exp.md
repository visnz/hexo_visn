---
title: AE表达式的一些奇怪玩法
date: 2020-10-12 11:33:36
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_Exp2.webp'
tags: 
    - AfterEffects
categories: "后期合成"
---
这里记录一下早期使用ae工作时候，用过的ae表达式奇怪玩法

## 图片、视频模板的预合成
1. 套用图片模板的时候，将所有图片以每张图一帧，汇总在单个合成中。使用冻结帧+帧数作为索引，这样就可以把所有图片汇总到一个合成中。（来自老鹰AE）
2. 相同的思路也可以应用到视频，使用Essential Graphic功能。所有视频丢到同一个合成，使用一个参数控制出现图层数，每个素材的透明度判断图层index是否等于参数值。外部暴露这一个参数。这样就可以实现一个合成套全部的模板。

## 自适应大小
```
sourceRectAtTime()
```
获取图层的宽高，适合获取动态变化的图层的实时大小，如变化的图形图层与字体图层
```
a = thisComp.layer("Text1").sourceRectAtTime();
```
在此基础上，判断字体图层的变化，适配背景框的大小之类的操作

## 自动渐变过渡

由于不像pr里存在同一图层多个素材，在用ae剪辑的时候要做叠化得手k，好麻烦。

```
var End=thisComp.layer(thisLayer.index+1).outPoint
var Start=thisLayer.inPoint
linear(time,Start,End,0,100)
```
写一个表达式，使得下一个出现的图层，判断时间自然叠化进来。
![](/assets/blog/CG/Comp/AE_Exp1.webp)

## 路径点位置
```
path.pointonpath(0.5)
```
获取一条路径对象的50%的位置。用于对象附着，或多个对象一起跟随路径移动。

## 跳帧渲染-AE后期后的抽帧再导出
比如C4D渲染0,60,120,180,240这样一组关键帧，在ae里按照一整个逐帧调整之后，总不可能240帧全部输出出来，毕竟只需要这5帧就行。

把合成丢进一个新的只有5帧的和成立，用一个表达式控制timeRemap
```
((thisLayer.index-1)*60)/(1/thisComp.frameDuration)
```
![](/assets/blog/CG/Comp/AE_Exp2.webp)

