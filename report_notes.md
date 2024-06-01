# Report Notes

## Part I: Research Question

### A: Research Question

Which features in the provided dataset are most useful for accurately predicting whether a patient will be readmitted within a month of release?

### B: Describe all Variables

The column indices indicate the columns as they are imported from the original `.csv` into Pandas. As such, they are zero-indexed and include the leftmost value from the original `.csv`.

As some columns have logical groupings, the indexes may appear slightly out of order.

#### Indexing variables

| Column Index | Column Name | Data Type | Variable Type    | Samples      |
| ------------ | ----------- | --------- | ---------------- | ------------ |
| 0            | Unnamed: 0  | Integer   | Sequential Index | `1, 2, 3, 4` |
| 1            | CaseOrder   | Integer   | Sequential index | `1, 2, 3, 4` |

Both of these variables contain a sequential index (from 1 to 10000) and are duplicates of one another. They are stored as integers, and only serve to maintain the sequential order of records. As the Pandas DataFrame data structure provides a numeric index by default, these features can be removed.

Examples:

#### Customer Identification, Location, and Demographics

##### Identification

| Column Index | Column Name | Data Type | Variable Type                             | Samples                                                      |
| ------------ | ----------- | --------- | ----------------------------------------- | ------------------------------------------------------------ |
| 2            | Customer_id | String    | Categorical (Nominal) - Unique Identifier | `'N205700', 'S930245', 'V58969'`                             |
| 3            | Interaction | String    | Categorical (Nominal) - Unique Identifier | `'22c7288a-2b36-4378-ae5b-144f4524075f', '095ee654-88b0-4999-978c-b273c08ea7d5', '1a47329c-3313-46e2-b758-767af46daee5'` |
| 4            | UID         | String    | Categorical (Nominal) - Unique Identifier | `'ee8e49f874e2d961e9cd94ef51ba5baf', 'f18c9bc8a2cfee0f2722cc725472962e', '3804f6fdadff70fdf7e6af6a50c615e0'` |

2   Customer_id

* This is a unique alphanumeric customer identifier string.
* It could be considered a categorical variable in a very general sense, but only if you consider each individual customer their own category.

3   Interaction
4   UID

* According to the data dictionary, these alphanumeric strings are "unique IDs related to patient transactions, procedures, and admissions"
* As with `Customer_id`, these could be considered categorical variables.

##### Customer Location

| Column Index | Column Name | Data Type                                  | Variable Type                                 | Samples                                                    |
| ------------ | ----------- | ------------------------------------------ | --------------------------------------------- | ---------------------------------------------------------- |
| 5            | City        | String                                     | Categorical (Nominal) - 6072 unique values    | `'Lenora', 'Thornton', 'West Danville'`                    |
| 6            | State       | String                                     | Categorical (Nominal) - 52 unique values      | `'MD', 'MI', 'CA'`                                         |
| 7            | County      | String                                     | Categorical (Nominal) - 1607 unique values    | 'Rutland', 'Tarrant', 'Ford'                               |
| 8            | Zip         | Originally an integer, converted to string | Categorical (Nominal) - 8612 unique values    | '03588', '76527', '90746'                                  |
| 9            | Lat         | Float                                      | Continuous interval data (latitude location)  | `37.85869, 39.08833, 30.14483`                             |
| 10           | Lng         | Float                                      | Continuous interval data (longitude location) | `-71.64837, -89.26033, -77.22221`                          |
| 11           | Population  | Integer                                    | Discrete ratio                                | `56790, 879, 879`                                          |
| 12           | Area        | String                                     | Categorical (Ordinal) - 3 unique categories   | `'Rural', 'Suburban', 'Urban'`                             |
| 13           | Timezone    | String                                     | Categorical (Nominal) - 26 unique categories  | `'America/Chicago', 'America/Chicago', 'America/New_York'` |

Residence location as listed on the billing statment.

* Although Zip is numeric and therefore imported as an integer by default, Zip should be stored as a string padded with zeros on the left side as some zip codes begin with leading zeros that the integer data type will not preserve.
  * The Zip examples above are post-conversion (note the leading zero)

* A case could be made for modifying Timezone to reflect an ordinal intervallic nature (perhaps by distance from GMT)
  * These could be encoded by signed numeric values relative to GMT (e.g. 'America/Adak' encoded as `-9`)

#### Customer Demographics

| Column Index | Column Name | Description                                             | Data Type             | Variable Type                                | Samples                                                      |
| ------------ | ----------- | ------------------------------------------------------- | --------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| 14           | Job         | Job of patient (or primary insurance holder)            | String                | Categorical (Nominal) - 639 unique values    | `'Pharmacist, community' 'Statistician' 'IT sales professional'` |
| 15           | Children    | Number of children in household                         | Float (includes NaNs) | Discrete Interval - values 0-10              | `1, nan,  3,  1,  2`                                         |
| 16           | Age         | Age in years (between  18-89, includes Nulls)           | Float (includes NaNs) | Discrete Interval (Age in Years)             | `nan, 35, nan, 81, 35`                                       |
| 17           | Education   | Highest level education attained                        | String                | Categorical (Ordinal) - 12 unique categories | `'Some College, 1 or More Years, No Degree', 'Bachelor's Degree'` |
| 18           | Employment  | Patient employment status                               | String                | Categorical (Nominal) - 5 unique categories  | `'Full Time', 'Part Time', 'Retired', 'Student', 'Unemployed'` |
| 19           | Income      | Annual income of Patient (or primary insurance holder)  | Float (includes NaNs) | Continuous ratio                             | `52120.99, 7874.03, 70030.91, nan, 70144.95`                 |
| 20           | Marital     | Marital status of patient (or primary insurance holder) | String                | Categorical (Nominal)                        | `'Divorced', 'Married', 'Never Married', 'Separated', 'Widowed'` |

