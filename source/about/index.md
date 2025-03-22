---
title: 关于我
date: 2025-03-21
aubot: 可能是水桶吧
portrait: '../assets/blog/about/d.webp.jpg'
describe: '望向十倍遥远的星空'
type: "about"
layout: "about"
---

# 是水桶啊

<style>
    #div1 {
        position: relative;
        width: 450px;
        height: 450px;
        margin: 20px auto 0
    }
    #div1 a {
        position: absolute;
        top: 0px;
        left: 0px;
        font-family: sans-serif;
        color: #eee;
        font-weight: normal;
        text-decoration: none;
        padding: 3px 6px
    }
    #div1 a:hover {
        border: 1px solid #eee;
        background: #9df
    }
    #div1 .C2 { color:rgb(92, 182, 80)}
    #div1 .C1 { color:rgb(104, 200, 255)}
    #div1 .C3 { color: rgb(255, 151, 191)}
    #div1 .C4 { color: rgb(191, 151, 255)}
    p {
        font: 16px Microsoft YaHei;
        text-align: center;
        color: #ba0c0c
    }
    p a {
        font-size: 14px;
        color: #ba0c0c
    }
    p a:hover {
        color: red
    }
</style>
<div id="div1">
    <a class="C1">Cinema4D</a>
    <a class="C1">OctaneRender</a>
    <a class="C1">AfterEffects</a>
    <a class="C1">Blender</a>
    <a class="C1">MarvelousDesigner</a>
    <a class="C1">SubstancePainter</a>
    <a class="C1">MotionGraphic</a>
    <a class="C1">Lighting</a>
    <a class="C1">Compositing</a>
    <a class="C2">蔚蓝档案</a>
    <a class="C2">重返未来1999</a>
    <a class="C2">原神</a>
    <a class="C2">绝区零</a>
    <a class="C2">崩坏3</a>
    <a class="C2">博德之门3</a>
    <a class="C2">京都动画</a>
    <a class="C2">芳文社</a>
    <a class="C2">利兹与青鸟</a>
    <a class="C2">摇曳露营</a>
    <a class="C2">初音未来</a>
    <a class="C2">武林外传</a>
    <a class="C2">库布里克</a>
    <a class="C3">Momentor</a>
    <a class="C3">米哈游</a>
    <a class="C3">浅烘/美式</a>
    <a class="C3">INFP</a>
    <a class="C3">尼采</a>
    <a class="C3">萨特</a>
    <a class="C3">表情包爱好者</a>
    <a class="C3">抽象</a>
    <a class="C3">广州&上海</a>
</div>

