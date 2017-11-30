<div id="main" class=""> <div class="entry-banner">       </div>  <div class="entry-box wrap "> <div class="boxwrap cl "> <div class="boxinner-l" id="baike-content"><div class="entry-header">  <div class="doc-tag-zone"> <div class="essence-tag "></div> </div>  <div id="baikecard" data-sub="#6952601-7175002-0"> <a name="6952601-7175002-0"></a> <div id="baike-title"> <h1> <span class="title">k近邻算法</span> <span id="edit_op" class="opt js-edittext"> <a href="/create/edit/?eid=6952601&amp;sid=7175002" id="J-entry-edit" class="edit edit-btn"><i class="ico"></i>免费编辑</a> </span> <span class="opt"> <a href="javascript:;" id="J-entry-sense" class="J-entry-sense"><i class="ico"></i>添加义项名</a> </span> </h1> <div class="add-multiple-box"> <div id="addMultiplebox" class="addMultiplep"> <a href="###" class="btn-add-mulitiple" id="J-addItemName"><span class="icofont col1">B</span>&nbsp;添加义项</a> <div class="addMultipletips"> <span class="icofont">?</span> <div class="tipscon"><span class="arrow"></span><span class="arrow arrow1"></span> 义项指多义词的不同概念，如<a href="/doc/992653.html" target="_blank">李娜</a>的义项：网球运动员、歌手等；<a href="/doc/1147990.html" target="_blank">非诚勿扰</a>的义项：冯小刚执导电影、江苏卫视交友节目等。 <a href="/doc/7478654.html" target="_blank">查看详细规范&gt;&gt;</a> </div> </div> </div> </div> </div><div class="entry-classify " id="entry-classify"> <div class="entry-classify-hd"> <div class="entry-classify-down js-classify-list"> <span class="name">所属类别 : </span> <div class="classify-txt js-classify-txt short"> 其他数学相关 </div> </div> <div class="entry-classify-up js-classify-total"> 其他数学相关 </div> </div> <div class="entry-classify-bd"> <a class="entry-classify-edit" data-multipicker="0" href="javascript:;"><span class="icon"></span>编辑分类</a> </div> </div><script id="g-classify-list-tmpl" type="text/x-jquery-tmpl"><div>
	<div class="g-classify-total">
		{{each(key, item) list[0]}}
		<div class="total-item {{if item.name==$data.cur_classify[0]}}active{{/if}}" data-picker="${item.id}">${item.name}</div>
		{{/each}}
	</div>
	<div class="g-classify-rel">
		<div class="g-classify-list {{if list.length>5}}more{{/if}}" {{if list.length > 1}}style="width: ${(list.length-1)*160}px;"{{/if}}>
			{{if list.length > 1}}
                {{each(key, item) list}}
                {{if key>0}}
                <div class="g-classify-item">
                    {{each(_key, _item) item}}
                    <div class="classify-item {{if _item.is_leaf}}leaf{{/if}} {{if _item.is_selected}}active{{/if}}" data-picker="${_item.id}">
                        <div class="classify-item-hd">${_item.name}</div>
                        <div class="classify-item-bd">
                            <span class="icon"></span>
                        </div>
                    </div>
                    {{/each}}
                </div>
                {{/if}}
                {{/each}}
            {{else}}
            	{{if $data.cur_classify[0] != '其他'}}
                <span class="g-classify-none">
                    <em></em>点选左侧选项，添加新的分类
                </span>
                {{/if}}
            {{/if}}
		</div>
	</div>
</div></script><script id="g-classify-tmpl" type="text/x-jquery-tmpl"><div>
	<div class="g-classify" id="g-classify">
		<div class="g-classify-hd">
			<div class="g-classify-cur">词条名称：${ename}{{if sname}}（${sname}）{{/if}}
			<div class="g-classify-add js-classify-add">
				<span class="add-icon">+</span><span >添加分类</span>
			</div>
			</div>
			<div class="g-classify-state js-classify-state">
				<div class="g-classify-state-left">
					<span>可编辑分类：</span>
					<span class="editable-text">审核中分类：</span>
				</div>
				<div class="g-classify-state-right">
					<ul class="g-classify-editable js-editable" style="{{if editable.length != 0 }}width:${$item.getWidth($data.editable, -10)}px;{{/if}}">
						{{if editable.length != 0 }}
							{{each(key, item) editable}}
								<li class="{{if key == 0}}on{{/if}}{{if key == editable.length -1}} last{{/if}}"  data-type_id="${item.type_id}" data-rid="${item.id}">${item.name}</li>
							{{/each}}
						{{else}}
							<li class="none-data">暂无</li>
						{{/if}}
					</ul>
					<ul class="g-classify-audit js-audit" style="{{if audit.length != 0 }}width:${$item.getWidth($data.audit, -10)}px;{{/if}}">
						<li class="g-classify-add js-classify-add {{if editable.length == 0 && audit.length == 0}}on{{/if}}" style="display: none;">+</li>
						{{if audit.length != 0 }}
							{{each(key, item) audit}}
								<li class="{{if editable.length == 0 && key == 0}}on{{/if}}{{if key == audit.length -1}} last{{/if}}" data-type_id="${item.type_id}" data-audit="1"  data-rid="${item.id}">${item.name}</li>
							{{/each}}
						{{else}}
							<li class="none-data">暂无</li>
						{{/if}}
					</ul>
				</div>
			</div>
			<div class="g-classify-new">
				<div class="g-classify-new-text"> 分类路径：${$item.classify($data.cur_classify)} </div>
				<input type="text" class="g-classify-suggest" id="g-classify-suggest">
				<span class="g-classify-search js-classify-search"></span>
				<div id="g-classify-suggest-container">
					<div class="g-classify-suggest-bd">
						<div id="g-classify-suggest-common" data-box="suggest-box">
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="g-classify-bd">
		</div>
		<div class="g-classify-ft">
			<div class="g-classify-tips" style="display: none;">
				<div class="tips-hd">
					<span class="icon"></span>
				</div>
				<div class="tips-bd"></div>
			</div>
		</div>
	</div>
