---
title: OSL笔记
date: 2024-04-01 20:33:36
aubot: 可能是水桶吧
aubot_link: '/index.html'
cover: '/assets/blog/CG/OSLnote/title.png'
tags: 
    - OSL
    - CG相关
    - TA
    - OctaneRender
categories: "CG通用相关"
---

使用OctaneRender探索了一下OSL摄像机

# OSLcamera斜切镜头
![](/assets/blog/CG/OSLnote/1.jpg)
一个可以对画面进行y轴斜切操作的摄像机osl（会引入视图摄像机看不到的地方）
```c
shader OslCamera(
    float index = 1.0[[ float min = -10.0, float max = 10.0 ]],
    output point pos = P,
    output vector dir = 0,
    output float tMax = 1.0/0.0){
        float uv[2];
        getattribute("hit:uv", 2, uv);
        dir = point("camera", (uv[0]-.5),(uv[1]-.5)+index*(uv[0]-.5)*abs((uv[0]-.5)), -1.0);
}
```
同理，可以把uv的1和0互换，变成x轴斜切
```c
shader OslCamera(
    float index = 1.0[[ float min = -10.0, float max = 10.0 ]],
    output point pos = P,
    output vector dir = 0,
    output float tMax = 1.0/0.0){
        float uv[2];
        getattribute("hit:uv", 2, uv);
        dir = point("camera", (uv[1]-.5),(uv[0]-.5)+index*(uv[1]-.5)*abs((uv[1]-.5)), -1.0);
}
```
在上面这个基础上，可以开发远处大广角、近处长焦的、类似三角形拉扯的视野效果（不会变空间透视和前后节奏）

# OSL鱼眼镜头
来自大佬的OSL摘抄，稍微修改了初始参数。
早期OC还不支持超广角鱼眼的时候，就会使用这个镜头

```c
// Simulates a fisheye lens with an attempt at DOF...
// Comments to James@liminaltv.co.uk
shader OslCamera(
  float aperture = 0.01 [[ float min = 0.0, float max = 100.0 ]],
  float focusDistance = 5.0 [[ float min = 0.0, float max = 100.0 ]],
  float FOV = 150.0 [[ float min = 1.0, float max = 360.0 ]],
    output point  pos  = P,
    output vector dir  = 0,
    output float  tMax = 1/0.0)
{
  float angle = atan2(u-0.5,v-0.5);
  float r = sqrt((u-0.5)*(u-0.5)+(v-0.5)*(v-0.5))/1.43;
  if(r>=0.5) {dir = 0; return;}
  float alpha = linearstep(0,0.5,r)*M_PI_2*FOV/180.0;
  //let's jitter p with some time noise...
  float apHeading = noise("noise",time*5679+1234+u*7879+v*7321)*2.0*M_PI;
  float apRadius = noise("noise", time*4567+2345+u*456+v*983)*aperture/2.0;
  point source = point("camera",sin(apHeading)*apRadius, cos(apHeading)*apRadius,0.0);
  point target = point("camera",focusDistance*sin(angle)*sin(alpha),focusDistance*cos(angle)*sin(alpha),-focusDistance*cos(alpha));
  dir = target-source;
    pos = source;
}
```
相比目前新版本的OC自带的鱼眼摄像头，感觉这个OSL的范围和畸变比官方自带的更真实一些

# OSL 云置换
blender中直接由修改器的displace完成，C4D中oc的vol对象只能通过这个OSL接口输入完成修改
```c
shader disp(
    float amount=5[[float slidermin=0, float slidermax=10, float min=0]],
    float freq=1[[float slidermin=0, float slidermax=10]],
    float displacer=0.5[[float slidermin=0, float slidermax=1, float min=0]],
    float dispFreq=3[[float slidermin=0, float slidermax=10]],
    output color c = 0)
{
    point p = P+displacer*snoise(dispFreq*freq*P);
    c = amount*(snoise(freq*p));
}
```

# 高斯模糊
此代码为OC官方内置公开的代码，搬运保留，以便使用
```c
// 输入端口1为贴图（需要将投射方式改为OSL投射或OSL延迟UV）
// 输入端口2为重复次数，0~10
// 输入端口3为重复范围，以uv计算。0.01即为1%的范围。
//
// 题外话：主要是有OSL延迟UV（_evaluateDelayed这个函数）使得各种贴图处理都要简单一些
// Blender之中使用节点复刻高斯模糊，处理思路也跟这个差不多

#include <octane-oslintrin.h>

#define MAX_ITERATIONS  10
#define MAX_KERNEL_SIZE 11 // MAX_ITERATIONS + 1

// OSL sample implementation of gaussian blur for Octane Render
shader GaussianBlur(
    color in = 0
        [[string label = "Input texture"]],
    int iterations = 5
        [[int min = 0, int max = MAX_ITERATIONS,
          string label = "Step count",
          string description = "Number of steps"]],
    float stepSize = 0.001
        [[float min = 0.00001, float max = 0.01,
          string label = "Step size",
          string description = "UV distance between steps"]],
    output color out = 0)
{
    if (iterations == 0)
    {
        // just return the input with the right UV mapping
        out =  _evaluateDelayed(in, u, v);
    }
    else
    {
        float kernel[MAX_KERNEL_SIZE];

        // initialize the kernel
        float normFactor = 0;
        for (int i = 0; i <= iterations; ++i)
        {
            // use normal probability density function with sigma = 7
            float n  = 0.05699175 * exp(-0.01020408 * i * i);
            normFactor += i == 0 ? n : 2*n;
            kernel[i] = n;
        }

        // average the neighbours
        color c  = 0;
        for (int i = -iterations; i <= iterations; ++i)
        {
            float n = kernel[iterations - abs(i)];
            for (int j = -iterations; j <= iterations; ++j)
            {
                float f = n * kernel[iterations - abs(j)];
                c += f * _evaluateDelayed(in, u + i * stepSize, v + j * stepSize);
            }
        }

        // calculate the final value
        out = c/(normFactor*normFactor);
    }
}
```