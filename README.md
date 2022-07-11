# 星地一体化设计仿真验证平台
![仿真平台主页](./guidance/images/平台宣传页.png)

## 第0课-熟悉卫通
### 如何上网
由于公司2022年申请了军工二级&B&M&资质，故拆除了公司原有的AP面板，要求员工通过有线网络上网。
#### 有线网络配置
  + Note：选择**使用下面的IP地址**
  + IP：172.16.67.**（选取50-253之间的数值）
  + Mask：255.255.255.0
  + Gateway: 172.16.67.254
  + DNS：114.114.114.114

#### 无线网络配置（实验室内使用，请勿广泛传播）
  + SSID：仿真平台
  + Password：ABC.123456

#### 完成用户认证
  + URL：http://202.106.0.20/
  + Username：'name'@spacechina.com / 'name'@chinasatcom.com（入职时会告知）
  + Password：使用初始密码登录后自行修改
  + Note
    + 上网认证系统每12小时会要求重新登录一次
    + 登录OA系统无需连接登录
    + [自动联网脚本获取](D:\source_code\FZPT\Backstage\scheduled_task)

#### 科学上网（不建议频繁和长时间使用）
  [请点这里](https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7)

### 了解卫通
#### 登录公司官网，了解公司大致发展情况
  + URL（Homepage）：http://www.chinasatcom.com/
  + URL（Satellites）：http://www.chinasatcom.com/n782704/n3412226/index.html
  + URL（Leaders，看见本人记得称职务）：http://www.chinasatcom.com/n782699/n782749/index.html
  + 公司简介
    + **中国卫通集团股份有限公司（简称：中国卫通）是中国航天科技集团有限公司从事卫星运营服务业的核心专业子公司，具有国家基础电信业务经营许可证和增值电信业务经营许可证，是我国唯一拥有通信卫星资源且自主可控的卫星通信运营企业，被列为国家一类应急通信专业保障队伍**。2019年6月28日，中国卫通成功登陆上交所主板挂牌交易，**股票代码：601698**。<br/>
    + 中国卫通运营管理着**15颗**优质的在轨民商用通信广播卫星，覆盖中国全境、澳大利亚、东南亚、南亚、中东以及欧洲、非洲等地区。公司拥有完善的基础设施、可靠的测控系统、优秀的专业化团队、卓越的系统集成和7X24小时全天候高品质服务能力，为广大民众提供安全稳定的广播电视信号传输，为国家政府部门和重要行业客户提供专属服务，为重大活动和抢险救灾等突发事件提供及时可靠的通信保障，赢得了广大客户的好评和高度信赖，树立了良好信誉和品牌形象。<br/> 
    + 中国卫通秉承“以国为重、以人为本、以质取信、以新图强”的核心价值观，充分发挥卫星运营国家队的主导作用，坚持**“业务平台化、平台市场化”**的发展思路，以深化改革和技术创新为双轮驱动,统筹推进**“星频站网端”**基础能力建设、**“1+3+N+1”**平台系统建设，加快构建卫星运营服务、行业系统集成、综合信息服务**三大主业**协同发展格局，努力打造成为卫星通信现代产业链链长，促进卫星通信原创技术策源地建设和卫星通信产业数字化转型，为航天强国、网络强国建设作出新的更大贡献！<br/>