</div></script>   <div class="card_content" id="js-card-content"><p>K最近邻(k-Nearest Neighbor，KNN)分类算法，是一个理论上比较成熟的方法，也是最简单的机器学习算法之一。该方法的思路是:如果一个样本在特征空间中的k个最相似(即特征空间中最邻近)的样本中的大多数属于某一个类别，则该样本也属于这个类别。</p></div> <div class="intro_button"></div> </div> <div class="starVideo starVideo1" id="starVideo"> </div>         </div>  <div class="entry-stream-switch" id="entry-stream-switch"> <div class="stream-switch-wrap" style="margin-top: 25px;"> <div class="switch-tag switch-word js-stream-switch active" data-switch="js-switch-word" data-module="entry-detail"> <span class="switch-tag-text">词条</span> </div> <div class="switch-tag switch-plus js-stream-switch" data-switch="js-switch-plus" data-module="entry-stream"> <span class="switch-tag-text">百科</span> <i class="tag-icon"></i> <div class="stream-update-tip js-stream-tips"> <i class="before-part"></i> 点击这里刷新内容 <i class="after-part"></i> </div> <div class="stream-function-tip js-stream-tips active"> <span class="function-tip-text"> 精彩信息一览无遗 </span> </div> </div> <i class="stream-switch-bar js-stream-bar"></i> </div> </div> <div class="entry-stream"></div> <div class="entry-stream-more js-stream-more"> <a href="javascript:;" data-log="info-stream-more"> <span>查看更多</span> <i class="icon"></i> </a> </div> <div class="entry-stream-error js-stream-error"> <a href="javascript:;" data-log="info-stream-error"> <span>网络错误，请点击重试</span> </a> </div><script type="text/x-jquery-tmpl" id="entry-stream-tmpl"><div class="stream-item js-stream-item">
		{{if imgMode == 'p' && imgList.length > 0}}
		<div class="title-wrap stream-img-album">
			<a href="${newsUrl}" target="_blank" data-log="info-stream-item">
				<h2 class="stream-item-title">${title}</h2>
			</a>	
		</div>	
		<div class="img-wrap stream-img-album">
			{{each(i, e) imgList}}
			<div class="stream-item-img">
				<a href="${newsUrl}" target="_blank" data-log="info-stream-item">
					<img src="${e}" onerror="this.src='https://p1.ssl.qhmsg.com/t01f7ccd5fd7d47e81c.png'" />
				</a>
			</div>
			{{/each}}
		</div>	
		<div class="mark-wrap stream-img-album">
			<div class="stream-item-mark">
				<span class="item-mark_1">${siteName}</span>
				<span class="item-mark_2">${time}</span>
			</div>	
		</div>			
		{{else}}
			{{if imgList.length > 0}}
			<div class="img-wrap">
				<div class="stream-item-img">
					<a href="${newsUrl}" target="_blank" data-log="info-stream-item">
						<img src="${imgList[0]}" onerror="this.src='https://p1.ssl.qhmsg.com/t01f7ccd5fd7d47e81c.png'" />
					</a>
				</div>
			</div>	
			{{/if}}	
		<div class="stream-item-details">
			<a href="${newsUrl}" target="_blank" data-log="info-stream-item">
				<h2 class="stream-item-title">${title}</h2>
			</a>
			<div class="stream-item-content">${content}</div>
			<div class="stream-item-mark">
				<span class="item-mark_1">${siteName}</span>
				<span class="item-mark_2">${time}</span>
			</div>
		</div>
		{{/if}}
	</div></script><script type="text/x-jquery-tmpl" id="entry-stream-popup-tmpl"><div class="stream-popup js-stream-popup">
		{{if imgList.length != 0}}
		<div class="stream-popup-img js-stream-popup-open">
			<a>
				<img src="${imgList[0]}" onerror="this.src='https://p1.ssl.qhmsg.com/t01f7ccd5fd7d47e81c.png'">
			</a>
		</div>
		{{/if}}
		<div class="stream-popup-details">
			<a>
				<h2 class="stream-popup-title js-stream-popup-open">${title}</h2>
			</a>
			<div class="stream-popup-mark">
				<span class="js-stream-popup-close">忽略</span>
			</div>
		</div>
	</div></script> <div class="entry-detail"> <div class="entry-basic"> <div id="basic-info"> <a name="uni_baseinfo"></a> <h2 class="titleH2"><span class="h2mark"></span>基本信息</h2> <div class="card-list-box"> <ul class="cardlist"> <li> <div class="cardlist-con"> <p class="cardlist-name" title="中文名称">中文名称</p> <p class="cardlist-value" title="k近邻算法">k近邻算法</p> </div> </li> <li> <div class="cardlist-con"> <p class="cardlist-name" title="外文名称">外文名称</p> <p class="cardlist-value" title="k-Nearest Neighbour，KNN">k-Nearest Neighbour，KNN</p> </div> </li> </ul> <ul class="cardlist"> <li> <div class="cardlist-con"> <p class="cardlist-name" title="地位">地位</p> <p class="cardlist-value" title=" 最简单的机器学习算法之一 "> 最简单的机器学习算法之一 </p> </div> </li> <li> <div class="cardlist-con"> <p class="cardlist-name" title="不足">不足</p> <p class="cardlist-value" title=" 计算量较大 "> 计算量较大 </p> </div> </li> </ul> </div> </div> </div><div class="entry-before">         </div> <div class="entry-catalogue"> <div class="entry-mod-catalogue"> <div class="catalogModWrap"> <span class="h2mark"></span> <table class="catalogMod" id="J-ext-mod-topcatalog"> <tbody><tr> <th><span><em></em>目录</span></th> <td class="listTd"> <div><em>1</em><a title="概念介绍" href="#6952601-7175002-1">概念介绍</a></div> </td><td class="listTd"> <div><em>2</em><a title="案例介绍" href="#6952601-7175002-2">案例介绍</a></div> </td> </tr> </tbody></table> </div> </div> </div><div class="entry-body"> </div> <div class="entry-content"> <div id="lemma-main" class="lemma-meaning" data-sub="#6952601-7175002-0"> <div class="main_content_text cl" id="main-content-text">     <h2> <a name="6952601-7175002-1"></a> <a class="conArrow" href="#" data-logid="h2-title">折叠</a>  <span class="opt js-edittext"> <a class="edit" href="/create/edit/?eid=6952601&amp;sid=7175002&amp;secid=1" data-log="edit-title"><i class="ico"></i>编辑本段</a></span>  <b class="title">概念介绍</b></h2> <div class="sonConBox ">  <div class="h2_content"> <p>用官方的话来说，所谓K近邻算法，即是给定一个训练数据集，对新的输入实例，在训练数据集中找到与该实例最邻近的K个实例(也就是上面所说的K个邻居)， 这K个实例的多数属于某个类，就把该输入实例分类到这个类中。根据这个说法，咱们来看下引自维基百科上的一幅图:</p> </div>   </div>    <h2> <a name="6952601-7175002-2"></a> <a class="conArrow" href="#" data-logid="h2-title">折叠</a>  <span class="opt js-edittext"> <a class="edit" href="/create/edit/?eid=6952601&amp;sid=7175002&amp;secid=2" data-log="edit-title"><i class="ico"></i>编辑本段</a></span>  <b class="title">案例介绍</b></h2> <div class="sonConBox ">  <div class="h2_content"> <p>如右图所示，有两类不同的样本数据，分别用蓝色的小正方形和红色的小三角形表示，而图正中间的那个绿色的圆所标示的数据则是待分类的数据。也就是说，现在， 我们不知道中间那个绿色的数据是从属于哪一类(蓝色小正方形or红色小三角形)，下面，我们就要解决这个问题:给这个绿色的圆分类。</p><p>我们常说，物以类聚，人以群分，判别一个人是一个什么样品质特征的人，常常可以从他/她身边的朋友入手，所谓观其友，而识其人。我们不是要判别上图中那个绿色的圆是属于哪一类数据么，好说，从它的邻居下手。但一次性看多少个邻居呢?从上图中，你还能看到:</p><p><a href="https://p1.ssl.qhmsg.com/t01e09e95cfb2b04523.png" class="show-img layoutright" data-type="gallery" data-index="1"><span class="show-img-hd" style="width:220px;height:198px;"><img id="img_13958888" data-img="mod_img" style="width: 220px; height: 198px; display: inline;" src="https://p1.ssl.qhmsg.com/dr/220__/t01e09e95cfb2b04523.png"></span><span class="show-img-bd"></span></a></p><ul><li>如果K=3，绿色圆点的最近的3个邻居是2个红色小三角形和1个蓝色小正方形，少数从属于多数，基于统计的方法，判定绿色的这个待分类点属于红色的三角形一类。</li><li>如果K=5，绿色圆点的最近的5个邻居是2个红色三角形和3个蓝色的正方形，还是少数从属于多数，基于统计的方法，判定绿色的这个待分类点属于蓝色的正方形一类。</li></ul><p>于此我们看到，当无法判定当前待分类点是从属于已知分类中的哪一类时，我们可以依据统计学的理论看它所处的位置特征，衡量它周围邻居的权重，而把它归为(或分配)到权重更大的那一类。这就是K近邻算法的核心思想。</p><p>KNN算法中，所选择的邻居都是已经正确分类的对象。该方法在定类决策上只依据最邻近的一个或者几个样本的类别来决定待分样本所属的类别。</p><p>KNN 算法本身简单有效，它是一种 lazy-learning 算法，分类器不需要使用训练集进行训练，训练时间复杂度为0。KNN 分类的计算复杂度和训练集中的文档数目成正比，也就是说，如果训练集中文档总数为 n，那么 KNN 的分类时间复杂度为O(n)。</p><p>KNN方法虽然从原理上也依赖于极限定理，但在类别决策时，只与极少量的相邻样本有关。由于KNN方法主要靠周围有限的邻近的样本，而不是靠判别类域的方法来确定所属类别的，因此对于类域的交叉或重叠较多的待分样本集来说，KNN方法较其他方法更为适合。</p><p>K 近邻算法使用的模型实际上对应于对特征空间的划分。K 值的选择，距离度量和分类决策规则是该算法的三个基本要素:</p><ol><li>K 值的选择会对算法的结果产生重大影响。K值较小意味着只有与输入实例较近的训练实例才会对预测结果起作用，但容易发生过拟合;如果 K 值较大，优点是可以减少学习的估计误差，但缺点是学习的近似误差增大，这时与输入实例较远的训练实例也会对预测起作用，使预测发生错误。在实际应用中，K 值一般选择一个较小的数值，通常采用交叉验证的方法来选择最优的 K 值。随着训练实例数目趋向于无穷和 K=1 时，误差率不会超过贝叶斯误差率的2倍，如果K也趋向于无穷，则误差率趋向于贝叶斯误差率。</li><li>该算法中的分类决策规则往往是多数表决，即由输入实例的 K 个最临近的训练实例中的多数类决定输入实例的类别</li><li>距离度量一般采用 Lp 距离，当p=2时，即为欧氏距离，在度量之前，应该将每个属性的值规范化，这样有助于防止具有较大初始值域的属性比具有较小初始值域的属性的权重过大。</li></ol><p>KNN算法不仅可以用于分类，还可以用于回归。通过找出一个样本的k个最近邻居，将这些邻居的属性的平均值赋给该样本，就可以得到该样本的属性。更有用的方法是将不同距离的邻居对该样本产生的影响给予不同的<a href="/doc/6758922-6973527.html" target="_blank">权值</a>(weight)，如权值与距离成反比。 该算法在分类时有个主要的不足是，当样本不平衡时，如一个类的样本容量很大，而其他类样本容量很小时，有可能导致当输入一个新样本时，该样本的K个邻居中大容量类的样本占多数。 该算法只计算"最近的"邻居样本，某一类的样本数量很大，那么或者这类样本并不接近目标样本，或者这类样本很靠近目标样本。无论怎样，数量并不能影响运行结果。可以采用权值的方法(和该样本距离小的邻居权值大)来改进。</p><p>该方法的另一个不足之处是计算量较大，因为对每一个待分类的文本都要计算它到全体已知样本的距离，才能求得它的K个最近邻点。目前常用的解决方法是事先对已知样本点进行剪辑，事先去除对分类作用不大的样本。该算法比较适用于样本容量比较大的类域的自动分类，而那些样本容量较小的类域采用这种算法比较容易产生误分。</p><p>实现 K 近邻算法时，主要考虑的问题是如何对训练数据进行快速 K 近邻搜索，这在特征空间维数大及训练数据容量大时非常必要。</p> </div>   </div>      </div>   </div> </div><div class="entry-after">          <div id="characterRelationship" style="display:none;padding:0 30px"></div> </div> <div class="entry-belong"> <div class="reinforce cl"> </div> </div> </div> </div> <div class="boxinner-r">        
       
       
       
       
