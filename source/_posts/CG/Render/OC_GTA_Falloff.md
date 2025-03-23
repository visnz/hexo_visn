---
title: OC使用全局材质输出falloff信息
date: 2024-02-22 10:53:39
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_GTA_Falloff1.webp'
tags: 
    - 多通道
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---

# 问题
1. 需要全局的falloff做后期处理

# 解决
利用global输出falloff通道
![](/assets/blog/CG/Render/OC_GTA_Falloff1.webp)
可以在多通道里查看通道的输出状况
![](/assets/blog/CG/Render/OC_GTA_Falloff2.webp)

# 拓展
基于类似的操作，可以把dirt或Imperfection贴图贴在场景内的所有物件，
后期选择性地使用柔光增加细节。