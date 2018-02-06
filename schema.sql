-----------------------------------------
-- Schema for derbylane-spider project --
-----------------------------------------

DROP TABLE IF EXISTS `dogentry`;
CREATE TABLE `dogentry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `birthDate` datetime DEFAULT NULL,
  `box` int(11) DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  `dogName` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `grade` varchar(255) DEFAULT NULL,
  `raceDate` datetime DEFAULT NULL,
  `raceNumber` int(11) DEFAULT NULL,
  `schedule` varchar(255) DEFAULT NULL,
  `track` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `dogresult`;
CREATE TABLE `dogresult` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `behind` double DEFAULT NULL,
  `box` int(11) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  `dogName` varchar(255) DEFAULT NULL,
  `finish` int(11) DEFAULT NULL,
  `grade` varchar(10) DEFAULT NULL,
  `raceDate` datetime DEFAULT NULL,
  `raceNumber` int(11) DEFAULT NULL,
  `schedule` varchar(10) DEFAULT NULL,
  `start` int(11) DEFAULT NULL,
  `stretch` int(11) DEFAULT NULL,
  `time` double DEFAULT NULL,
  `track` varchar(255) DEFAULT NULL,
  `turn` int(11) DEFAULT NULL,
  `weight` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
