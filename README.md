
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)


###  [2019-nCoV-Vis](http://carrychang.top)
#### 针对于2019-nCoV的数据可视化预测项目， 底层完全使用ElasticSearch-5.6进行数据存储，利用前中后台的配合完成新型冠状病毒的疫情发展时间序列可视化项目，方便观察疫情发展情况，并可以结合回归模型对疫情进行预测。

 
>  ubuntu16下支持一键sh部署，flask使用Gunicorn进行部署

## 使用方法

> 1. [使用地址](http://carrychang.top)
#### 代码结构：使用前中后分离的结构，完全使用Python实现，可视化数据来自于丁香园，通过crontab定时即可实现信息的更新 ps:温馨提示，spider定时不宜太快，防止影响丁香园信息的及时发布，感谢。

> 1. 前端使用flask+echarts的组合进行数据的vis
> 2. 中台结合使用数据接口和机器学习接口的方法，对数据进行清洗计算和结果返回
> 3. 后台使用es和爬虫作为数据存储和采集，保证源数据的接口供给和低响应时间

> 时间序列

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/timeseries.png"></div>


> 感染城市地图

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/map.png"></div>

 
> 感染城市统计图

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/static.png"></div>

 
> 疫情实时信息

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/news.png"></div>

 
 