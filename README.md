
<h1>ETF NYSE Transaction Data Analysis</h1>
 
<h2>Description</h2>
Analyzing time-series stock movement data to identify key and new market players. 


- A PostgreSQL RDS database is constructed to optimize query-time efficiency and prioritize scalability for rapidly growing transaction data.
- On a monthly basis, \<BroadRidge API> is called to import data on 4 different types of ETF Products operated by QRAFT TECHNOLOGIES.
- The input data is automatically normalized into the locally run server at the firm through PANDAS and SQLAlchemy.
- To ensure maintainability, a simple GUI program was developed to allow non-technical users to interact and query from the DB.
- An automatic report generator was developed to send relevant monthly data to the sales team in the US through email.



<h2>Languages and Utilities Used</h2>

- <b>Python</b>
  - PySimpleGUI
  - SQLAlchemy
  - Pscycopg2
  - Pandas
- <b>PostgreSQL</b>
- <b>CSV</b>


<h2>Environments Used </h2>

- <b>Visual Studio Code</b>

<h2>Program walk-through:</h2>

<p align="center">
Program Output: <br/>
<a href="https://drive.google.com/uc?export=view&id=1g8B6U3k_L_KjDJgwUW_M8By2Zh1JQMXX"><img src="https://drive.google.com/uc?export=view&id=1g8B6U3k_L_KjDJgwUW_M8By2Zh1JQMXX" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
