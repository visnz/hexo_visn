---
title: 使用Blender剪辑直出子弹时间
date: 2025-03-12 23:19:32
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Blender/BulletTime.jpg'
tags: 
    - Blender
    - CG相关
categories: "Blender相关"
---
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114150114068196&bvid=BV1CYQpYgEJf&cid=28832236143&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500vh"></iframe>

# 问题
1. 制作一段动画，想要制作子弹时间。如果需要在后期调整，需要额外渲染很多的帧数

# 解决
1. 在SceneA中，提高帧速率，正常k动画。
2. 新建Scene用于剪辑，在剪辑序列中添加变速点
3. 只需要渲染最终所需的帧数，避免了多余帧的渲染