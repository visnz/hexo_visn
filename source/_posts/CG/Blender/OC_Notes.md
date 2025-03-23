---
title: Blender使用OC相关操作备忘
date: 2024-06-09 12:14:20
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Blender/OC_Notes1.webp'
tags: 
    - Blender
    - CG相关
    - OctaneRender
categories: "Blender相关"
---

# Blender Octane太阳对象使用空对象控制

## 问题

  blender的octane中，太阳是属于世界系统，但是在控制面板中只能通过一个球来控制。

工作需要，需求变为使用空间中的一个空对象来控制。

## 解决

![](/assets/blog/CG/Blender/OC_Notes1.webp)

创建一个空对象，将空对象的xyz按照以下逻辑映射到env的xyz
驱动器逻辑：
env.sun.x = sun.x
env.sun.y = sun.z
env.sun.z = -sun.y