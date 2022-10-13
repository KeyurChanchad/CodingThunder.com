// MONGODB DATABASE

const { platform } = require("os")

// Download mongobd center from "https://www.mongodb.com/try/download/community"
// Create directory in C: named data inside another directory db "C:\data\bd" if not created then gives error at a time of mongod process. 
// copy path of bin file where mongo and mongod are there and set path of environment variable. 

// What is MONGO DB?
//No SQL Database
// Document orientaed
// open source, cross platform, document oriented database, written in c++

// In mongodb Database = Database, Tables = Collections, Rows = Documents
//Data is stored in BJSON form means it same as json but we must declare type of variable.

// mongod is the host process for the database. mongod in main process that connect to mongo database. 
// mongo is the command line shell that connect to a specific instance of mongod. 
//Instead of mongo we can connect mongod by python (pymongo), nodejs(mongoose)


// To show databases  ---> show dbs 
// To show tables     ---> show collections
// To use database or if it's exist then created   --->use keyurkart

// Inserting data in mongo db
// use keyurKart
//db.items.insert({}) db which database use that db, items is table name, insert row
db.items.insertOne({name: "Samsung 30s", price: 22000, rating: 4.5, qty: 233, sold: 98})

db.items.insertMany([{name: "Samsung 30s", price: 22000, rating: 4.5, qty: 233, sold: 98}, {name: "Moto 30s", price: 29000, rating: 3.5, qty: 133, sold: 598}, {name: "Realme 80s", price: 129000, rating: 2.5, qty: 633, sold: 98, isBig: true}])