#### Customer Physical Attributes & Health

| Column Index | Column Name        | Description                                                  | Data Type                    | Variable Type         | Samples                                                      |
| ------------ | ------------------ | ------------------------------------------------------------ | ---------------------------- | --------------------- | ------------------------------------------------------------ |
| 21           | Gender             | Customer self-identification                                 | String                       | Categorical (Nominal) | `'Female', 'Male', 'Prefer not to answer'`                   |
| 23           | VitD_levels        | Patient's vitamin D level (ng/mL)                            | Float                        | Continuous ratio      | `19.1532082, 14.08663461, 14.05481607 15.957204, 14.80686606` |
| 26           | VitD_supp          | Vitamin D supplements provided to patient                    | Integer                      | Discrete ratio        | `0, 1, 2, 3, 4, 5`                                           |
| 27           | Soft_drink         | Does patient habitually during more than three sodas a day?  | Categorical, (includes NaNs) | Categorical (Binary)  | `'No', 'Yes', 'No', 'No', NaN`                               |
| 29           | HighBlood          | Does the patient have high blood pressure?                   | Categorical                  | Categorical (Binary)  | `1, 1, 0, 0, 0`                                              |
| 30           | Stroke             | Patient has had a stroke in the past.                        | Categorical                  | Categorical (Binary)  | `0, 0, 0, 1, 0`                                              |
| 31           | Complication_risk  | Level of complication risk for the patient as assessed by a primary patient assessment | Categorical                  | Categorical (Ordinal) | `'Low', 'Medium', 'High'`                                    |
| 32           | Overweight         | Is the patient overweight                                    | Categorical (includes NaNs)  | Categorical (Binary)  | `0.0, 1.0, NaN`                                              |
| 33           | Arthritis          | Does the patient have arthritis                              | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 34           | Diabetes           | Does the patient have diabetes                               | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 35           | Hyperlipidemia     | Does the patient have Hyperlipidemia                         | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 36           | BackPain           | Does the patient have chronic back pain                      | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 37           | Anxiety            | Does the patient have an anxiety disorder                    | Categorical (includes NaNs)  | Categorical (Binary)  | `0.0, 1.0, NaN`                                              |
| 38           | Allergic_rhinitis  | Does the patient have allergic rhinitis                      | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 39           | Reflux_esophagitis | Does the patient have allergic rhinitis                      | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |
| 40           | Asthma             | Does the patient have asthma                                 | Categorical                  | Categorical (Binary)  | `0.0, 1.0`                                                   |

#### Customer Hospital Tracking

| Column Index | Column Name        | Description                                                  | Data Type             | Variable Type                               | Samples                                                      |
| ------------ | ------------------ | ------------------------------------------------------------ | --------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| 24           | Doc_visits         | Number of times the primary physician visited the patient during the initial hospitalization | Integer               | Discrete ratio - 9 unique values            | `1, 2, 3, 4, 5, 6, 7, 8, 9`                                  |
| 25           | Full_meals_eaten   | Number of full meals the patient ate (partial meals count as 0) | Integer               | Discrete ratio - 8 unique values            | `0, 1, 2, 3, 4, 5, 6, 7`                                     |
| 28           | Initial_admin      | Circumstances of initial hospital admission                  | String                | Categorical (Nominal) - 3 unique categories | `'Emergency Admission', 'Elective Admission',                  'Observation Admission'` |
| 41           | Services           | Primary service the patient received while hospitalized      | String                | Categorical (Nominal) - 4 unique categories | `'Blood Work', 'CT Scan', 'Intravenous', 'MRI'`              |
| 42           | Initial_days       | Duration of patient's initial hospital stay                  | Float (includes NaNs) | Continuous ratio data                       | `70.01384446, 7.4745906, 47.08194265, nan, 30.16130764`      |
| 43           | TotalCharge        | Amount charged to patient daily (total/stay duration)        | Float                 | Continuous ratio data                       | `13964.38675, 2631.975085, 2840.620344, 17892.9408, 2789.476853` |
| 44           | Additional_charges | Average amount charged for miscellaneous procedures, treatments, medicines, anesthesiology, etc. | Float                 | Continuous ratio data                       | `7911.926119, 12159.07509, 13818.9826, 7829.036633, 5991.504059` |

#### Survey responses

Responses to customer survey asking customers to rate the importance of each item on a scale of 1 to 8 (with 1 being most important and 8 being the least)

| Column Index | Column Name | Description                            | Data Type   | Variable Type         | Samples |
| ------------ | ----------- | -------------------------------------- | ----------- | --------------------- | ------- |
| 45           | Item1       | Timely admission                       | Categorical | Categorical (ordinal) |         |
| 46           | Item2       | Timely treatment                       | Categorical | Categorical (ordinal) |         |
| 47           | Item3       | Timely visits                          | Categorical | Categorical (ordinal) |         |
| 48           | Item4       | Reliability                            | Categorical | Categorical (ordinal) |         |
| 49           | Item5       | Options                                | Categorical | Categorical (ordinal) |         |
| 50           | Item6       | Hours of treatment                     | Categorical | Categorical (ordinal) |         |
| 51           | Item7       | Courteous staff                        | Categorical | Categorical (ordinal) |         |
| 52           | Item8       | Evidence of active listing from doctor | Categorical | Categorical (ordinal) |         |

#### Target

22  ReAdmis             10000 non-null  object
