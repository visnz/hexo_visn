---
title: C4D/OC Scatter做简单摇曳草地
date: 2023-04-15 12:51:49
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_ScatterWiggle1.webp'
tags: 
    - CG相关
    - OctaneRender
    - Cinema4D
categories: "渲染器相关"
---
## 问题
需要制作一些草以一种浪的形式摇曳的效果。用克隆也可以的，克隆也支持更复杂的效果，编辑预览的时候可能会卡一些，量大记得切换到渲染实例。
![效果](/assets/blog/CG/Render/OC_ScatterWiggle1.webp)


## 解决
1. 创建草分布，简单做一下垂直地面的高度偏移Random
    ![](/assets/blog/CG/Render/OC_ScatterWiggle2.webp)
2. 添加一个模拟大范围摇曳的随机效果器
    ![](/assets/blog/CG/Render/OC_ScatterWiggle3.webp)
![](/assets/blog/CG/Render/OC_ScatterWiggle4.webp)
3. 同理再添加一个小范围摇曳的效果器
    ![](/assets/blog/CG/Render/OC_ScatterWiggle5.webp)
4. 可以配合域控制不同区域的不同效果
    ![调整到满意即可](/assets/blog/CG/Render/OC_ScatterWiggle1.webp)

## 其他
1. C4D贴图好像都缺少贴图空间的z轴移动效果，建议blender
2. 在大范围场景，配合megascans的草素材，不卡效果也还可以。