Shopping_mall
==
作者:王宇夫  

###程序介绍:
    实现购物常用功能，购物商场登录、添加购物车、结算、调用信用卡信息，执行bin/shopping_mall.py

###执行流程：  
	1、用户登录输入用户名密码，三次错误退出  
	2、打印购物列表，输入商品，加入购物车   
	2、打印购物列表，输入b，结算购物车，输入信用卡账户，调用atm用户，用户不存在认证失败，退出程序，认证成功，完成付款；如果余额无法购买   
	2、打印购物列表，输入q，退出程序   
	
		
###程序结构:  
atm/   
├── README.md  
├── shopping_mall		(shopping_mall主程目录)  
│   ├── __init__.py  
│   ├── bin 			(shopping_mall执行文件目录)  
│   │   ├── __init__.py  
│   │   ├── shopping_mall.py  	(shopping_mall 执行程序)  
│   ├── conf 			(配置文件)  
│   │   ├── __init__.py  
│   │   └── settings.py  
│   ├── core 			(主要程序逻辑都在这个目录里)  
│   │   ├── __init__.py  
│   │   ├── auth.py     (用户认证模块)  
│   │   ├── db_handler.py (数据库连接引擎)  
│   │   ├── logger.py   (日志记录模块)  
│   │   ├── main.py     (主逻辑交互程序)  
│   ├── db  			(用户数据存储的地方)  
│   │   ├── __init__.py    
│   │   └── accounts 	(存各个用户的账户数据 ,一个用户一个文件)    
│   │       └── 1234.json (一个用户账户文件)   
│   │       └── goods.json (商品文件)   
│   └── log    
│       ├── __init__.py    
│       ├── access.log  
│       └── transactions.log      
└── shopping_mall    
    └── __init__.py    