# ETF NYSE Transaction Data Analysis
 
## Description
This project involves the analysis of time-series stock movement data to identify key and new market players in the ETF market on the New York Stock Exchange (NYSE).

## Overview
- PostgreSQL RDS Database: A PostgreSQL RDS (Relational Database Service) database is constructed to optimize query-time efficiency and prioritize scalability for rapidly growing transaction data.
- Data Import from <BroadRidge API>: Monthly data on four different types of ETF products operated by QRAFT TECHNOLOGIES is imported using the <BroadRidge API>. The data is crucial for understanding market trends.
- Data Normalization with PANDAS and SQLAlchemy: The imported data is automatically normalized into the locally run server at the firm using PANDAS for data manipulation and SQLAlchemy for efficient database interaction.
- GUI Program for User Interaction: To ensure maintainability and user-friendliness, a simple GUI program is developed. This allows non-technical users to interact with and query the database, making insights accessible to a broader audience.
- Automatic Report Generation: An automatic report generator is implemented to send relevant monthly data to the sales team in the US through email. This ensures that key insights are communicated efficiently.

## Technologies Used
- Python:
  - PySimpleGUI: A Python library for creating simple graphical user interfaces.
  - SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
  - Psycopg2: A PostgreSQL adapter for Python.
  - PANDAS: A powerful data manipulation and analysis library.
- PostgreSQL: A powerful, open-source relational database system.
- CSV: Comma-separated values format is used for efficient data exchange.

## Contributing
Feel free to contribute to the project by submitting issues or pull requests. Your input and suggestions are valuable!