<span style="display:none;"></span>
 <div id="card-image"> <div class="img"> <a data-type="gallery" href="https://p1.ssl.qhmsg.com/dr/270_500_/t0177f80f0e71d2ba0d.png" target="_blank" data-index="0"> <img id="js-entry-image" class="pic" width="270" src="https://p1.ssl.qhmsg.com/dr/270_500_/t0177f80f0e71d2ba0d.png?size=268x152" alt="k近邻算法" title=""> </a> </div> <div class="desc"> <a id="entry_search_url" href="http://image.so.com/i?src=360baike_sidepicmore&amp;q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank">k近邻算法</a> </div> <div class="bline1"></div> <div class="bline2"></div> </div>    <div id="weiboshow"></div> <div class="right_high_top"></div> <div class="doc-rightslide" id="js-doc-rightslide" style="position: relative;"><div class="doc-rightslide-inner">         <h2>百科专题<a class="more" href="/zt.html" title="更多" target="_blank">更多</a></h2>         <div class="cont items" id="js-rightslide-wrap">             <ul style="position: absolute; left: -230px; width: 690px; transition-property: none; transition-duration: 500ms; transition-timing-function: ease;">                                  <li class="cont-img" style=""> <a title="扎心了，久坐的危害居然这么大" href="http://baike.so.com/zt/jiuzuoweihai.html?src=dr" target="_blank"><img src="https://p.ssl.qhimg.com/dmtfd/460_308_/t01d0500fa213cdeb30.jpg" alt=""></a> </li>                                  <li class="cont-img"> <a title="小雪来了，这些健康保暖小妙招你知道吗?" href="http://baike.so.com/zt/xiaoxue2017.html?src=dr" target="_blank"><img src="https://p.ssl.qhimg.com/dmtfd/460_308_/t013d6ae14854f1f8c0.jpg" alt=""></a> </li>                                  <li class="cont-img"> <a title="一图了解震惊世界的中国超级计算机" href="http://baike.so.com/zt/chaojijisuanji.html?src=dr" target="_blank"><img src="https://p.ssl.qhimg.com/dmtfd/460_308_/t016e9b3daa677b7001.jpg" alt=""></a> </li>                              </ul>             <!--              <div _tmplitem="3"  class="cont-img" ><a _tmplitem="3"  title="扎心了，久坐的危害居然这么大" href="http://baike.so.com/zt/jiuzuoweihai.html?src=dr" target="_blank"><img _tmplitem="3"  src="https://p.ssl.qhimg.com/dmtfd/460_308_/t01d0500fa213cdeb30.jpg" alt=""></a></div>                          <div _tmplitem="3"  class="cont-img" ><a _tmplitem="3"  title="小雪来了，这些健康保暖小妙招你知道吗?" href="http://baike.so.com/zt/xiaoxue2017.html?src=dr" target="_blank"><img _tmplitem="3"  src="https://p.ssl.qhimg.com/dmtfd/460_308_/t013d6ae14854f1f8c0.jpg" alt=""></a></div>                          <div _tmplitem="3"  class="cont-img" ><a _tmplitem="3"  title="一图了解震惊世界的中国超级计算机" href="http://baike.so.com/zt/chaojijisuanji.html?src=dr" target="_blank"><img _tmplitem="3"  src="https://p.ssl.qhimg.com/dmtfd/460_308_/t016e9b3daa677b7001.jpg" alt=""></a></div>              -->         </div>         <span class="direction prev" id="js-rightslide-left">‹</span>         <div class="menus slide-pagination" id="js-rightslide-items">             <a href="javascript:;" class=""><div></div></a>             <a href="javascript:;" class="active"><div></div></a>             <a href="javascript:;" class=""><div></div></a>         </div>         <span class="direction next" id="js-rightslide-right">›</span>     </div></div>  <div id="J-ext-mod-nlpmodule-2" style="display:none"> <script id="J-ext-mod-nlpmodule-2-tmpl" type="text/x-jquery-tmpl"><div class="rtBox">
            <h2>${recreason}</h2>
        {{each(i, item) list}}
            {{if (i % 3 === 0)}}
            {{if i !== 0}}
            </div>
            {{/if}}
            <div class="imgMod imgtxtMod mg-fix">
            {{/if}}
            <a href="${item.href}" target="_blank" title="${item.title}">
                <div class="inner-img-box"><img src="${item.imgsrc||'https://p1.ssl.qhmsg.com/d/inn/9d534e38/no.png'}" /></div>
                <span>${item.title}</span>
            </a>
        {{/each}}
        {{if list && list.length}}
        </div>
        {{/if}}
        </div></script> </div> <div class="starNote" style="display:none"> <h2>星语星愿</h2> <a class="videoBox" href="javascript:;" id="videoTargetId" style="background:url(https://p1.ssl.qhmsg.com/d/inn/49addde3/ns.jpg) no-repeat 50%"><em class="playBtn"></em></a> </div>  <div class="right_top"><div class="rtBox" id="J-ext-mod-8">         <h2>相关图片</h2>         <div class="h2rt"><a href="http://image.so.com/i?src=360baike_sidepicmore&amp;q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank">更多</a></div>         <div class="imgMod">                                                   <a href="http://image.so.com/v?src=360baike_sidepic&amp;q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95#id=370f8702b4ce22957c7b39a224df3fb8&amp;dataindex=0&amp;lightboxindex=0" target="_blank"><img src="https://p1.ssl.qhimgs1.com/sdmt/70_70_/t011030d09c50ef6291.png" alt=""></a>                                                                    <a href="http://image.so.com/v?src=360baike_sidepic&amp;q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95#id=a37cae2b5de357e638a477f20d1afecb&amp;dataindex=1&amp;lightboxindex=1" target="_blank"><img src="https://p1.ssl.qhimgs1.com/sdmt/70_70_/t01f4111424929b5763.jpg" alt=""></a>                                                                    <a href="http://image.so.com/v?src=360baike_sidepic&amp;q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95#id=5fa3154b506ffe5ba052f6f4ba740905&amp;dataindex=2&amp;lightboxindex=2" target="_blank"><img src="https://p1.ssl.qhimgs1.com/sdmt/70_70_/t015de92d2e61aa65b1.jpg" alt=""></a>                                                                                                                                                                                                                           </div>     </div></div> <div data-sub="#6952601-7175002-0" id="J-mod-stat" class="" style=""><script id="J-mod-stat-template" type="text/x-jquery-tmpl"><div class="rtBox rtEntryInfo">
    <h2>词条信息</h2>
    <p>创建者：<em class="js-usercard" data-index="${entry_author_uid}">${entry_author}</em></p>
    <p>创建时间：<span>${entry_create_time}</span></p>
    {{if entry_update_time}}
    <p>最近更新：<span>${entry_update_time}</span></p>
    {{/if}}
    {{if entry_edit_times}}
    <p>编辑次数：<span>${entry_edit_times}</span></p>
    {{/if}}
    <p class="historyVesion"><a target="_blank" href="/history?eid=${eid}&sid=${sid}">历史版本</a></p>

    {{if contribute_list.elite}}
        <div class="cFix">
            <p>精华贡献者</p>
            {{if contribute_list.elite.author_head}}
            <span class="fl flHd js-usercard" data-index="${contribute_list.elite.uid}"><img src="${contribute_list.elite.author_head}" alt=""/></span>
            {{/if}}
            <div class="overFix">
                <p><em class="js-usercard" data-index="${contribute_list.elite.uid}">${contribute_list.elite.author}</em></p>
                <p><a href="/elite" target="_blank" class="elite lv${contribute_list.elite.elite_level}"></a></p>
            </div>
        </div>
    {{/if}}

    {{if contribute_list.is_show == 1}}
        <p>贡献排名</p>
        <div class="rank">
            {{each(i, v) contribute_list.list}}
                {{if i<3}}
                <p><span>${i+1}</span><em class="js-usercard" data-index="${v.uid}">${v.author}</em></p>
                {{/if}}
            {{/each}}
        </div>
    {{/if}}
