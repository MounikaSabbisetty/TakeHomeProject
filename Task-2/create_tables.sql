CREATE TABLE Sponsor (
manufacturer_id INT PRIMARY KEY,
manufacturer_name VARCHAR(255)
);
CREATE TABLE MedicalCondition (
med_condition_id INT,
med_condition VARCHAR(255)
);
CREATE TABLE DrugProduct (
protocol_id INT, submission_no VARCHAR(255),
brand_id INT,
manufacturer_id INT,
manufacturer_name VARCHAR(255),
brand_name VARCHAR(255)
);
CREATE TABLE Protocol (
protocol_id INT,
protocol_no VARCHAR(255),
submission_no VARCHAR(255),
status_id INT,
start_date DATE,
end_date DATE,
nol_date DATE,
protocol_title TEXT,
medConditionList JSONB,
studyPopulationList JSONB);
CREATE TABLE TrialStatus (
Status_id INT ,
Status_name VARCHAR(255)
);
CREATE TABLE StudyPopulation (
Study_population_id INT,
Study_population VARCHAR(255)
);
