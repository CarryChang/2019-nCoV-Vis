
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)


###  [2019-nCoV-Vis](http://carrychang.top)

#### 基于网络大数据针对于2019-nCoV的数据可视化预测项目， 底层完全使用ElasticSearch-5.6集群进行数据存储，利用前中后台的配合完成新型冠状病毒的疫情发展时间序列可视化项目，方便观察疫情发展情况，加入回归模型对疫情进行预测和散点聚类。

>  ubuntu16下支持一键sh部署，flask使用Gunicorn进行部署，使用前后完全分离的开发模式 

## 使用方法

> * [点击查看数据](http://carrychang.top)
#### 代码结构：使用前中后分离的结构，完全使用Python实现，可视化数据来自于丁香园，通过crontab定时即可实现信息的更新 ps:温馨提示，spider定时不宜太快，防止影响丁香园信息的及时发布，感谢。

> 1. spider是数据采集目录，包含数据的采集和数据清洗，清洗后的数据保存在ElasticSearch5.6中（需自行搭建ES）
> 2. Outbreak_BD_server是项目的前中后台代码，包含前端和中台的数据接口和处理接口，以及前端的可视化（使用百度Echart进行可视化）

> 项目架构图

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/sys_structure.png"></div>


> 数据处理流程

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/data_process.png"></div>

> 1. 前端使用Flask+Echarts的组合进行数据的可视化
> 2. 中台结合使用数据接口和机器学习接口的方法，对数据进行清洗计算和结果返回
> 3. 后台使用es和爬虫作为数据存储和采集，使用ES集群保证源数据的接口的高并发和低响e应

#### 后端ES集群信息存储

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/es_data.png"></div>

#### 前端信息展示
> 基于百度LBS的实时定位和周边疫情实时展示

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/reallocation.png"></div>

> 时间序列

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/timeseries.png"></div>


> 感染城市地图

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/map.png"></div>

 
> 感染城市统计图

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/static.png"></div>

 
> 疫情实时信息

<div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/news.png"></div>

 > 疫情实时预测，使用sklearn的回归模型，利用redis进行数据的存储
 
 <div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/lr.png"></div>
 
> 疫情省份聚类
 
 <div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/city_cluster.png"></div>
 
> 疫情城市聚类
 
 <div align=center><img  src="https://github.com/CarryChang/2019-nCoV-Vis/blob/master/vis/province_cluster.png"></div>
 
 