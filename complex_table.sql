CREATE TABLE InitiatingFirm (
  initiating_id BIGSERIAL,
  initiating_name VARCHAR(128),
  initiating_industry_id VARCHAR(16),
  addressline1 VARCHAR(128),
  addressline2 VARCHAR(128),
  addressline3 VARCHAR(128),
  address_type VARCHAR(16),
  city VARCHAR(128),
  country VARCHAR(128),
  postalcode VARCHAR(128),
  state_region VARCHAR(128),
  PRIMARY KEY (initiating_id)
);

CREATE TABLE IntermediaryFirm (
  intermediatry_name VARCHAR(128),
  intermediatry_id BIGSERIAL,
  PRIMARY KEY (intermediatry_id)
);

CREATE TABLE Etf (
  ticker_symbol VARCHAR(5),
  PRIMARY KEY (ticker_symbol)
);

CREATE TABLE Transactions (
  transaction_id BigSERIAL,
  intermediatry_id INTEGER,
  initiating_id INTEGER,
  channel VARCHAR(64),
  tickersymbol VARCHAR(5),
  transaction_date DATE,
  nna FLOAT(4),
  aum FLOAT(4),
  shares FLOAT(4),

  PRIMARY KEY (transaction_id),
  CONSTRAINT "FK_Transactions.initiating_id"
    FOREIGN KEY (initiating_id)
      REFERENCES InitiatingFirm(initiating_id),
  CONSTRAINT "FK_Transactions.tickersymbol"
    FOREIGN KEY (tickersymbol)
      REFERENCES Etf(ticker_symbol),
  CONSTRAINT "FK_Transactions.intermediatry_id"
    FOREIGN KEY (intermediatry_id)
      REFERENCES IntermediaryFirm(intermediatry_id)
);