</div></script> <div class="rtBox rtEntryInfo">     <h2>词条信息</h2>     <p>创建者：<em class="js-usercard" data-index="357839082">神一样的粟</em></p>     <p>创建时间：<span>2013-08-27</span></p>          <p>最近更新：<span>2017-10-20</span></p>               <p>编辑次数：<span>4</span></p>          <p class="historyVesion"><a target="_blank" href="/history?eid=6952601&amp;sid=7175002">历史版本</a></p>                     <p>贡献排名</p>         <div class="rank">                                               <p><span>1</span><em class="js-usercard" data-index="1902062685">vwkp3084</em></p>                                                                <p><span>2</span><em class="js-usercard" data-index="1902238861">xinwanyuan123</em></p>                                                                <p><span>3</span><em class="js-usercard" data-index="1902134674">wjking2009</em></p>                                                                     </div>      </div></div>   <div class="entry-widget rtBox rtEntryInfo" id="knowledge" style=""> <div class="entry-widget-hd"> <h2>你知道吗</h2> </div> <div class="entry-widget-bd"> <ul id="knowledge-solved"><li><a href="http://wenda.so.com/q/1396109555062389" target="_blank" title="k近邻算法 外文翻译 急"><b>k近邻算法</b> 外文翻译 急</a></li><li><a href="http://wenda.so.com/q/1378383007074299" target="_blank" title="K近邻聚类算法"><b>K近邻</b>聚类<b>算法</b></a></li><li><a href="http://wenda.so.com/q/1459487152723937" target="_blank" title="谁能提供点云数据搜索k近邻的matlab算法">谁能提供点云数据搜索<b>k近邻</b>的matlab<b>算法</b></a></li><li><a href="http://wenda.so.com/q/1366700929063657" target="_blank" title="求k近邻法实例,有的给我发一个,matlab程序。求高手啊!">求<b>k近邻</b>法实例,有的给我发一个,matlab程序。求高手啊!</a></li></ul> <ul id="knowledge-unsolved"><li class="unsolved"><span class="icon">未解决</span><a href="http://wenda.so.com/q/1501908452216256?src=baike_ans" target="_blank" title="K均值与k 近邻算法区别">K均值与<b>k 近邻算法</b>区别</a></li></ul> </div> <div class="entry-widget-ft" id="knowledge-more"><a href="http://wenda.so.com/search/?q=k近邻算法" target="_blank">更多&gt;&gt;</a></div> </div> <div id="J-mod-ranking"><div class="rtBox">   <h2>百科热搜</h2>   <div class="hostso">              <a href="https://baike.so.com/doc/5368019-5603800.html?stat_source=hot" target="_blank" title="英国哈里王子订婚啦!" class="hot-so1">英国哈里王子订婚啦!</a>                   <a href="https://baike.so.com/doc/25717132-26806401.html?stat_source=hot" target="_blank" title="寻梦环游记" class="hot-so2">寻梦环游记</a>                   <a href="https://baike.so.com/doc/3106633-3274453.html?stat_source=hot" target="_blank" title="刘亦菲演真人版花木兰" class="hot-so3">刘亦菲演真人版花木兰</a>                   <a href="https://baike.so.com/doc/6248450-6461860.html?stat_source=hot" target="_blank" title="崔志成辞去北京大兴区区长职务" class="hot-so4">崔志成辞去北京大兴区区长职务</a>                   <a href="https://baike.so.com/doc/5384589-5621002.html?stat_source=hot" target="_blank" title="刘强东上任村长" class="hot-so1">刘强东上任村长</a>                   <a href="https://baike.so.com/doc/27073742-28457408.html?stat_source=hot" target="_blank" title="北京大兴火灾" class="hot-so2">北京大兴火灾</a>                   <a href="https://baike.so.com/doc/27074207-28457939.html?stat_source=hot" target="_blank" title="杀妻藏尸案" class="hot-so3">杀妻藏尸案</a>                   <a href="https://baike.so.com/doc/7487701-7757976.html?stat_source=hot" target="_blank" title="e租宝案二审维持原判:主犯被判无期" class="hot-so4">e租宝案二审维持原判:主犯被判无期</a>                   <a href="https://baike.so.com/doc/5422042-5660233.html?stat_source=hot" target="_blank" title="张阳自杀身亡" class="hot-so1">张阳自杀身亡</a>                   <a href="https://baike.so.com/doc/27073928-28457618.html?stat_source=hot" target="_blank" title="红黄蓝幼儿园虐童事件" class="hot-so2">红黄蓝幼儿园虐童事件</a>            </div>  </div></div><script id="J-mod-ranking-template" type="text/x-jquery-tmpl"><div class="rtBox">
		<h2>百科热搜</h2>
		<div class="hostso">
			{{each(i,v) data}}
				{{if v.aid !== '0' && v.aname.length > 0 }}
				<a href="/doc/${v.eid}.html?from=${v.aid}&redirect=search&stat_source=hot#${v.eid}-${v.sid}-0"
				   target="_blank" title="${v.title}" class="${$item.getClass(i+1)}">{{if v.title}}${v.title}{{else}}${v.ename}{{/if}}</a>
				{{else}}
				<a href="${v.url}?stat_source=hot"
				   target="_blank" title="${v.title}" class="${$item.getClass(i+1)}">{{if v.title}}${v.title}{{else}}${v.ename}{{/if}}</a>
				{{/if}}
			{{/each}}
		</div>
	</div></script> <div class="right_bottom"></div> <div id="J-mod-relate-recommend" class="" style=""><div class="rtBox relate-recommend">  <h2>相关搜索</h2>  <div class="recommend-word">   <ul>               <li>      <i></i><a href="https://www.so.com/s?q=%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A%E7%BD%91&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">学术期刊网</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=matlab%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">matlab编程入门教程</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">中国学术期刊</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A%E7%BD%91&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">中国学术期刊网</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E4%B8%AD%E5%9B%BD%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A%E7%BD%91%E5%AE%98%E7%BD%91&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">中国学术期刊网官网</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E5%AD%A6%E6%9C%AF%E4%B8%8D%E7%AB%AF%E6%96%87%E7%8C%AE%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">学术不端文献检测系统</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E5%AD%A6%E6%9C%AF%E6%9C%9F%E5%88%8A&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">学术期刊</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E5%AD%A6%E6%9C%AF%E8%AE%BA%E6%96%87&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">学术论文</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E5%AD%A6%E6%9C%AF%E8%AE%BA%E6%96%87%E7%BD%91&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">学术论文网</a>     </li>                     <li>      <i></i><a href="https://www.so.com/s?q=%E6%95%99%E8%82%B2%E5%AD%A6%E6%9C%AF%E6%9C%88%E5%88%8A&amp;src=baike_inline_ad" data-logid="s-search-related" target="_blank">教育学术月刊</a>     </li>             </ul>  </div> </div></div><script id="J-mod-relate-recommend-template" type="text/x-jquery-tmpl"><div class="rtBox relate-recommend">
	<h2>相关搜索</h2>
	<div class="recommend-word">
		<ul>
			{{each(i,v) $data.data}}
	        	<li>
					<i></i><a href="https://www.so.com/s?q=${encodeURIComponent(text)}&src=baike_inline_ad" data-logid="s-search-related" target="_blank">${text}</a>
				</li>
	        {{/each}}
		</ul>
	</div>
