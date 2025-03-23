---
title: Blender更换已绑定好人物的初始姿势
date: 2024-07-15 07:25:40
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/Blender/RestPose1.webp'
tags: 
    - Blender
    - CG相关
    - 绑定
categories: "Blender相关"
---

## 问题
由于需要制作高跟鞋，人物原本的脚是平底的状况，进入模型编辑之后，立起来的脚就会变回原本平底的模型的样子。
![](/assets/blog/CG/Blender/RestPose1.webp)
现在需要把骨骼摆好的模型效果传递回去原本模型。之后才能再模型上修改制作高跟鞋
![](/assets/blog/CG/Blender/RestPose2.webp)

## 解决
Ctrl+A 类似于C4D里的C，会把结果计算到模型上![](/assets/blog/CG/Blender/RestPose3.webp)
重新添加骨骼修改器，指定骨骼
![](/assets/blog/CG/Blender/RestPose4.webp)

在Pose Mode里，继续使用应用，把Pose设置为Rest Pose
![](/assets/blog/CG/Blender/RestPose5.webp)
