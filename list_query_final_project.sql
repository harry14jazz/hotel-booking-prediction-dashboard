-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS hotel_pwdk;

-- set the db that we use
USE hotel_pwdk;

-- create table
CREATE TABLE hotel_bookings(
	hotel INT, 
	lead_time INT, 
	arrival_date_year INT, 
	arrival_date_month INT,
	arrival_date_week_number INT, 
	arrival_date_day_of_month INT,
	stays_in_weekend_nights INT, 
	stays_in_week_nights INT, 
	adults INT, 
	children float,
	babies INT, 
	is_repeated_guest INT, 
	previous_cancellations INT,
	previous_bookings_not_canceled INT, 
	booking_changes INT, 
	agent float,
	days_in_waiting_list INT, 
	adr float, 
	required_car_parking_spaces INT, 
	total_of_special_requests INT, 
	meal__BB INT, 
	meal__FB INT, 
	meal__HB INT,
	meal__SC INT, 
	country__BEL INT, 
	country__BRA INT, 
	country__DEU INT,
	country__ESP INT, 
	country__FRA INT, 
	country__GBR INT, 
	country__IRL INT,
	country__ITA INT, 
	country__PRT INT,
	country__Other INT, 
	market_segment__Aviation INT, 
	market_segment__Complementary INT,
	market_segment__Corporate INT, 
	market_segment__Direct INT,
	market_segment__Groups INT, 
	market_segment__Offline__TA_TO INT,
	market_segment__Online__TA INT, 
	distribution_channel__Corporate INT,
	distribution_channel__Direct INT, 
	distribution_channel__GDS INT,
	distribution_channel__TA_TO INT, 
	deposit_type__No_Deposit INT,
	deposit_type__Non_Refund INT, 
	deposit_type__Refundable INT,
	customer_type__Contract INT, 
	customer_type__Group INT,
	customer_type__Transient INT, 
	customer_type__Transient_Party INT,
	reserved_room_type__A INT, 
	reserved_room_type__B INT,
	reserved_room_type__C INT, 
	reserved_room_type__D INT,
	reserved_room_type__E INT, 
	reserved_room_type__F INT,
	reserved_room_type__G INT, 
	reserved_room_type__H INT,
	reserved_room_type__L INT, 
	assigned_room_type__A INT,
	assigned_room_type__B INT, 
	assigned_room_type__C INT,
	assigned_room_type__D INT, 
	assigned_room_type__E INT,
	assigned_room_type__F INT, 
	assigned_room_type__G INT,
	assigned_room_type__H INT, 
	assigned_room_type__I INT,
	assigned_room_type__K INT, 
	assigned_room_type__L INT
);

-- load csv to database
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ml_data.csv'
INTO TABLE hotel_bookings
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT *
FROM hotel_bookings
LIMIT 1000;

SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'hotel_bookings';

-- hapus isi semua data
TRUNCATE TABLE hotel_bookings;
DROP TABLE hotel_bookings; 