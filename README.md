# PythonSpider
【练习】python爬虫



### 练习记录

1. doubanTop250
   * 通过设置USER_AGENT，伪装成浏览器访问，绕过站点反爬机制
   * //div[@class="info"]：表示 **所有节点下** class 是 'info' 的 div 节点
   * div[@class="hd"]：表示 **某个节点下** class 是 'hd' 的 div 节点
   * 运行爬虫使用 `scrapy crawl doubanTop250`，doubanTop250代表爬虫的名称，是spiders/doubanTop250.py中类`class doubanTop250(CrawlSpider):`中的`name`的名称
2. daomubiji+mongodb
   * mongodb是一个非关系型数据库，在scrapy中的体现是：items代表一个数据模型，所有的字段都直接放在模型下，同一个模型（document）中字段之间无父子关系

     需求：通过点击列表（一级页面）进入详情页（二级页面）

     设计1：只使用一个document，列表页中包含详情页内容。当点击列表时，将详情页的内容直接传递下去

     设计2：使用两个document，列表页中并不包含详情页内容。当点击列表时，通过列表中的信息（某个key），去详情页的document检索相关内容

   * 关联一级目录和二级目录爬取的内容：在scrapy爬虫中，当使用yield返回item时，表示一个完整的数据模型爬取完成。如果想要根据一级页面的信息爬取二级页面的内容，并将一级页面和二级页面的内容关联到数据模型中，我们的处理是：在一级页面某个数据模型爬取完成时，并不直接返回item，而是使用Request函数关联到另一个函数`parseContent`去爬取二级页面的内容，当`parseContent`中的内容爬取完成后，赋值到item并使用yield返回item，本次完整的数据模型才算爬取完成

   * 将内容存入mongodb：在`settings.py`中设置好MONGODB和开启`ITEM_PIPELINES`，在`pipelines.py`中链接mongodb并编写好插入语句