# TODO: 
1. 数据处理（采用中位数，众数填充缺失值，创造交叉项，LASSO，PCA, 对于y值log）
2. EDA
3. 模型选择（XGBoost，TFDF，RF, ridge, elastic, 多项式检测哪些是非线性关系）

# 2024.9.2
TODO：
1. 类别型变量
	- <input type="checkbox"> 检查处理缺失值（填充，删除）
	
	- <input type="checkbox"> 查看数据分布（每一类有多少个值，每一个变量售价的平均值）

	![image1](https://github.com/laofoye99/house_price_regression/blob/main/Archive/EDA_result/Boxplot%20of%20MSSubClass.png?raw=true)

	![image2](https://github.com/laofoye99/house_price_regression/blob/main/Archive/EDA_result/Distribution%20of%20MSSubClass.png?raw=true)

	- <input type="checkbox"> 检查多重共线性（PCA，Lasso，Ridge）

	- <input type="checkbox"> 编码（对类别数据进行编码）

	- <input type="checkbox"> 检查处理异常值
	![image](https://www.kaggleusercontent.com/kf/94433095/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..PRjJ6a34_kG3hBor0ndQdA.9jGujbPrJ0LE3wa02qx-e4oYIa53e90bwpqIuzE4iZGrZqz0ivAEzQ3lgcKFQEDT3F8OIvi9nyWPxG-OrYFaiQQuvpugvGSgU7HF4VZodt9Ck8MrO7Sghg5faQeqh5TYE0mb9PXLL5PSXel81UcU9RcjQ4wXrCJH9-2NaqUR26faguoOQB0TeUXzrTiBYIG1no7ibVUne-0e9BhsFM6zcHRdASmVZ3cVTp-nfkgWlY1LsvGqYFNNOiKAytkgGsThf8hhHcsMkyNPxrhgywNQ-MEX_JmEe1AqzhzyPWcKBGIecPnw0jdI4LfpkZ-kl8dUc_IQGvvLbJC9pJFbNAiy0jsjFZTieStuTr_42hVMCjwqXqEWtvDcIN6N2tKxEyYfYZn18tf2LNRIgcfsoD_EwfL4RI2e_j6Q9-3IjNOdEPWjuvyWQsa12bIBt-RX_xyg96nMevQ5zFdjfKHJJCQXvcu29NkozwMIGHdykl0vca4dwniZqkyGRaqlXdu-PvV7FdZ3pH4kkhJSuRnlqMO1-2YhmYKZpNsO2LpOu2RzXU5aEDSEhTNZaOjabF2Mb8BXSO0fViOmzTLz5ub3IaKW7ur7_DkYsGKskBGSu7q-2_zA6IFc8oTuj2t5jnrADA7fuR0QEXW666rsaOxWSYBj0wV7a4tppkVfgiFPCSrrZo8.9J7epdXrcFrMQn-Q7bgS1g/__results___files/__results___62_1.png)
	- <input type="checkbox"> 特征选择

2. 数值型变量
	- <input type="checkbox"> 检查缺失值和异常值
	- <input type="checkbox"> 标准化
	- <input type="checkbox"> 特征工程（多项式特征，交互特征）
	- <input type="checkbox"> 特征选择
	- <input type="checkbox"> 创建 evaluation function
	- <input type="checkbox"> 绘制多变量关系图（pairplot）