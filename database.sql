-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2022 at 03:49 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moviestore`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `UserID` int(10) NOT NULL,
  `MovieID` int(10) NOT NULL,
  `Title` varchar(30) NOT NULL,
  `amount` int(2) NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`UserID`, `MovieID`, `Title`, `amount`, `total`) VALUES
(2, 4, 'Due Date', 1, '6.00'),
(4, 2, 'Iron Man 2', 2, '30.00'),
(3, 6, 'Only You', 1, '16.68'),
(2, 3, 'Iron Man 3', 1, '21.00');

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `MovieID` int(10) NOT NULL,
  `Title` varchar(30) NOT NULL,
  `Director` text NOT NULL,
  `Year` int(4) NOT NULL,
  `Genre` text NOT NULL,
  `Amount` int(3) NOT NULL,
  `Price` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`MovieID`, `Title`, `Director`, `Year`, `Genre`, `Amount`, `Price`) VALUES
(1, 'Iron Man', 'Jon Favreau', 2008, 'action', 35, '16.00'),
(2, 'Iron Man 2', 'Jon Favreau', 2010, 'action', 40, '15.00'),
(3, 'Iron Man 3', 'Shane Black', 2013, 'action', 13, '21.00'),
(4, 'Due Date', 'Todd Phillips', 2010, 'Comedy', 15, '6.00'),
(5, 'Chef', 'Jon Favreau', 2014, 'comedy', 10, '5.99'),
(6, 'Only You', 'Norman Jewison', 1994, 'romance', 30, '16.68');

-- --------------------------------------------------------

--
-- Table structure for table `orderhistory`
--

CREATE TABLE `orderhistory` (
  `UserID` int(10) NOT NULL,
  `MovieID` int(10) NOT NULL,
  `Title` varchar(30) NOT NULL,
  `amount` int(2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `dateOrdered` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderhistory`
--

INSERT INTO `orderhistory` (`UserID`, `MovieID`, `Title`, `amount`, `total`, `dateOrdered`) VALUES
(1, 1, 'Iron Man', 2, '32.00', '2022-05-02'),
(1, 5, 'Chef', 1, '5.99', '2022-04-12'),
(3, 3, 'Iron Man 3', 2, '42.00', '2022-04-17'),
(3, 6, 'Only You', 1, '16.68', '2021-12-28');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UserID` int(10) NOT NULL,
  `Username` varchar(15) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Birthday` date NOT NULL,
  `CreditCardnum` bigint(16) NOT NULL,
  `cvv` int(3) NOT NULL,
  `CCexpire` date NOT NULL,
  `Address` varchar(80) NOT NULL,
  `City` varchar(30) NOT NULL,
  `State` text NOT NULL,
  `zip` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserID`, `Username`, `Password`, `Name`, `Birthday`, `CreditCardnum`, `cvv`, `CCexpire`, `Address`, `City`, `State`, `zip`) VALUES
(1, 'thd67', 'BasicDogName', 'Trey Dilly', '1998-09-16', 1234123412341234, 123, '2022-05-31', '350 Main Street', 'Starkville', 'MS', 39759),
(2, 'jkl35', 'I<3cats', 'Joseph Little', '2006-05-02', 1231231231231231, 876, '2022-07-08', '127 W Magnolia Drive', 'Starkville', 'MS', 39759),
(3, '12Foot dwarf', 'Longlivethedwarv3nking', 'Keith Stills', '1973-10-17', 4567456745674567, 938, '2023-06-02', '13 5th Street', 'Slidell', 'LA', 70458),
(4, '69__xXx__69', 'Longes+John', 'Tiny Dude', '2006-03-02', 2865328755328568, 734, '2022-05-04', '110 crossgates Boulevard', 'Brandon', 'MS', 39042);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`MovieID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UserID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
