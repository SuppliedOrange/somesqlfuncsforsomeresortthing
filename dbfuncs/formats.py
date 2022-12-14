# every table in the database and their formats

class Format():
    # This class basically takes 3 arguments. Table, Syntax and Columns. It organizes that into a class called format. (x).table, (x).syntax, (x).columns are ways to call it    
    def __init__ (self, table, syntax, columns):
        self.table = table 
        self.syntax = syntax 
        self.columns = columns 

# Formats:

Members = Format(
    "members",

    """
    username varchar(255) PRIMARY KEY,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) UNIQUE,
    password varchar(255) NOT NULL
    """,

    "(username, firstName, lastName, password)"
)

EncryptionTokens = Format(
    "encryptiontokens",

    """
    username varchar(255) PRIMARY KEY,
    token varchar(255) NOT NULL
    """,

    "(username, token)"
)

Resorts = Format(
    "resorts",

    """
    name varchar(255) PRIMARY KEY,
    location varchar(255) NOT NULL,
    price int NOT NULL,
    description varchar(690),
    facilities varchar(420)
    """,

    "(name, location, price, description, facilities)"
)

Bookings = Format(
    "bookings",

    """
    resort_name varchar(255) PRIMARY KEY,
    username varchar(255) UNIQUE NOT NULL,
    start_date date NOT NULL,
    end_date date,
    occupants int DEFAULT 1,
    cost int NOT NULL,
    id varchar(50) UNIQUE,
    FOREIGN KEY (resort_name) REFERENCES resorts(name) on update cascade on delete cascade
    """,

    "(resort_name, username, start_date, end_date, occupants, cost, id)"

)

# Database-table map
formats = {
    "resortdb": {
        "members": Members,
        "encryptiontokens": EncryptionTokens,
        "resorts": Resorts,
        "bookings": Bookings
    }
}