<script>
    var radius = 180;
    var dtr = Math.PI / 180;
    var d = 300;
    var mcList = [];
    var active = false;
    var lasta = 1;
    var lastb = 1;
    var distr = true;
    var tspeed = 10;
    var size = 250;
    var mouseX = 0;
    var mouseY = 0;
    var howElliptical = 1;
    var aA = null;
    var oDiv = null;
    window.onload = function () {
        var i = 0;
        var oTag = null;
        oDiv = document.getElementById('div1');
        aA = oDiv.getElementsByTagName('a');
        for (i = 0; i < aA.length; i++) {
            oTag = {};
            oTag.offsetWidth = aA[i].offsetWidth;
            oTag.offsetHeight = aA[i].offsetHeight;
            mcList.push(oTag);
        }
        sineCosine(0, 0, 0);
        positionAll();
        oDiv.onmouseover = function () {
            active = true;
        };
        oDiv.onmouseout = function () {
            active = false;
        };
        oDiv.onmousemove = function (ev) {
            var oEvent = window.event || ev;
            mouseX = oEvent.clientX - (oDiv.offsetLeft + oDiv.offsetWidth / 2);
            mouseY = oEvent.clientY - (oDiv.offsetTop + oDiv.offsetHeight / 2);
            mouseX /= 5;
            mouseY /= 5;
        };
        setInterval(update, 30);
    };
    function update() {
        var a;
        var b;
        if (active) {
            a = (-Math.min(Math.max(-mouseY, -size), size) / radius) * tspeed;
            b = (Math.min(Math.max(-mouseX, -size), size) / radius) * tspeed;
        } else {
            a = lasta * 0.98;
            b = lastb * 0.98;
        }
        lasta = a;
        lastb = b;
        if (Math.abs(a) <= 0.01 && Math.abs(b) <= 0.01) {
            return;
        }
        var c = 0;
        sineCosine(a, b, c);
        for (var j = 0; j < mcList.length; j++) {
            var rx1 = mcList[j].cx;
            var ry1 = mcList[j].cy * ca + mcList[j].cz * (-sa);
            var rz1 = mcList[j].cy * sa + mcList[j].cz * ca;
            var rx2 = rx1 * cb + rz1 * sb;
            var ry2 = ry1;
            var rz2 = rx1 * (-sb) + rz1 * cb;
            var rx3 = rx2 * cc + ry2 * (-sc);
            var ry3 = rx2 * sc + ry2 * cc;
            var rz3 = rz2;
            mcList[j].cx = rx3;
            mcList[j].cy = ry3;
            mcList[j].cz = rz3;
            per = d / (d + rz3);
            mcList[j].x = (howElliptical * rx3 * per) - (howElliptical * 2);
            mcList[j].y = ry3 * per;
            mcList[j].scale = per;
            mcList[j].alpha = per;
            mcList[j].alpha = (mcList[j].alpha - 0.6) * (10 / 6);
        }
        doPosition();
        depthSort();
    };
    function depthSort() {
        var i = 0;
        var aTmp = [];
        for (i = 0; i < aA.length; i++) {
            aTmp.push(aA[i]);
        }
        aTmp.sort(
            function (vItem1, vItem2) {
                if (vItem1.cz > vItem2.cz) {
                    return -1;
                } else if (vItem1.cz < vItem2.cz) {
                    return 1;
                } else {
                    return 0;
                }
            }
        );
        for (i = 0; i < aTmp.length; i++) {
            aTmp[i].style.zIndex = i;
        }
    };
    function positionAll() {
        var phi = 0;
        var theta = 0;
        var max = mcList.length;
        var i = 0;
        var aTmp = [];
        var oFragment = document.createDocumentFragment();
        for (i = 0; i < aA.length; i++) {
            aTmp.push(aA[i]);
        }
        aTmp.sort(
            function () {
                return Math.random() < 0.5 ? 1 : -1;
            }
        );
        for (i = 0; i < aTmp.length; i++) {
            oFragment.appendChild(aTmp[i]);
        }
        oDiv.appendChild(oFragment);
        for (var i = 1; i < max + 1; i++) {
            if (distr) {
                phi = Math.acos(-1 + (2 * i - 1) / max);
                theta = Math.sqrt(max * Math.PI) * phi;
            } else {
                phi = Math.random() * (Math.PI);
                theta = Math.random() * (2 * Math.PI);
            }
            mcList[i - 1].cx = radius * Math.cos(theta) * Math.sin(phi);
            mcList[i - 1].cy = radius * Math.sin(theta) * Math.sin(phi);
            mcList[i - 1].cz = radius * Math.cos(phi);
            aA[i - 1].style.left = mcList[i - 1].cx + oDiv.offsetWidth / 2 - mcList[i - 1].offsetWidth / 2 + 'px';
            aA[i - 1].style.top = mcList[i - 1].cy + oDiv.offsetHeight / 2 - mcList[i - 1].offsetHeight / 2 + 'px';
        }
    };
    function doPosition() {
        var l = oDiv.offsetWidth / 2;
        var t = oDiv.offsetHeight / 2;
        for (var i = 0; i < mcList.length; i++) {
            aA[i].style.left = mcList[i].cx + l - mcList[i].offsetWidth / 2 + 'px';
            aA[i].style.top = mcList[i].cy + t - mcList[i].offsetHeight / 2 + 'px';
            aA[i].style.fontSize = Math.ceil(12 * mcList[i].scale / 2) + 8 + 'px';
            aA[i].style.filter = "alpha(opacity=" + 100 * mcList[i].alpha + ")";
            aA[i].style.opacity = mcList[i].alpha;
        }
    };
    function sineCosine(a, b, c) {
        sa = Math.sin(a * dtr);
        ca = Math.cos(a * dtr);
        sb = Math.sin(b * dtr);
        cb = Math.cos(b * dtr);
        sc = Math.sin(c * dtr);
        cc = Math.cos(c * dtr);
    }
</script>

# Showreel
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1755319273&bvid=BV1g4421X7XP&cid=1571189311&p=1&autoplay=0" width="100%" height="500vh" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[头像原作](https://www.pixiv.net/artworks/112044290)
[联系我](/assets/blog/about/QQ_QRCode.jpg)