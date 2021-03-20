import psycopg2
def connn():
    conn = psycopg2.connect(database='Notify', user='postgres', password='1999', host='localhost', port='5432')
    cur = conn.cursor()
    return(conn,cur)
conn,cur=connn()

cur.execute('''CREATE TABLE 
	customer(customer_id INT,
	firstName varchar(50),
	lastName varchar(50),
	Email varchar(100),
	password varchar(300),
	PRIMARY KEY(customer_id))''')

cur.execute('''CREATE TABLE 
	Notify(Notify_id INT,
	customer_id INT,
	Product_id INT ,
	IMprice varchar(100),
	ended boolean )''')
# PRIMARY KEY(Notify_id),
# 	FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
# 	FOREIGN KEY(Product_id))


cur.execute('''CREATE TABLE 
	Product(Product_id INT,
	sku VARCHAR(50),title VARCHAR(300),
	manufacture VARCHAR(50),
	description text,
	img text[],categroy INT,
	keywords text[],ean VARCHAR(50),
	lowertPrice VARCHAR(50),
	AvgRatING INT )''')
	# PRIMARY KEY(Product_id),
	# FOREIGN KEY(categroy) REFERENCES customer(customer_id)

cur.execute('''CREATE TABLE noon (
	noonID VARCHAR (300) not NULL,
    sku VARCHAR (300) not NULL,
    title VARCHAR (300) not NULL,

    active boolean NOT NULL, 
    lastPrice varchar(50),
    productID serial)''')
	#  rate float
	    # category serial,
	    # id serial PRIMARY KEY,
	#  CONSTRAINT fk_category
    #   FOREIGN KEY(category) 
	#     REFERENCES category(id)
	#     ON DELETE SET NULL,
    # CONSTRAINT fk_productID
    #   FOREIGN KEY(productID) 
    #   REFERENCES product(id)
    #   ON DELETE SET NULL


cur.execute('''CREATE TABLE 
	Jumia(Jumia_id INT,
	Product_id VARCHAR(50),
	sku VARCHAR(50),
	title VARCHAR(300),
	manufacture VARCHAR(50),
	description text,
	categroy INT,
	keywords text[],
	ean VARCHAR(50),
	active boolean,
	lastPrice VARCHAR(50),
	JumiaID VARCHAR(50),
	rate INT )''')
	# 	PRIMARY KEY(Jumia_id),
	# FOREIGN KEY(Product_id),
	# FOREIGN KEY(categroy)

cur.execute('''CREATE TABLE 
	Souq(Souq_id INT,
	Product_id VARCHAR(50),
	sku VARCHAR(50),
	title VARCHAR(300),
	manufacture VARCHAR(50),
	description text,
	img text [] ,
	categroy INT,
	keywords text[],
	ean VARCHAR(50),
	active boolean,
	lastPrice VARCHAR(50),
	SouqID VARCHAR(50),
	rate INT )''')
	# 	PRIMARY KEY(Souq_id),
	# FOREIGN KEY(Product_id),
	# FOREIGN KEY(categroy)

cur.execute('''CREATE TABLE category(name VARCHAR(300))''')
	PRIMARY KEY(categroy_id)

cur.execute('''CREATE TABLE 
	PriceHistory(Product_id INT ,
	date_product Date ,
	price VARCHAR(50))''')
	# FOREIGN KEY(Product_id)

cur.execute('''CREATE TABLE 
	img(img_id INT ,
	Product_id INT,
	imgpath VARCHAR(300))''')
	# 	PRIMARY KEY(img_id),
	# FOREIGN KEY(Product_id)
conn.commit()
