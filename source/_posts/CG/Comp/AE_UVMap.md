---
title: 在AE用uv通道映射视频到三维曲面
date: 2023-12-27 21:24:06
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Comp/AE_UVMap2.webp'
tags: 
    - 后期合成
    - AfterEffects
    - OctaneRender
    - 多通道
categories: "后期合成"
---
## 问题

需要将左侧视频片段，按uv投射到右侧球幕
![](/assets/blog/CG/Comp/AE_UVMap1.webp)
丢进c4d渲染，渲染时长较长（900帧视频，720p100采样，需要30分钟 4090）

## 解决
由于右侧是静态镜头，只需要渲染一帧白色底+uv贴图，即可在后期使用uv信息，把视频片段映射到右边球幕。渲染时长只需要ae导出的时长。
![](/assets/blog/CG/Comp/AE_UVMap2.webp)
1. 需要先输出原图和oc的16bit的uv图（不要用standard的uv，有错位）
    ![](/assets/blog/CG/Comp/AE_UVMap3.webp)
2. 使用ft-uvpass插件，指定材质图，切换到effects&mask方便后续在材质贴图上微调。下面的offset、tile分别调整偏移和重复
    ![image.png](/assets/blog/CG/Comp/AE_UVMap4.webp)

3. 缺点：tile重复，只能是整倍数。在tile调整整数倍之后，需要给texture添加transform效果微调直至与需求贴合
    ![](/assets/blog/CG/Comp/AE_UVMap5.webp)

## 拓展
1. 可以拓展到飘扬的旗帜（柔面）、后期建筑的细节添加（置换面）、翻书模板中书每一页的内容替换等
2. 缺点1：边缘会细节会丢失，32bit也会。适合用于中远景的细节增加和不需要考虑过高细节的边缘融合的后期材质替换。像翻书那种翻到中间，视角跟页面垂直的时候容易显得粗糙（可结合动态模糊解决）。
3. 缺点2：由于是后期映射，不存在前期的阴影和光照信息。可以用demain使用明度混合还原。但后期材质不会跟环境有关系。
4. 缺点3：无法配合oc中带反射与折射信息的custom通道做细节的后期材质添加，uv通道属于info不记录折射投射信息。

## 修订

1. 如果出现马赛克问题，请提高工程精度
    ![](/assets/blog/CG/Comp/AE_UVMap6.webp)
    ![](/assets/blog/CG/Comp/AE_UVMap7.webp)
2. 出现这种情况，uv通道可能不是16bit及以上
    ![](/assets/blog/CG/Comp/AE_UVMap8.webp)
