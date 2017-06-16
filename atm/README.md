ATM
==
作者:王宇夫  

### 程序介绍:
    实现ATM常用功能，账户信息、还款、取款、转账、账单，执行bin/atm.py
	管理功能，有创建银行账户，执行bin/manage.py
	
### 程序流程：
	####atm.py
	1、输入帐户密码认证，认证失败打印报错；       
	2、打印用户交互功能，输入选项；   
	3、账户信息、账单，直接打印；   
	4、还款、取款、转账，先打印信用额度和余额，输入还款、取款、转账的金额，余额满足正常扣款，余额不足返回提示；输入b，返回用户交互菜单
	5、账户信息都记录在db文件夹中；    
	6、访问、交易日志存放到log中，转账时，不打印转账用户的余额    
	####manage.py     
	1、打印用户交互功能，输入选项；   
	2、创建账户,输入新用户的密码，账户是根据db下account_id_record.json里面记录的id+1，就是新id,创建完成，把记录id的文件修改成最新的id     

### 程序结构:  
atm/   
├── README.md  
├── atm					(ATM主程目录)  
│   ├── __init__.py  
│   ├── bin 			(ATM执行文件目录)  
│   │   ├── __init__.py  
│   │   ├── atm.py  	(ATM 执行程序)  
│   │   └── manage.py 	(ATM 管理端)  
│   ├── conf 			(配置文件)  
│   │   ├── __init__.py  
│   │   └── settings.py  
│   ├── core 			(主要程序逻辑都在这个目录里)  
│   │   ├── __init__.py  
│   │   ├── accounts.py (用于从文件里加载和存储账户数据)   
│   │   ├── auth.py     (用户认证模块)  
│   │   ├── db_handler.py (数据库连接引擎)  
│   │   ├── logger.py   (日志记录模块)  
│   │   ├── main.py     (主逻辑交互程序)  
│   │   ├── manage_main.py  (管理逻辑交互程序) 
│   │   └── transaction.py  (记账\还钱\取钱等所有的与账户金额相关的操作都在这)  
│   ├── db  			(用户数据存储的地方)  
│   │   ├── __init__.py    
│   │   └── accounts 	(存各个用户的账户数据 ,一个用户一个文件)    
│   │       └── 1234.json (一个用户账户文件)   
│   │       └── account_id_record.json (一个用户账户id文件)   
│   └── log    
│       ├── __init__.py    
│       ├── access.log  
│       └── transactions.log      
└── shopping_mall    
    └── __init__.py    
