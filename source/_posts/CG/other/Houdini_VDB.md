---
title: Houdini细化VDB文件
date: 2021-04-22 10:53:32
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Houdini_VDB3.webp'
tags: 
    - Houdini
    - CG相关
    - VDB
categories: "CG通用相关"
---
## 问题

渲染的时候由于VDB导出密度不够导致方块状图案，可以导入houdini进行重新采样
![](/assets/blog/CG/Houdini_VDB1.webp)

## 解决
使用vdbresample获取，使用cloud noise扰乱
![基本逻辑节点如上](/assets/blog/CG/Houdini_VDB2.webp)

![调整后的结果](/assets/blog/CG/Houdini_VDB3.webp)


## 补充修订
1. octane vdb载入的云，可以直接添加osl displacement，不过调整范围和样式有限。
2. Blender里的云直接在修改器上添加displace即可
3. 大部分vdb素材精度都是够用的，如果是在某些场合精度不对，建议按照vdb本身的比例表现。
4. 如果是网上的资产，大部分是有分精度级别（如0.2，0.1，0.05，0.02，0.01），数字越小精度越高。可以优先替换一下更高精度的资产