</div></script> <div id="J-mod-guess-hobby" class="" style=""><div class="rtBox guess-hobby-recommend">  <h2>猜你喜欢</h2>  <div class="guess-hobby-word">   <ul class="mr-16">                      <li>       <i class="red">1.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E5%B9%BF%E5%B7%9E%E8%A3%85%E4%BF%AE%E5%85%AC%E5%8F%B8&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=0&amp;txt=%E5%B9%BF%E5%B7%9E%E8%A3%85%E4%BF%AE%E5%85%AC%E5%8F%B8" data-logid="s-search-utm-ad">广州装修公司</a>      </li>                                  <li>       <i class="red">2.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%B4%97%E7%A2%97%E6%9C%BA&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=1&amp;txt=%E6%B4%97%E7%A2%97%E6%9C%BA" data-logid="s-search-utm-ad">洗碗机</a>      </li>                                  <li>       <i class="red">3.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%89%AB%E5%9C%B0%E6%9C%BA%E5%93%81%E7%89%8C&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=2&amp;txt=%E6%89%AB%E5%9C%B0%E6%9C%BA%E5%93%81%E7%89%8C" data-logid="s-search-utm-ad">扫地机品牌</a>      </li>                            <li>       <i>4.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E7%BD%91%E5%BA%97%E6%80%8E%E4%B9%88%E5%BC%80%E5%95%8A&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=3&amp;txt=%E7%BD%91%E5%BA%97%E6%80%8E%E4%B9%88%E5%BC%80%E5%95%8A" data-logid="s-search-utm-ad">网店怎么开啊</a>      </li>                           <li>       <i>5.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E8%87%AA%E8%80%83%E4%B8%93%E5%8D%87%E6%9C%AC&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=4&amp;txt=%E8%87%AA%E8%80%83%E4%B8%93%E5%8D%87%E6%9C%AC" data-logid="s-search-utm-ad">自考专升本</a>      </li>                           <li>       <i>6.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E8%B1%AA%E5%8D%8E%E6%B8%B8%E8%BD%AE%E6%97%85%E8%A1%8C&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=5&amp;txt=%E8%B1%AA%E5%8D%8E%E6%B8%B8%E8%BD%AE%E6%97%85%E8%A1%8C" data-logid="s-search-utm-ad">豪华游轮旅行</a>      </li>                           <li>       <i>7.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=e%E5%BA%97%E5%AE%9D&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=6&amp;txt=e%E5%BA%97%E5%AE%9D" data-logid="s-search-utm-ad">e店宝</a>      </li>                           <li>       <i>8.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E9%98%BF%E9%87%8C%E4%BA%91&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=7&amp;txt=%E9%98%BF%E9%87%8C%E4%BA%91" data-logid="s-search-utm-ad">阿里云</a>      </li>                           <li>       <i>9.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%89%93%E9%B1%BC%E6%9C%BA&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=8&amp;txt=%E6%89%93%E9%B1%BC%E6%9C%BA" data-logid="s-search-utm-ad">打鱼机</a>      </li>                           <li>       <i>10.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E9%92%BB%E6%88%92&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=9&amp;txt=%E9%92%BB%E6%88%92" data-logid="s-search-utm-ad">钻戒</a>      </li>                           <li>       <i>11.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E8%85%BE%E5%86%B2%E6%97%85%E6%B8%B8&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=10&amp;txt=%E8%85%BE%E5%86%B2%E6%97%85%E6%B8%B8" data-logid="s-search-utm-ad">腾冲旅游</a>      </li>                  </ul>   <ul>               <li>      <i>12.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E9%87%8D%E5%9E%8B%E8%B4%A7%E6%9E%B6&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=11&amp;txt=%E9%87%8D%E5%9E%8B%E8%B4%A7%E6%9E%B6" data-logid="s-search-utm-ad">重型货架</a>     </li>                     <li>      <i>13.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E5%B0%8F%E5%9E%8B%E6%A6%A8%E6%B2%B9%E6%9C%BA&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=12&amp;txt=%E5%B0%8F%E5%9E%8B%E6%A6%A8%E6%B2%B9%E6%9C%BA" data-logid="s-search-utm-ad">小型榨油机</a>     </li>                     <li>      <i>14.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=skf&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=13&amp;txt=skf" data-logid="s-search-utm-ad">skf</a>     </li>                     <li>      <i>15.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E4%BC%9A%E8%AE%A1%E7%BD%91&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=14&amp;txt=%E4%BC%9A%E8%AE%A1%E7%BD%91" data-logid="s-search-utm-ad">会计网</a>     </li>                     <li>      <i>16.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E7%9A%87%E8%8C%B6&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=15&amp;txt=%E7%9A%87%E8%8C%B6" data-logid="s-search-utm-ad">皇茶</a>     </li>                     <li>      <i>17.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%B2%88%E9%98%B3%E6%90%AC%E5%AE%B6%E5%85%AC%E5%8F%B8&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=16&amp;txt=%E6%B2%88%E9%98%B3%E6%90%AC%E5%AE%B6%E5%85%AC%E5%8F%B8" data-logid="s-search-utm-ad">沈阳搬家公司</a>     </li>                     <li>      <i>18.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%B1%9F%E6%B9%96%E7%BD%91%E9%A1%B5%E6%B8%B8%E6%88%8F&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=17&amp;txt=%E6%B1%9F%E6%B9%96%E7%BD%91%E9%A1%B5%E6%B8%B8%E6%88%8F" data-logid="s-search-utm-ad">江湖网页游戏</a>     </li>                     <li>      <i>19.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%BC%A0%E6%B2%B3%E6%97%85%E6%B8%B8%E6%94%BB%E7%95%A5&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=18&amp;txt=%E6%BC%A0%E6%B2%B3%E6%97%85%E6%B8%B8%E6%94%BB%E7%95%A5" data-logid="s-search-utm-ad">漠河旅游攻略</a>     </li>                     <li>      <i>20.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E6%B6%B2%E5%8E%8B%E6%89%B3%E6%89%8B&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=19&amp;txt=%E6%B6%B2%E5%8E%8B%E6%89%B3%E6%89%8B" data-logid="s-search-utm-ad">液压扳手</a>     </li>                     <li>      <i>21.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E5%8A%A0%E6%B9%BF%E5%99%A8&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=20&amp;txt=%E5%8A%A0%E6%B9%BF%E5%99%A8" data-logid="s-search-utm-ad">加湿器</a>     </li>                     <li>      <i>22.</i><a href="http://www.so.com/s?src=lm&amp;ls=s509c46029b&amp;q=%E7%88%B1%E5%A4%9C%E6%AC%A2%E7%BA%A6%E4%BC%9A%E7%BD%91&amp;lmsid=ae2560fc4d1ba703&amp;lm_extend=ctype:4" target="_blank" data-lianmeng="https://stat.lianmeng.360.cn/s2/clk.gif?lm_extend=ctype:4&amp;qid=ae2560fc4d1ba703&amp;nu=22&amp;ls=s509c46029b&amp;ifr=0&amp;ir=0&amp;index=21&amp;txt=%E7%88%B1%E5%A4%9C%E6%AC%A2%E7%BA%A6%E4%BC%9A%E7%BD%91" data-logid="s-search-utm-ad">爱夜欢约会网</a>     </li>             </ul>  </div> </div></div><script id="J-mod-guess-hobby-template" type="text/x-jquery-tmpl"><div class="rtBox guess-hobby-recommend">
	<h2>猜你喜欢</h2>
	<div class="guess-hobby-word">
		<ul class="mr-16">
			{{each(i,v) $data.guess1}}
					{{if i <= 3}}
		        	<li>
						<i class="red">${v.i}.</i><a href="${v.sites[0].url}" target="_blank" data-lianmeng="${v.sites[0].clk}" data-logid="s-search-utm-ad">${v.sites[0].name}</a>
					</li>
					{{else}}
					<li>
						<i>${v.i}.</i><a href="${v.sites[0].url}" target="_blank" data-lianmeng="${v.sites[0].clk}" data-logid="s-search-utm-ad">${v.sites[0].name}</a>
					</li>
				{{/if}}
	        {{/each}}
		</ul>
		<ul>
			{{each(i,v) $data.guess2}}
	        	<li>
					<i>${v.i}.</i><a href="${v.sites[0].url}" target="_blank" data-lianmeng="${v.sites[0].clk}" data-logid="s-search-utm-ad">${v.sites[0].name}</a>
				</li>
	        {{/each}}
		</ul>
	</div>
