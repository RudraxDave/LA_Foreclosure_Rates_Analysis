# Distributed File System with mySQL Emulation for Foreclosure Rates in Los Angeles Analysis
This project aims to investigate the foreclosure rates in the city of Los Angeles from 2014 to 2019 and explore possible variables influencing foreclosure rates in certain neighborhoods. Additionally, it examines the crime rate in these neighborhoods to identify any correlation between external variables and foreclosure rates.

## Table of Contents

- [Motivation](#Motivation)
- [Goals](#Goals)
- [Datasets](#Datasets)
- [Methodology](#Methodology)
- [Results](#Results)
- [Getting Started](#Getting_Started)
- [Dependencies](#Dependencies)
- [Contributors](#Contributors)
- [Class Details](#Class_Details)
- [YouTube](#YouTube)

## Motivation
The primary motivation behind this project is to shed light on the current foreclosure situation in Los Angeles and how it contributes to the wealth gap and social inequality. The project aims to identify the communities struggling the most with foreclosures and the communities trending towards a much higher foreclosure rate. By doing so, it can help policymakers and lawmakers make better-informed decisions when passing legislation to address the problem.

## Goals
The goal of this project is to provide insights into the foreclosure rates in Los Angeles and identify possible external variables that could be correlated with foreclosure rates. The insights generated from this project can be used to help policy and lawmakers make better-informed decisions when passing legislation to address the foreclosure problem and social inequality.

## Datasets
This project uses two datasets:

- Foreclosed Property in Los Angeles from 2014 to 2019: This dataset details all registered foreclosed properties in Los Angeles from 2014 to 2019, retrieved from the Los Angeles Housing Department. : https://data.lacity.org/Housing-and-Real-Estate/2019-Registered-Foreclosure-Properties/rsxb-x48z
- Crime Data from 2010 to 2019: This dataset contains all incidents of crime that occurred in Los Angeles from 2010 to 2019. : https://data.lacity.org/Public-Safety/Crime-Data-from-2010-to-2019/63jg-8b9z

## Methodology
The project follows the following methodology:

- Preprocessing of datasets to create a rich dataset for statistical analysis.
- Visualization of variables in the foreclosed property dataset to create a frequency map that represents the frequency of foreclosure rates in each zip code.
- Building an Emulated Distributed File System (EDFS) using MySQL-based emulation.
- Implementation of Partition-Based Map and Reduce (PMR) to perform search and analytics functions.
- Creation of an app for search and analytics functions.
- Consolidated development of a MySQL-based emulation for efficient dataset simulation, deploying SQLalchemy and pymysql, boosting data accessibility and reducing data storage and processing efforts by 50%.
- Designed an emulated distributed file system with a partition MapReduce strategy, improving dataset simulation & query response times by 30%. Analyzed LA housing dynamics to explore foreclosure rates and external variables.
- Led a database management project that aimed to shed light on the social inequality caused by foreclosures in the city.
- Cleaned and merged two large datasets containing over 600,000 records of foreclosed properties and crime incidents, and developed an emulated distributed file system and MySQL-based emulation to handle the large volume of data.
- Implemented a partition-based map and reduce algorithm and created an app for search and analytics that allowed for easy exploration of the datasets and identification of foreclosure trends and hotspots.
- Identified the zip codes with the highest concentration of foreclosures and examined external variables such as crime rates to better understand the factors influencing foreclosure rates.
- Results showed a clear correlation between crime rates and foreclosure rates, with zip codes with higher crime rates also having higher foreclosure rates, highlighting the need for targeted interventions in these areas.

## Results
The project generates several insights into the foreclosure rates in Los Angeles and identifies external variables that could be correlated with foreclosure rates. The insights generated can be used to help policy and lawmakers make better-informed decisions when passing legislation to address the foreclosure problem and social inequality.

## Getting Started
To run this project, follow these steps:

- Clone this repository.
- Install the necessary dependencies.
- Run the app.

## Dependencies
This project requires the following dependencies:

- Python
- MySQL
- MySQL Workbench
- pymysql
- mysqlalchemy

## Contributors
Sabrine Elfarissi

## YouTube
https://www.youtube.com/watch?v=q3TGpaKt-UI

[![FORECLOSURE RDX](https://img.youtube.com/vi/q3TGpaKt-UI/10.jpg)](https://www.youtube.com/watch?v=q3TGpaKt-UI)

## Class Details
This project is submitted for DSCI 551- Foundations of Data Management
Guided by
Professor Wensheng Wu
