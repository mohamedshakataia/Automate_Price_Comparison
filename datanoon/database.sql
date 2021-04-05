-- table creation
CREATE TABLE category (
	id serial PRIMARY KEY,
	sweetName VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE img (
	id serial PRIMARY KEY,
	productID serial,
  imgPath varchar(300)
);

CREATE TABLE product (
    id serial PRIMARY KEY,
    ean VARCHAR (50) not NULL,
    title VARCHAR (50) not NULL,
    manufacture varchar(50),
    category serial,
    lastPrice varchar(50),
    mainImg text,
    fullDescription text,
    SouqID INT,
    avgRating float,
    img serial,
    CONSTRAINT fk_category
      FOREIGN KEY(category) 
	    REFERENCES category(id)
	    ON DELETE SET NULL,
    CONSTRAINT fk_img
      FOREIGN KEY(img) 
	    REFERENCES img(id)
	    ON DELETE SET NULL
      );
ALTER TABLE img 
ADD CONSTRAINT fk_productID
FOREIGN KEY(productID) 
REFERENCES product(id)
ON DELETE SET NULL;

CREATE TABLE souq (
    id serial PRIMARY KEY,
    ean VARCHAR (50) not NULL,
    title VARCHAR (50) not NULL,
    manufacture varchar(50),
    category serial,
    active boolean NOT NULL, 
    lastPrice varchar(50),
    mainImg text,
    productID serial,
    fullDescription text,
    SouqID INT,
    rate float,
    CONSTRAINT fk_category
      FOREIGN KEY(category) 
	    REFERENCES category(id)
	    ON DELETE SET NULL,
    CONSTRAINT fk_productID
      FOREIGN KEY(productID) 
      REFERENCES product(id)
      ON DELETE SET NULL
);
CREATE TABLE jumia (
    id serial PRIMARY KEY,
    sku VARCHAR (50) not NULL,
    title VARCHAR (50) not NULL,
    manufacture varchar(50),
    category serial,
    active boolean NOT NULL, 
    lastPrice varchar(50),
    mainImg text,
    productID serial,
    fullDescription text,
    jumiaID INT,
    rate float,
    CONSTRAINT fk_category
      FOREIGN KEY(category) 
	    REFERENCES category(id)
	    ON DELETE SET NULL,
    CONSTRAINT fk_productID
      FOREIGN KEY(productID) 
      REFERENCES product(id)
      ON DELETE SET NULL
);
CREATE TABLE noon (
    id serial PRIMARY KEY,
    noonID VARCHAR (50) not NULL,
    sku VARCHAR (50) not NULL,
    title VARCHAR (300) not NULL,
    manufacture varchar(50),
    category serial,
    active boolean NOT NULL, 
    lastPrice varchar(50),
    mainImg text,
    productID serial,
    fullDescription text,
    rate float,
    CONSTRAINT fk_category
      FOREIGN KEY(category) 
	    REFERENCES category(id)
	    ON DELETE SET NULL
      );
CREATE TABLE PriceHistory (
	productID serial,
	dateOFchange date,
  price varchar(50),
  CONSTRAINT fk_productID
    FOREIGN KEY(productID) 
    REFERENCES product(id)
    ON DELETE SET NULL
);

