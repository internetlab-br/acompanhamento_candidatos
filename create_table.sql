CREATE TABLE `Tweets` (
  `idTweets` bigint(40) DEFAULT NULL,
  `plain text` text CHARACTER SET utf8mb4,
  `timestamp_tw` datetime DEFAULT NULL,
  `handle` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `retweets` int(11) DEFAULT NULL,
  `favs` int(11) DEFAULT NULL,
  `query` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_tabela` bigint(40) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_tabela`),
  UNIQUE KEY `unike` (`idTweets`,`query`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
