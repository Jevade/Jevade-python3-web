CREATE DATABASE  IF NOT EXISTS `awesome` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `awesome`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: awesome
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blogs`
--

DROP TABLE IF EXISTS `blogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs` (
  `id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `summary` varchar(200) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  `private` tinyint(1) NOT NULL DEFAULT '0',
  `clicked` int(11) NOT NULL DEFAULT '0',
  `comments` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs`
--

LOCK TABLES `blogs` WRITE;
/*!40000 ALTER TABLE `blogs` DISABLE KEYS */;
INSERT INTO `blogs` VALUES ('001493883071762d52bc476f3174f7e9c79c5e973324fa700','001493779297791eb099a9b72a144c1967d2aa51110464a00','小敏','http://www.gravatar.com/avatar/e92e01af807fc8eedace58b4e75fe20b?d=mm&s=120','漫天的繁星才是他们的最爱','我们以为地铁很便捷，可是对于一个不适应的孩子来说甚至是种折磨。我们眼中的车水马龙、灯红酒绿，在外公眼里都不过是噪音，对于一个农村孩子而言，到了夜晚，漫天的繁星才是他们的最爱......???','湖南卫视的《变形计》自开播以来就被各种各样的批评声包围，大家认为“变形”对于农村孩子而言是种伤害，让他们开拓的不是眼界，而是埋下了仇富的种子。\n\n知乎上有一个提问：变形计为什么对农村的孩子是种伤害？\n\n点赞最多的一个回答是这样的：因为他们会适应了城市里的各种方便和城市里的那种散漫。\n\n我试着想了想，七天真的就可以适应城市的生活吗？答案是否定的。我外公，地地道道的农民，面朝黄土背朝天，在农村生活了一辈子，每次来城里都好像是折磨他一样。\n\n待不了2天就嚷嚷着要回去。所以，如果说《变形计》让农村的孩子适应了城市里的散漫，适应了城市的便捷是不成立的。在农村孩子眼里，这7天的生活很大可能就如同外公一样，只觉得格格不入，还不如在农村的自在。\n\n我们以为地铁很便捷，可是对于一个不适应的孩子来说甚至是种折磨。我们眼中的车水马龙、灯红酒绿，在外公眼里都不过是噪音，对于一个农村孩子而言，到了夜晚，漫天的繁星才是他们的最爱。\n\n龙应台在《亲爱的安德烈》中说：农村中长大的孩子，会接触更真实的社会，接触更丰富的生活，会感受到人间的各种悲欢离合。所以更能形成那种原始的，正面的价值观——”那“愚昧无知”的渔村，确实没有给我知识，但是给了我一种能力，悲悯同情的能力，使得我在日后面对权力的傲慢、欲望的嚣张和种种时代的虚假时，仍旧得以穿透，看见文明的核心关怀所在。\n\n-2-\n\n在《年轻人该如何提高眼界，摆脱思维局限？》一文，我认为眼界没有高低优劣，经历不同，得到的不同，真的要比个高低，那就只能说谁的眼界更适应这个社会罢了。\n\n比起担心农村孩子回去后不能适应原来的生活，我觉得更值得我们警惕的是因此产生的嫉妒心。\n\n一个上不起学，吃不饱饭的孩子到了城市里，城市爸爸妈妈为了尽地主之谊，又或是出于同情的原因，带他们去最好的餐厅，买最好的衣服，这些都无可厚非。\n\n但，人是会比较的，无论大人还是小孩。\n\n7天的城市生活转瞬即逝，如同做了一场梦，对于这个繁华的都市，终究只是一个过客，回到农村，巨大的心理落差开始萌芽，而这份情绪便很可能转换成嫉妒，甚至是一种仇富的心态。\n\n所以，希望节目组不要为了一时的收视率而放弃对农村孩子心里的引导，现在的通讯如此发达，如果可以，是否能安排1-2个网络心理医生，定期和孩子沟通，及时发现潜在的危险。\n\n比较只是一个中性词，学会利用它或许会成为我们成长的利器。引导孩子们朝着正面的方向前进，即使速度很慢，但注定有所成长。',1493883071.76211,1,8,0),('00149389173534991e7c972d9db4c26b8610e006fb0487c00','001493301274801521ec4e45f994f50a93d581281ac325a00','jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120','偏差值','知乎转载','作者：大象\n链接：https://www.zhihu.com/question/59216554/answer/163421973\n来源：知乎\n著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。\n\n有几个定量研究里面经常被混淆的概念偏倚(Bias)和误差(Error)误差分为系统误差和随机误差，而偏倚是指系统误差，因此我们说一个研究存在偏倚的时候，指的是研究中计算出的估计值与真实值之间存在系统误差。\n\n经常有同学会问，如果线性回归的残差不满足独立，正态或者等方差的条件会不会导致偏倚？实际上，这些条件的违背只会影响对随机误差的估计，而不会增加系统误差，因此不会造成偏倚。偏倚(Bias)和缪误(Fallacy)这个混淆经常出现在生态学缪误 (Ecological Fallacy)的语境中，很多人把生态学缪误归为偏倚的一种。\n\n其实这是不对的，生态学缪误在于错误地把生态学层面的结论推论到个体水平，是一种结论解读的错误，而不是研究本身存在偏倚。例如有人分别利用社区和个体级别的数据，研究了外来人口和自评健康得分的关系。用社区水平数据的分析发现，外来人口比例高的社区，其平均自评健康得分也高。\n\n而个体水平上，是否是外来人口却与自评健康得分成负相关。这两个研究本身都没有问题，但当把社区层面的结论地简单推论到个体水平时，就是发生了我们说的生态学缪误。无偏估计值和真值无偏估计值和真值是两个不同的概念。这样的混淆经常出现在一些论文中，得到了一个正的回归系数，但标准误很大以至于统计学上不显著。作者常解释说，因为研究控制了足够多的混杂因素或者使用了工具变量，所以点估计不受影响，进而开始解释这个回归系数的意义是什么。实际上，点估计是一个变量，而无偏估计值是指点估计值的期望等于真值，而不是说当前研究里面得到的这个点估计就是一个稳定不变的真值。\n\n因果和相关“相关不等于因果”和“脱离剂量谈毒性”已经成为知乎上评论区打脸的标配了，然而当讨论到因果和相关性强弱时，却又容易发生混淆。比如研究中证实A与B存在因果关系，在排除了混杂因素的影响后，是不是A和B一定高度相关呢？答案并不是，如果没有效应修饰作用，A和B的因果关系是一个与人群无关的量，而相关性却会随人群变化而变化，如果在一个人群中A的取值都相同，A和B的相关性为0，但A和B的因果关系却总是存在的。效应强度和统计学显著这类混淆在解释回归系数的时候可能会发生。\n\n统计学显著指的是P值小于一个预先设定的一类错误率  。P值的大小随样本量，效应强度变化而变化，P值小不代表效应强度就大。有统计学意义，不一定效应强度就有实际意义。统计学显著和统计功效这类混淆常发生在阴性结果的解读中。通常论文里会有这样的句子，A组和B组的均值差异没有统计学意义（P=0.85)，因此我们得出结论，A组和B组没有差别。实际上，P值仅代表原假设成立时，观察到这样或更大均值差的概率，并不能告诉我们错误地接受原假设的概率是多少。得到大P值可能是因为样本量小，要验证A组和B组没有差别，需要计算的是统计功效而不是P值。效应强度和证据强度这个混淆很常见，一个因果关系的证据等级不能代表其效应强度的大小。因果关系的证据等级强弱和很多因素有关，包括了效应强度，更重要的是这个问题是不是重要的问题，以至于能有足够多和足够严谨的研究。\n\n常见的混淆是认为IARC对致癌物的分级代表了致癌物效应的强弱，其实这个只是代表了证据是否充分而已。又比如，心血管疾病危险因素的证据往往比较充分，而脱发的危险因素可能证据就不充分了，原因是研究脱发比研究心血管疾病难拿研究经费。假设(Assumption)和假设(Hypothesis)这里的Assumption和Hypothesis在中文里有时候都叫假设，实际上假设和假设是完全不同的。\n\n在一个研究里，Assumption是你假定已经满足的前提条件，而Hypothesis是要检验的命题。Assumption可以是研究中不能证明的部分。比如用身高决定基因的多态性作为身高的工具变量，来研究身高与社会经济地位的关系。这里就有三个Assumption，身高的决定基因能决定身高，身高的决定基因不会通过其他因素影响社会经济地位，身高的决定基因只能通过身高来影响社会经济地位，其中后两个Assumption是无法用实证证明的。而这个研究中的Hypothesis是身高与社会经济地位有关。',1493891735.3493,0,22,0),('001493917669069edd3e7cfa1124f20a090bef75eeb584900','001493301274801521ec4e45f994f50a93d581281ac325a00','jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120','“最后没有在一起，该不该删对方好友？”','有些关系只能到此为止，再前进一点，或许就是万丈深渊。﻿﻿','文/曲尚菇凉﻿\n\n1.﻿\n\n回家的公交车上，旁边一姑娘在打电话，对方大概是她好朋友。她说她昨天跟喜欢的男生表白，可是被男生拒绝了，男生说还不想恋爱，想好好工作。﻿﻿\n\n姑娘觉得尴尬，怕留着对方的联系方式自己会忍不住去联系他，所以就把他给删了。﻿﻿\n\n她说她真的很难受，表白失败连朋友都不是，可不表白自己又不甘心。因为不缺朋友啊，缺的只是男朋友，而这个男朋友，我希望能够是你，所以最终在两者之间选择了后者。﻿﻿\n\n而选择这个后者的代价就是失去再次问候的身份，要说以朋友的名义再去和他聊天，那不可能，他觉得尴尬，自己本身也会觉得如此。何况那种氛围，估计会冷成冰。﻿﻿\n\n选择后者的同时，要做好两种准备。一是你去表白，然后成功了，你们在一起了。二是你去表白，然后失败了，你们做不回朋友了。﻿﻿\n\n在一段感情中，一但牵扯到爱，说实话，那味道就不一样了。关系再好的两个人，如果捅破了最后一层膜，提到了爱，那可能两人之间多多少少也会有些阻碍。﻿﻿\n\n有些关系只能到此为止，再前进一点，或许就是万丈深渊。﻿﻿\n\n2.﻿\n\n姑娘跟朋友打完电话，哭的像个泪人，在一旁的我看着有些心疼，从包里拿出纸巾叠好递给他。她抬起头看了看我，说了句谢谢。﻿﻿\n\n我微笑的回了句，没事。﻿﻿\n\n姑娘看我拿着手机码字，便问我：你是在写小说嘛？我摇摇头说不是，只是写文章。﻿﻿\n\n她想了一会，然后问我：刚刚我和朋友说的话，你应该也听到了吧。我不好意思的点了点头。﻿﻿\n\n我说，很难受这种感觉，我也曾体会过。﻿﻿\n\n姑娘好奇的问我，那你是怎么度过的。﻿﻿\n\n很久之前喜欢的一个男生，那时候我们都还不懂事，只知道喜欢一个人就是要对他好，如果他也喜欢你的话，那他也一定会对你好。﻿﻿\n\n后来，我付出了很多，他都没用感动。可能这就是不爱吧，当你不喜欢一个人时，无论他做什么你都不会感动，无论他对你有多好，你都不会在意。因为没有感情在里面，虽然说人都是感情动物，心都是软的，但是心软并不能够转化为爱情。﻿﻿\n\n孩子气的我把他删了，他也不曾发觉。那段时间我每天都逼自己忍住不碰手机，因为我知道一碰手机我就想着到处寻找他的痕迹，甚至可能会忍不住把他加回来。﻿﻿\n\n直到有一天，我发了一条说说“什么时候你会发现，你的列表里少了一个我？”，他评论了一句：刚刚发现。﻿﻿\n\n我愣了一会，没想到他会看到这条说说，也没想到他竟然还会评论。之后我也忘了我们是怎么又恢复成好友的，不记得是我加他还是他加我。﻿﻿\n\n我只记得那段时间是真的难熬，他的手机号，QQ号，微信号，我都倒背如流，却始终提醒自己忍住，不能联系。好像联系了就会有什么大事发生一样。﻿﻿\n\n3.﻿\n\n姑娘问：然后呢？﻿﻿\n\n然后。然后我再也没有删过任何人，因为我在这期间明白了一个道理。﻿﻿\n\n姑娘疑惑的看着我，我说，其实删和不删都一样，你删掉他的联系方式，你就真的能不联系了嘛？s如果真的忍不住，很想他的话，你还是去给他打电话，问他在干嘛。﻿﻿\n\n所谓的删好友，删联系人，不过就是自己潜意识里的一个感情枷锁，你以为你解开了，可没想到那个锁早已生了锈。﻿﻿\n\n比如和前男友分手后，我们都很默契的没有删掉彼此的任何联系方式。我们之间可能偶尔会聊几句，但是基本上没什么事都不会去打扰，因为我们都知道，我们的感情已经是过去式了。﻿﻿\n\n朋友说，你们都分手了，还留着联系方式干嘛？虐自己啊？我说不啊，我只是还想知道他的消息，尽管他已经不是我的爱人。﻿﻿﻿\n\n我和他是我们圈子里唯一一对分手后没有互删的。我时常调侃着说，就属我们这对最冷静，最理智。﻿﻿\n\n4.﻿\n\n或许有些人会觉得没有必要再看到对方的生活，或许有些人会觉得没什么。不管对方过得好不好都与自己无关，好也罢，不好也罢，那都是他的事。你都只是一个前任。﻿﻿\n\n当真要删除一个人，那应该是在心里删掉，并非手动删除。手动删除，脑海中还有记忆，人是很难去控制自己的大脑，一般都是随着心里的想法去做某一件事情。﻿﻿\n\n我看到他在朋友圈里发他和他女朋友的照片，秀着恩爱的时候，我也很难受啊，可那又能怎样，我清楚自己的定位。看到他过得快乐，我也为他开心，只是我做不到祝他们幸福，我只能祝他幸福。﻿﻿\n\n终有一天，我也会这样在朋友圈里秀着我和我男朋友的照片，到时候咱还可以来比比。﻿﻿\n\n可能很久之后的某一天，当我们再次回想起曾经时，看到对方发的一个动态，还会感到一丝心酸。那个曾经我最深爱的人如今有了依靠，这时或许我们能够做到去释怀，去道一声祝福。﻿﻿\n\n去和那个Ta说句：你有你的爱人，我有我的爱人，祝你幸福，也祝我幸福。\n\n                                  —end—\n\n 南方姑娘的梦 © 著作权归作者所有 举报文章',1493917669.06915,0,17,0),('001493931581835440098927c3a4e698bd1af4863af991700','001493779297791eb099a9b72a144c1967d2aa51110464a00','小敏','http://www.gravatar.com/avatar/e92e01af807fc8eedace58b4e75fe20b?d=mm&s=120','凌晨五点的北京','一个晚上的加班加点，博客网站开始渐渐成型','一个晚上的加班加点，博客网站开始渐渐成型。',1493931581.8352,0,3,0),('001493988050929704b5b9b9d05433987feb6da81239f6200','001493301274801521ec4e45f994f50a93d581281ac325a00','jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120','一一','你看见','进口红酒',1493988050.92987,0,0,0),('001493988074616639169f6a07d4bba8ee0f13b9c08a43d00','001493301274801521ec4e45f994f50a93d581281ac325a00','jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120','将军金甲夜不脱','坎坎坷坷','离开老厉害了',1493988074.61686,1,0,0);
/*!40000 ALTER TABLE `blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` varchar(50) NOT NULL,
  `blog_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES ('001493892462048b62cecad1a1445649381d755c93da4d600','001493883071762d52bc476f3174f7e9c79c5e973324fa700','001493779297791eb099a9b72a144c1967d2aa51110464a00','小敏','http://www.gravatar.com/avatar/e92e01af807fc8eedace58b4e75fe20b?d=mm&s=120','这就是真实的一面',1493892462.04861),('001493931067631eab36a040e7a4f5aa987e9d58360f76200','001493930782896f3fd02e8342d4634ab522a95a09b9a9a00','001493301274801521ec4e45f994f50a93d581281ac325a00','jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120','youdianyisi',1493931067.63146);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('001493301274801521ec4e45f994f50a93d581281ac325a00','1107779806@qq.com','123',1,'jiawei','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120',1493301274.801),('001493305854870849c6e948d1141478092b8cbb40e086700','13204140501@qq.com','0501',0,'wy','http://www.gravatar.com/avatar/8539fa9ad2ee54d2cbc0dd068cf58b8d?d=mm&s=120',1493305854.87033),('001493779297791eb099a9b72a144c1967d2aa51110464a00','min@163.com','8c8eacabbfaad17924548d14b6096676fffa3849',0,'小敏','http://www.gravatar.com/avatar/e92e01af807fc8eedace58b4e75fe20b?d=mm&s=120',1493779297.7918),('001493931655655d636a306b0684c32b64361a139c4863400','li@133.com','b79b856ae2208735167e573ddfea8d930a549c67',0,'li','http://www.gravatar.com/avatar/708b64e069f215e60aba0f956b71d687?d=mm&s=120',1493931655.65538);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-05 22:57:27
