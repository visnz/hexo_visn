---
title: Houdini合并场景环状云
date: 2024-08-22 20:18:42
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/other/Houdini_VDB_instance1.webp'
tags: 
    - Houdini
    - CG相关
    - VDB
categories: "CG通用相关"
---
## 问题
![](/assets/blog/CG/other/Houdini_VDB_instance1.webp)

## 需求
做了一张海岛的地图，现在要在上面加上环状的云
![](/assets/blog/CG/other/Houdini_VDB_instance2.webp)

## 思路
使用Houdini进行扭曲-合并-切除再导出

## 操作记录
1. 导入地形模型和贴图，作为参考
    ![](/assets/blog/CG/other/Houdini_VDB_instance3.webp)
2. file导入vdb文件，移动轴心，并且稍微拉长以适配扭曲
    ![](/assets/blog/CG/other/Houdini_VDB_instance4.webp)
3. 连接volumedeform节点，中间添加bend节点
    ![](/assets/blog/CG/other/Houdini_VDB_instance5.webp)
4. 合并并裁切
    ![](/assets/blog/CG/other/Houdini_VDB_instance6.webp)
5. 最后再合并、模糊等操作然后导出
    ![](/assets/blog/CG/other/Houdini_VDB_instance1.webp)