#### 基本概念介绍
  + 1+3+N+1平台体系
    + “1”：[星地一体化设计仿真验证平台](http://172.16.67.32:8095/)
    + "3"：[大波束综合服务平台](https://www.mychinasat.com/#/home)、[电信级宽带卫星基础运营平台](https://www.satzone.com/#/index)、多星统一测控平台（无访问链接）
    + "N"：[“海星通”海洋综合应用服务平台](http://gnms.sinosat.com.cn:6868/Default.aspx?Parameter=+cm9262GfAppaP16fdXfsyIP663wn0Uz4Roc3C8fJKmYeq2Rk3Verja8n0a0dRo3)、[机载综合信息服务平台](http://ground.aerosatlink.com/login/#/login)
    + "1"：管理信息化平台（建设中）
  + 三大主业
    + （一）卫星运营服务：转发器出租、网络传输、网络运维服务、卫星测控服务，面向行业：广电、JD等
    + （二）行业系统集成：应急救灾、泛在物联，面向行业：林草、救灾等
    + （三）综合信息服务：机载通信、船载通信、应急通信、普遍服务、泛在物联、咨询服务、培训服务、运营维护服务，面向行业：各类行业
  + 中国卫通微课堂
    + [微课堂01：《中国卫通带您看卫星》系列微课堂开播](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650574776&idx=1&sn=63184fae64266036c13fbefb3f651754&chksm=877c7de1b00bf4f7c54eaf407ca009dcefdf9b142c369eec938320a84e3f4bdbc3f576bed468&scene=21#wechat_redirect)
    + [微课堂02：通信卫星与广播电视不得不说的关系](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650574825&idx=1&sn=dc56a5d09031b442bd13e99d4b8e5945&chksm=877c7db0b00bf4a66a21775a0eb7e1862a6a91ab76b2111514129db14a00b685c4604e69d9d4&scene=21#wechat_redirect)
    + [微课堂03：走进海上无忧的真相](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650574851&idx=1&sn=71c413b9a957f88fa038feb61b89a57d&chksm=877c625ab00beb4c31d11670f3d52ebcc94898bdbfd29a9621515894eef83bc0fab15fbf6b5d&scene=21#wechat_redirect)
    + [微课堂04：谁是应急通信的MVP](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650574889&idx=1&sn=0e275ae3bff1d987ced6809af9377a12&chksm=877c6270b00beb66b5545a6e62f5f833fbe50d5f3d8dce27b7f7dd12e7c552f55eb93f40415e&scene=21#wechat_redirect)
    + [微课堂05：乡音无改 初心不忘 八旬总师闵士权再叙50年前的那颗星](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650574950&idx=1&sn=bbe42b13478da60bab3f4f5e07b41b15&chksm=877c623fb00beb29856b033b3ce83360e2b857e4b0727adff4ac3e266f34eef335f4840463ae&scene=21#wechat_redirect)
    + [微课堂06：卫星通信，让教育无处不在](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650575023&idx=1&sn=f0cfbd45c97cb5f0c87217b88295e8a9&chksm=877c62f6b00bebe01175a57f323569c20a57247c3d115a0810aa60ace9f4ec30f6863d73407f&scene=21#wechat_redirect)
    + [微课堂07：听“牧星人”讲述全国“两会”安播背后的故事](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650575237&idx=1&sn=148051d6d95b4021147ffea617b0de4e&chksm=877c63dcb00beacadb44de26b2ee3351c866b83b04d72698f5d1f4bb8036e47c36cf25412d27&scene=21#wechat_redirect)
    + [微课堂08：想了解新基建和卫星互联网，赶紧戳视频学习](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650575671&idx=1&sn=e569136acb3ccdc31634ec988052b316&chksm=877c616eb00be87898404da5987d340b716bf3e3be9861311e1e3e968e4c3e4ca3fbfddd9d81&scene=21#wechat_redirect)
    + [微课堂09：航空黑科技，中国首架高速卫星互联网飞机](http://mp.weixin.qq.com/s?__biz=MzA3NTE4ODAyMg==&mid=2650575930&idx=1&sn=ae1a5c7844bb9fb91d31498a11cf1769&chksm=877c6663b00bef759c91b6bfc1ce441248914c2bbaa4f366ec1b45218c64d6e39a822919c983&scene=21#wechat_redirect)
    + [微课堂10：再见第一季，相约第二季！](https://mp.weixin.qq.com/s/PFSLSY6SA6RZJGY5OkEfYA)
  + 中国卫通小剧场
    + [中国卫通小剧场01：“海星通”茶话会](https://mp.weixin.qq.com/s/0-4uAN3uN8j071uBQJQhwQ)
    + [中国卫通小剧场02：空中星缘](https://mp.weixin.qq.com/s/3zlSEXtoXT9xyZAP2xPzkA)
  + 了解更多卫星通信相关知识
    + [APSTAR-新一代高通量卫星宣传片](https://www.apstar.com/cn/apstar-video/apstar-hts/)
    + [APSTAR-亚太卫星HTS高通量卫星系列介绍](https://www.apstar.com/cn/apstar-video/%e4%ba%9e%e5%a4%aa%e8%a1%9b%e6%98%9fhts%e9%ab%98%e9%80%9a%e9%87%8f%e8%a1%9b%e6%98%9f%e7%b3%bb%e5%88%97%e4%bb%8b%e7%b4%b9/)
    + [APSTAR-5G对卫星的干扰和解决方案](https://www.apstar.com/cn/apstar-video/5g%e5%b0%8d%e8%a1%9b%e6%98%9f%e7%9a%84%e5%b9%b2%e6%93%be%e5%92%8c%e8%a7%a3%e6%b1%ba%e6%96%b9%e6%a1%88/)
    + [APSTAR-天线极化调整教学](https://www.apstar.com/cn/apstar-video/plan-to-adjust-teaching/)
    + [APSTAR-卫星通信随时随地就在你身边](https://www.apstar.com/cn/apstar-video/satellite-close-to-you/)
    + [APSTAR-卫星的诞生](https://www.apstar.com/cn/apstar-video/birth-of-satellite/)
    
## 第1课-熟悉并构建研发环境
### 个人开发环境构建
#### **Python**环境构建
1. 安装Python（Anaconda Python与原生Python*二选一*即可）
   + **推荐使用Anaconda + Python 3.6环境**
   + 方案1：安装[Anaconda](https://www.anaconda.com/products/distribution)
     + [各版本Anaconda下载](https://repo.anaconda.com/archive/)
     + [Anaconda的安装及环境配置（超详细）](https://blog.csdn.net/weixin_45552475/article/details/124324671)
   + 方案2：安装[原生Python](https://www.python.org/)
2. 安装IDE或编辑器
   + 推荐使用**Pycharm专业版**
   + 方案1：安装[Pycharm](https://www.jetbrains.com/pycharm/)
     + [Pycharm学生用户免费激活](https://blog.csdn.net/puppyoo/article/details/120888438)
     + [Pycharm环境配置](https://blog.csdn.net/m0_65100075/article/details/125080083)
   + 方案2：安装[Visual Studio Code](https://code.visualstudio.com/)
     + [【超好用】Visual Studio Code 配置Python环境](https://blog.csdn.net/qq_46092061/article/details/122438823)
3. 开启IDE，完成环境配置并运行

#### **JAVA**开发环境构建
1. 安装[JRE和JDK](https://www.oracle.com/java/technologies/downloads/#java8)
2. 安装[IntelliJ IDEA](https://www.jetbrains.com/idea/)
   + [IDEA创建学生账号](https://blog.csdn.net/hhh_ainihxh/article/details/80507179) 
3. 开启IDE，完成环境配置并运行

#### **VUE**开发环境构建
1. 安装[Node.js](http://nodejs.cn/download/)
2. 设置全局依赖包存放路径和缓存文件路径
   + 设置缓存文件路径：`npm config set cache "D:\'installPath'\nodejs\node_cache"`
   + 全局依赖包存放路径：`npm config set prefix "D:\'installPath'\nodejs\node_global"`
3. 安装cnpm（淘宝镜像）
   `npm install -g cnpm --registry=https://registry.npm.taobao.org`
4. 安装**VUE**
   `cnpm install vue -g`
5. 安装**VUE-CLI**脚手架
   + 安装3.0以下版本：`cnpm install vue-cli -g`
   + 安装3.0以上版本：`cnpm install -g @vue/cli`
   + [调整VUE版本](https://blog.csdn.net/weixin_43279985/article/details/104841143)
6. 使用**VUE-CLI**创建项目
   + 3.0以下版本vue-cli创建项目：`vue init webpack projectName`
   + 3.0以上版本vue-cli创建项目：`vue create projectName`
   + [如何创建VUE项目](https://www.cnblogs.com/plBlog/p/13968242.html)
   + [VITE安装及创建项目](https://blog.csdn.net/bakelFF/article/details/124672187)

### 协同开发环境构建
请参照[研发环境构建指北](./guidance/services.md)完成代码管理和文件管理环境构建。