</div></script>  <div id="rightbanner" class="doc-widget-rightbanner"><div id="J-entry-ad-right"></div>
<span style="display:none;"></span> <script id="J-entry-ad-right-template" type="text/x-jquery-tmpl"><div class="entry-ad-right-container js-ad-right-item">
		{{each(i,v) $data.ads}}
			<a class="js-desc lmitem" href="${v.curl}" target="_blank" data-clktk="${v.clktk}" >
				<img src="${v.img}">
				<span class="item-text">
					<p><span class="title">${v.desc}</span></p>
					<p><span class="gosee">去看看</span></p>
				</span>
			</a>
		{{/each}}
		<span class="ad-text">广告</span>
	</div></script> </div> <a id="js-sidetoolbar-contral" name="sidetoolbar-contral"></a> <div id="side-tool-bar" style="visibility:hidden"> <div id="sideCatalog" class="sideCatalog"> <div class="sidebar"> <div class="sideCatalog-sidebar-top"></div> <div class="sideCatalog-sidebar-bottom"></div></div> <div id="sideCatalog-updown"> <div id="sideCatalog-up" class="sideCatalog-up-disable" title="向上翻页"></div> <div id="sideCatalog-down" class="sideCatalog-down-enable" title="向下翻页"></div></div> <div id="sideCatalog-catalog" class="sideCatalog-catalog mCustomScrollbar _mCS_1"><div class="mCustomScrollBox mCS-dark" id="mCSB_1" style="position:relative; height:100%;max-width:100%;"><div class="mCSB_container mCS_no_scrollbar" style="position:relative; top:0;"> <dl>   <dd class="sideCatalog-item1" data-anchor="6952601-7175002-1">  <span class="index">1</span>  <a href="#6952601-7175002-1" title="概念介绍">概念介绍</a> <span class="dot"></span></dd>     <dd class="sideCatalog-item1" data-anchor="6952601-7175002-2">  <span class="index">2</span>  <a href="#6952601-7175002-2" title="案例介绍">案例介绍</a> <span class="dot"></span></dd>    </dl></div><div class="mCSB_scrollTools" style="position: absolute; display: none;"><div class="mCSB_draggerContainer"><div class="mCSB_dragger" style="position: absolute; top: 0px;" oncontextmenu="return false;"><div class="mCSB_dragger_bar" style="position:relative;"></div></div><div class="mCSB_draggerRail"></div></div></div></div></div></div> <a href="###" class="scrolltop hideText" data-log="back-top">回到顶部</a> <a href="http://info.so.com/feedback_baike.html?type=wordcorrect&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" class="faceicon hideText" data-log="feedback">意见反馈</a> <div class="shareicon" id="shareBtn"></div> <div class="sharearea-wrap" id="shareBox"> <a href="###" data-log="qq"><i class="qzone"></i>QQ空间</a> <a href="###" data-log="sina"><i class="weibo"></i>新浪微博</a> <a href="###" data-log="tencent"><i class="tweibo"></i>腾讯微博</a> <a href="###" data-log="baidu"><i class="tieba"></i>百度贴吧</a> <a href="###" data-log="renren"><i class="renren"></i>人人</a> <a href="###" data-log="douban"><i class="douban"></i>豆瓣</a></div> </div> </div> <div class="boxinner-r-bg"></div> </div> </div>  <div class="entry-footer wrap ">  <div class="mod-recommend" id="js-doc-recommand" style=""><div class="mod-recommend-hd">      <h2><i></i>为您推荐</h2>  </div>     <div class="mod-recommend-bd">                                 <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E5%8E%9F%E7%90%86&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法原理</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95matlab&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法matlab</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E4%BB%A3%E7%A0%81&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法代码</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E5%88%86%E7%B1%BB%E7%AE%97%E6%B3%95&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻分类算法</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%20python&amp;src=baike_inline" data-log="s-search-recommend" class="a-last" target="_blank">k近邻算法 python</a>                                              <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E4%BB%A3%E7%A0%81matlab&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法代码matlab</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E5%AE%9E%E4%BE%8B&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法实例</a>                                           <a href="https://www.so.com/s?q=k%E6%9C%80%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k最近邻算法</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E4%BC%98%E7%BC%BA%E7%82%B9&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法优缺点</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95r%E8%AF%AD%E8%A8%80&amp;src=baike_inline" data-log="s-search-recommend" class="a-last" target="_blank">k近邻算法r语言</a>                                              <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E6%B5%81%E7%A8%8B&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法流程</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E7%9A%84%E5%BA%94%E7%94%A8&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法的应用</a>                                           <a href="https://www.so.com/s?q=java%E4%B8%ADk%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">java中k近邻算法</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E6%B5%81%E7%A8%8B%E5%9B%BE&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法流程图</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%8F&amp;src=baike_inline" data-log="s-search-recommend" class="a-last" target="_blank">k近邻算法公式</a>                                              <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E6%A1%88%E4%BE%8B&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻算法案例</a>                                           <a href="https://www.so.com/s?q=k%E6%9C%80%E8%BF%91%E9%82%BB%E5%88%86%E7%B1%BB%E7%AE%97%E6%B3%95&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k最近邻分类算法</a>                                           <a href="https://www.so.com/s?q=k%E6%9C%80%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95%E4%BE%8B%E5%AD%90&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k最近邻算法例子</a>                                           <a href="https://www.so.com/s?q=k%E8%BF%91%E9%82%BB%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95&amp;src=baike_inline" data-log="s-search-recommend" target="_blank">k近邻搜索算法</a>                        </div></div><script id="js-t-doc-recommend" type="text/x-jquery-tmpl"><div class="mod-recommend-hd">
	    <h2><i></i>为您推荐</h2>
	</div>
    <div class="mod-recommend-bd">
        {{each(i,v) $data.data}}
        	{{if (i+1)%5==0}}
            	<a href="https://www.so.com/s?q=${encodeURIComponent(text)}&src=baike_inline" data-log="s-search-recommend" class="a-last" target="_blank">${text}</a>
           	{{else}}
           		<a href="https://www.so.com/s?q=${encodeURIComponent(text)}&src=baike_inline" data-log="s-search-recommend" target="_blank">${text}</a>
        	{{/if}}
        {{/each}}
    </div></script>  <div id="bnbtm" class="bnbtm ">                                                                                
                                                                             
                                                                             
                                                                             
                                                                             
