CREATE TABLE `students` (
  `fname` varchar(45) NULL,
  `lname` varchar(45) NULL,
  `stuID` varchar(12) NOT NULL,
  `phone` varchar(45) NULL,
  `address` varchar(45) NULL,
   PRIMARY KEY (`stuID`)
);

INSERT INTO `students` (`fname`, `lname`, `stuID`, `phone`, `address`) VALUES
('Menna', 'Ashraf', '222333', '011111111', 'Alexandria, Egypt'),
('Aya', 'Ahmed', '222334', '016653534', 'Cairo, Egypt'),
('Sara', 'Mohamed', '222335', '027672546', 'Cairo, Egypt'),
('Rana', 'Ahmed', '222336', '018778757', 'Giza, Egypt'),
('Mennatallah', 'Mostafa', '222339', '012345678', 'Luxor, Egypt'),
