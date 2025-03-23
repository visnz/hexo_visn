---
title: OC烘焙不同选区纹理进同一张贴图
date: 2024-07-25 09:21:42
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Render/OC_Baking3.webp'
tags: 
    - 多通道
    - CG相关
    - OctaneRender
categories: "渲染器相关"
---

## 问题
有一个带UV的模型，存在多个选区材质，已经在OC里做好Lookdev
需要烘焙之后同步到游戏软件中使用

现在需要把多个材质，按照选区烘焙在同一张贴图上。
无法使用C4D默认的baking texture烘焙。

## 解决
1. 确保模型存在UV，并加上oc物体标签
    ![](/assets/blog/CG/Render/OC_Baking1.webp)

2. 创建baking摄像机之后，Main图下可以烘焙带光照信息的贴图，但是需要的是不同层的贴图
    ![](/assets/blog/CG/Render/OC_Baking2.webp)

3. 进入每一个材质，把需要输出的通道，通过CutsomAOV输出
    ![](/assets/blog/CG/Render/OC_Baking3.webp)

4. 把Albedo烘焙到Custom2，其他依次操作
    ![](/assets/blog/CG/Render/OC_Baking4.webp)

5. 就是操作上繁琐了一些
    ![](/assets/blog/CG/Render/OC_Baking5.webp)

## 注意事项
1. 记得不要勾选带反射和折射通道
    ![](/assets/blog/CG/Render/OC_Baking6.webp)
2. 重新载入进来之后，在线性空间下使用2.2*1.5的gamma空间转换
    ![](/assets/blog/CG/Render/OC_Baking7.webp)

## 修订
1. 对于同一个工程需要烘焙多个不同对象的，在oc标签里设置不同的UV Group，然后再在摄像机里切换不同的UV组
    ![](/assets/blog/CG/Render/OC_Baking8.webp)
2. 导出之后使用这个脚本给“Cstm2/3/4/5/6/7”替换成“Albedo/Roughness……”之类的
    ```
    for i in `ls|grep Cstm2`;do mv $i `echo $i|sed 's\Cstm2_0000\Albedo\g'`;done;
    for i in `ls|grep Cstm3`;do mv $i `echo $i|sed 's\Cstm3_0000\Specular\g'`;done;
    for i in `ls|grep Cstm4`;do mv $i `echo $i|sed 's\Cstm4_0000\Metallic\g'`;done;
    for i in `ls|grep Cstm5`;do mv $i `echo $i|sed 's\Cstm5_0000\Roughness\g'`;done;
    for i in `ls|grep Cstm6`;do mv $i `echo $i|sed 's\Cstm6_0000\Bump\g'`;done;
    for i in `ls|grep Cstm7`;do mv $i `echo $i|sed 's\Cstm7_0000\Normal\g'`;done;
    for i in `ls|grep Cstm8`;do mv $i `echo $i|sed 's\Cstm8_0000\Emission\g'`;done;
    ```