<div id="J-entry-ad-bottom"></div>
<span style="display:none;"></span> <script id="J-entry-ad-bottom-template" type="text/x-jquery-tmpl"><div class="Js-ad-bottom-container ad-bottom-container">
		<div class="ad-bottom-slide-container">
			<div class="ad-bottom-slide">
				{{each(groupIndex, groupName) $data.groupAds}}
					<div class="ad-slide-item">
						{{each(i,v) groupName}}
							<a class="lmitem" data-clktk="${v.clktk}" href="${v.curl}" target="_blank">
								<img src="${v.img}">
								<span class="item-text">
									<p><span class="title">${v.desc}</span></p>
									<p><span class="gosee">去看看</span></p>
								</span>
							</a>
						{{/each}}
					</div>
				{{/each}}
			</div>
			<span class="ad-text">广告</span>
		</div>
		{{if $data.groupAds.length > 1}}
		<div class="ad-bottom-dot">
			{{each(groupIndex, groupName) $data.groupAds}}
				<a class="{{if groupIndex == 0}} active {{/if}}" href="javascript:void(0);"></a>
			{{/each}}
		</div>	
		{{/if}}
	</div></script>   <div class="cl"></div></div>  


        	     	     	     	     	         	     	     	     	     	         	     	     	     	     	         	     	     	         	     	     	     	     	         	     	     	     	     	 
