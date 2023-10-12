<a href="https://link.springer.com/chapter/10.1007/978-981-15-9293-5_12">Link to the paper</a>

# An approach for optimizing algorithms which find k1-most demanding products
#### Abstract: 
The primary goal of this paper is on optimizing the process of finding k1-most demanding products using traditional algorithms and clustering. We have used four clustering algorithms over two traditional algorithms to optimize the time for finding k1-most demanding products. A synthetic data set was used for demonstration and the results are plotted in a graph for comparison. This approach can be used in various fields for optimization purposes.

##### Keywords: 
Data mining, Decision support, Clustering set of rules, Performance comparison.


#### Introduction:
As the number of businesses is increasing and the competition between them for gaining more customers is growing. Selecting the products which perform the best in the market is very crucial for their development. Also, the capability of a business to identify each of its clients, focusing on their purchases and customizing the advertisements will attract new customers. So, expecting the performance of the brand new product (nominee products NP) in the market of a number of the clients (C) based at the demand of current products (EP) that are present in the market is very important. We have the Satisfaction (like/dislike) information of man or woman consumers over the existing and nominee merchandise inside the market. This information may be proven in a tabular form called “Satisfaction bit strings” (SBS) (Table 1) which may be built the usage of BMI index data. The table shows the consumer-product relationship. The ep1 - ep3 is the present products (EP), np1 - np9 is the nominee products (NP) and c1 - c8 are the customers (C). The 1 or 0 represents the consumer is satisfied or not through the product respectively. For example, the sequence 1, 1, 1, 1, 0, 1, 0, 0 in table[1] 1st row indicates that the customers c1, c2, c3, c4, c6 are satisfied through the ep2 and customers c5, c7 and c8 are not. The chance that consumer c1 will choose nominee product np7 is 1/7 (from column 1, Table 1). It is thought that clients pick any product with the same chance so as c1 likes seven products inside the set NP   EP the possibility of purchasing is 1/7 for every case. The predicted demand for np5 is found by including the possibilities for each customer ci ∈ C deciding on np5 as follows: (1/9 + 0/7 + 0/6 + 0/6+ 0/8 + 1/6 + 1/6 +1/8) =0.569444..  
The company is expanding the business with a brand-new product (NP ). Now to take diverse managerial selections the goal is to perceive k1-most annoying merchandise (kNP) from the set EP ⋃ NP. For example, if k=3, the expected quantity of total clients for np2, np3 and np7 are 1.0218, 1.1468 and 0.9802 respectively. The anticipated range of general customers for kNP=np2, np3, np7 is (1.0218 + 1.1468 +0.9802 =) 3.1488. The cost 3.1488 is the best price among all of the combinations such as three (k1) applicants merchandise. The k1-most (right here, k1 is ready to a few) annoying merchandise are np2, np3, np7. The primary objective of this paper is to optimize the method of identifying the k1-maximum annoying products that combined with a few clustering sets of rules. First, we follow the clustering algorithm to organization comparable products right into a cluster and apply conventional algorithms on a particular cluster where the k1-most nominee products might also reside in. To evaluate the overall performance of our clustering-based k1-most demanding products, we ran the conventional algorithms on the complete dataset also. The resulting k1-merchandise selected in both the procedure has been the same.  
We used synthetic dataset(car dataset)from UCI machine mastering repository(http://archive.Ics.Uci.Edu/ml/index.Php) [11] 


| EPꓴNP|	c1|	c2|	c3|	c4|	c5|	c6|	c7|	c8 |
|----|----|----|----|----|----|----|----|----|
| ep1|	1|	0|	1|	1|	1|	0|	1|	1 |
| ep2|	1|	1|	1|	1|	0|	1|	0|	0 |
| ep3|	0|	1|	1|	1|	1|	0|	1|	1 |
| np1|	0|	0|	0|	0|	1|	1|	0|	0 |
| np2|	1|	1|	1|	1|	1|	1|	1|	0 |
| np3|	1|	1|	1|	1|	1|	1|	1|	1 |
| np4|	1|	1|	0|	0|	0|	0|	0|	1 |
| np5|	1|	0|	0|	0|	0|	1|	1|	1 |
| np6|	1|	1|	1|	1|	1|	0|	0|	1 |
| np7|	1|	1|	0|	1|	1|	1|	1|	1 |
| np8|	1|	0|	0|	0|	0|	0|	0|	1 |
| np9|	0|	0|	0|	0|	1|	0|	0|	0 |

Table 1. The SBS of the existing and nominee products 

This approach performs fairly well on most datasets. The outline of this paper is as follows: in Sect. 2 we present the related work and later described the proposed approach. Section 3 presents the results of the experiment 
