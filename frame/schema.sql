# 고객 정보 테이블
DROP TABLE IF EXISTS customer;

CREATE TABLE customer(
	id VARCHAR(10),        # id 10자리
	pwd VARCHAR(15),       # pwd 15자리
	name VARCHAR(10),
	age INT,
	height FLOAT,
	weight INT,
	right_size VARCHAR(5)
) DEFAULT CHARSET=utf8;

ALTER TABLE customer ADD PRIMARY KEY(id);
ALTER TABLE customer MODIFY COLUMN pwd VARCHAR(15) NOT NULL;
ALTER TABLE customer MODIFY COLUMN name VARCHAR(10) NOT NULL;
ALTER TABLE customer MODIFY COLUMN age INT NOT NULL;
ALTER TABLE customer MODIFY COLUMN height FLOAT NOT NULL;
ALTER TABLE customer MODIFY COLUMN weight INT NOT NULL;

INSERT INTO customer VALUES('id01', 'pwd01', '김영희', 31, 183.1, 63, '');   # '', 'NULL' 은 값이 있는 것으로 인식됨
INSERT INTO customer VALUES('id02', 'pwd01', '이영주', 24, 167.9, 71, NULL);


# 웹사이트 링크 테이블----------------------------------------------------------------------------------------------------
DROP TABLE IF EXISTS link;

CREATE TABLE link(
	id INT,
	size CHAR(5),
	mf VARCHAR(500),
	yoox VARCHAR(500),
	mt VARCHAR(500),
	net VARCHAR(500)
);

ALTER TABLE link ADD PRIMARY KEY(id);
ALTER TABLE link MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE link AUTO_INCREMENT=10;
ALTER TABLE link MODIFY COLUMN size CHAR(5) NOT NULL;
ALTER TABLE link MODIFY COLUMN mf VARCHAR(500) NOT NULL;
ALTER TABLE link MODIFY COLUMN yoox VARCHAR(500) NOT NULL;

INSERT INTO link VALUES(NULL, 'XXS', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10001', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=1&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=4533%7C7107%7C7389%7C7405%7C7424%7C7444%7C7453%7C7455', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522XXS%2522');
INSERT INTO link VALUES(NULL, 'XS', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10002', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=2&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=4709%7C4837%7C7108%7C7406%7C7425%7C7445%7C7448%7C7456%7C7480', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522XS%2522');
INSERT INTO link VALUES(NULL, 'S', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10003', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=3&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=2601%7C4843%7C7109%7C7407%7C7426%7C7438%7C7449%7C7457%7C7481', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522S%2522');
INSERT INTO link VALUES(NULL, 'M', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10004', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=4&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=2602%7C4838%7C7110%7C7117%7C7408%7C7427%7C7439%7C7450%7C7458%7C7482', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522M%2522');
INSERT INTO link VALUES(NULL, 'L', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10005', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=5&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=2603%7C4933%7C7111%7C7118%7C7145%7C7409%7C7428%7C7440%7C7451%7C7459', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522L%2522');
INSERT INTO link VALUES(NULL, 'XL', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10006', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=6&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=2604%7C7112%7C7256%7C7410%7C7431%7C7441%7C7452%7C7475', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522XL%2522');
INSERT INTO link VALUES(NULL, 'XXL', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10007', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=7&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=4719%7C7114%7C7411%7C7432%7C7442%7C7471%7C7478', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522XXL%2522');
INSERT INTO link VALUES(NULL, 'XXXL', 'https://www.matchesfashion.com/uk/womens/shop?q=%3A%3AclothesSize%3A10272', 'https://www.yoox.com/uk/%EC%97%AC%EC%84%B1/%EC%9D%98%EB%A5%98/shoponline#/dept=clothingwomen&gender=D&page=1&size=8&season=X',
								'https://www.mytheresa.com/en-gb/clothing.html?size_harmonized=5034%7C7122%7C7412%7C7479%7C7654%7C8215', 'https://www.net-a-porter.com/en-gb/shop/clothing?facet=ads_f15008_ntk_cs%253A%2522XXXL%2522');