<div class="wrap">
    <div class="bnbtm-info">
        <div class="bnbtm-info-hd">
           	                        <div class="bnbtm-list">
                            <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>新手入门</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/1128786-1194141.html" target="_blank" data-log="footer-xinshourumen-intro">百科介绍</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://baike.so.com/uc/task" target="_blank" data-log="footer-xinshourumen-newbie">新手任务</a></li>
                                                                                            </ul>
                       <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/5343776-5579219.html" target="_blank" data-log="footer-xinshourumen-edit-rule">编辑规范</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://jifen.so.com/userMall/index" target="_blank" data-log="footer-xinshourumen-mall">礼品兑换</a></li>
                                                                     </ul>
                    </div>
                </div>
                                        <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>高校用户</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/24060587-24645835.html" target="_blank" data-log="footer-gaoxiaoyonghu-intro">团队介绍</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://jifen.so.com/schoolRank" target="_blank" data-log="footer-gaoxiaoyonghu-rank">团队排行</a></li>
                                                                                            </ul>
                       <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/hd/gaoxiao_weixin.html" target="_blank" data-log="footer-gaoxiaoyonghu-envoy">校园大使</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="https://www.wenjuan.com/s/j6Jfy2/?src=bkdbdh" target="_blank" data-log="footer-gaoxiaoyonghu-admit">报名加入</a></li>
                                                                     </ul>
                    </div>
                </div>
                                        <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>意见反馈</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://info.so.com/feedback_baike.html?type=violation&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" data-log="footer-yijianfankui-complaint">我要投诉</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://info.so.com/feedback_baike.html?type=wordcorrect&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" data-log="footer-yijianfankui-correct">我要纠错</a></li>
                                                                                            </ul>
                       <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://info.so.com/feedback_baike.html?type=suggest&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" data-log="footer-yijianfankui-advice">产品建议</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://info.so.com/feedback_baike.html?type=infringement&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" data-log="footer-yijianfankui-feedback">侵权反馈</a></li>
                                                                     </ul>
                    </div>
                </div>
                                    </div>
            <div class="bnbtm-list">
                            <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>答疑解惑</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/robot" target="_blank" data-log="footer-dayijiehuo-robot">小安答疑</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/7922749-8196983.html" target="_blank" data-log="footer-dayijiehuo-audit">审核问题</a></li>
                                                                                            </ul>
                       <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://info.so.com/feedback_baike.html?type=account&amp;eid=6952601&amp;sid=7175002&amp;entryname=k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95" target="_blank" data-log="footer-dayijiehuo-baned-user">账号封禁</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/7520530-7793907.html" target="_blank" data-log="footer-dayijiehuo-company">企业词条</a></li>
                                                                     </ul>
                    </div>
                </div>
                                        <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>大牌百科</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/24211109-24839174.html" target="_blank" data-log="footer-dapaibaike-intro">大牌百科</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="https://www.wenjuan.com/s/yQn2Yb/" target="_blank" data-log="footer-dapaibaike-admit">申请大牌</a></li>
                                                                     </ul>
                    </div>
                </div>
                                        <div class="bnbtm-item">
                    <div class="bnbtm-item-hd">
                        <h3>百科故事</h3>
                    </div>
                    <div class="bnbtm-item-bd">
                                                                     <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/zt/2016user.html" target="_blank" data-log="footer-baikegushi-leader">用户领袖</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://baike.so.com/elite" target="_blank" data-log="footer-baikegushi-elite">百科精英</a></li>
                                                                                            </ul>
                       <ul>
                                                                                            <li class="bnbtm-item-li"><a href="http://baike.so.com/doc/10035219-10383243.html" target="_blank" data-log="footer-baikegushi-event">百科大事</a></li>
                                                                                                                                          <li class="bnbtm-item-li"><a href="http://baike.so.com/zt/2016suiyue.html" target="_blank" data-log="footer-baikegushi-annual-report">年终盘点</a></li>
                                                                     </ul>
                    </div>
                </div>
                        </div>
        </div>
        <div class="bnbtm-info-bd">
            <div class="bnbtm-about">
                <div class="bnbtm-about-hd">
                    <div class="bnbtm-logo"></div>
                </div>
                <div class="bnbtm-about-bd">
                    <p>360百科致力于成为用户所信赖的专业性百科网站。人人可编辑，让求知更简单。</p>
                </div>
                <div class="bnbtm-about-ft">
                    <h3>联系方式</h3>
                            <ul class="bnbtm-about-share">
                                <li data-index="0"><a href="javascript:;"></a><div class="icon"><div class="icon-hd"><img src="https://p1.ssl.qhmsg.com/t015feee359f16ed591.png" alt=""></div><div class="icon-ft"></div></div></li>
                                <li data-index="1"><a href="http://weibo.com/u/5708689067" target="_blank"></a></li>
                                <li data-index="2"><a href="javascript:;"></a><div class="icon"><div class="icon-hd"><img src="https://p1.ssl.qhmsg.com/t01bda8a489492ffd9d.png" alt=""></div><div class="icon-ft"></div></div></li>
                                <li class="last" data-index="3"><a href="mailto://360baike@360.cn" target="_blank"></a></li>
                            </ul>
                </div>
            </div>
        </div>
        <div class="bnbtm-info-ft"></div>
    </div>
</div> </div>  <div class="stream-popup js-stream-popup" style="display: block; right: -460px;">      <div class="stream-popup-img js-stream-popup-open">    <a>     <img src="https://p0.ssl.qhimgs4.com/dmfd/180_100_/t01dc34ddc074a672db.jpg" onerror="this.src='https://p1.ssl.qhmsg.com/t01f7ccd5fd7d47e81c.png'">    </a>   </div>      <div class="stream-popup-details">    <a>     <h2 class="stream-popup-title js-stream-popup-open">机器学习经典算法系列K近邻算法</h2>    </a>    <div class="stream-popup-mark">     <span class="js-stream-popup-close">忽略</span>    </div>   </div>  </div></div>
