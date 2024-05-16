# Report Notes

## Part I: Research Question

### A: Research Question

Which features in the provided dataset are most useful for accurately predicting whether a patient will be readmitted within a month of release?

### B: Describe all Variables

The column indices indicate the columns as they are imported from the original `.csv` into Pandas. As such, they are zero-indexed and include the leftmost value from the original `.csv`.

As some columns have logical groupings, the indexes may appear slightly out of order.

#### Indexing variables:

| Column Index | Column Name | Data Type | Variable Type    | Samples      |
| ------------ | ----------- | --------- | ---------------- | ------------ |
| 0            | Unnamed: 0  | Integer   | Sequential Index | `1, 2, 3, 4` |
| 1            | CaseOrder   | Integer   | Sequential index | `1, 2, 3, 4` |

Both of these varaibles contain a sequential index (from 1 to 10000) and are duplicates of one another. They are stored as integers, and only serve to maintain the sequential order of records. As the Pandas DataFrame data structure provides a numeric index by default, these features can be removed.

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
| 5            | City        | String                                     | Categorical (Nominal)                         | `'Lenora', 'Thornton', 'West Danville'`                    |
| 6            | State       | String                                     | Categorical (Nominal)                         | `'MD', 'MI', 'CA'`                                         |
| 7            | County      | String                                     | Categorical (Nominal)                         | 'Rutland', 'Tarrant', 'Ford'                               |
| 8            | Zip         | Originally an integer, converted to string | Categorical (Nominal)                         | '03588', '76527', '90746'                                  |
| 9            | Lat         | Float                                      | Continuous interval data (latitude location)  | `37.85869, 39.08833, 30.14483`                             |
| 10           | Lng         | Float                                      | Continuous interval data (longitude location) | `-71.64837, -89.26033, -77.22221`                          |
| 11           | Population  | Integer                                    | Discrete ratio                                | `56790, 879, 879`                                          |
| 12           | Area        | String                                     | Categorical (Ordinal)                         | `'Rural', 'Suburban', 'Urban'`                             |
| 13           | Timezone    | String                                     | Categorical (Nominal)                         | `'America/Chicago', 'America/Chicago', 'America/New_York'` |

Residence location as listed on the billing statment.

* Although Zip is numeric and therefore imported as an integer by default, Zip should be stored as a string padded with zeros on the left side as some zip codes begin with leading zeros that the integer data type will not preserve.
  * The Zip examples above are post-conversion (note the leading zero)

* A case could be made for modifying Timezone to reflect an ordinal intervallic nature (perhaps by distance from GMT)
  * These could be encoded by signed numeric values relative to GMT (e.g. 'America/Adak' encoded as `-9`)

#### Customer Demographics

| Column Index | Column Name | Data Type             | Variable Type                    | Samples                                                      |
| ------------ | ----------- | --------------------- | -------------------------------- | ------------------------------------------------------------ |
| 14           | Job         | String                | Categorical (Nominal)            | `'Pharmacist, community' 'Statistician' 'IT sales professional'` |
| 15           | Children    | Float (includes NaNs) | Discrete Interval                | `1, nan,  3,  1,  2`                                         |
| 16           | Age         | Float (includes NaNs) | Discrete Interval (Age in Years) | `nan, 35, nan, 81, 35`                                       |
| 17           | Education   | String                | Categorical (Ordinal)            | `'Some College, 1 or More Years, No Degree', 'Bachelor's Degree'` |
| 18           | Employment  | String                | Categorical (Nominal)            | `'Full Time', 'Part Time', 'Retired', 'Student', 'Unemployed'` |
| 19           | Income      | Float                 | Continuous ratio                 | `52120.99, 7874.03, 70030.91, nan, 70144.95`                 |
| 20           | Marital     | String                | Categorical (Nominal)            | `'Divorced', 'Married', 'Never Married', 'Separated', 'Widowed'` |



#### Customer Physical Attributes & Health

| Column Index | Column Name        | Description                                                  | Data Type   | Variable Type                         | Samples                                                      |
| ------------ | ------------------ | ------------------------------------------------------------ | ----------- | ------------------------------------- | ------------------------------------------------------------ |
| 21           | Gender             | Customer self-identification                                 | String      | Categorical (Nominal)                 | `'Female', 'Male', 'Prefer not to answer'`                   |
| 23           | VitD_levels        | Patient's vitamin D level (ng/mL)                            | Float       | Continuous ratio                      | `19.1532082, 14.08663461, 14.05481607 15.957204, 14.80686606` |
| 26           | VitD_supp          | Vitamin D suppliments provided to patient                    | Integer     | Discrete ratio                        | `0, 1, 2, 3, 4, 5`                                           |
| 27           | Soft_drink         | Does patitnet habitually dring more than three sodas a day?  | Categorical | Categorical (Binary) - includes Nulls | `'No', 'Yes', 'No', 'No', NaN`                               |
| 29           | HighBlood          | Does the patient have high blood pressure?                   | Categorical | Categorical (Binary)                  | `1, 1, 0, 0, 0`                                              |
| 30           | Stroke             | Patient has had a stroke in the past.                        | Categorical | Categorical (Binary)                  | `0, 0, 0, 1, 0`                                              |
| 31           | Complication_risk  | level of complication risk for the patient as assessed by a primary patient assessment | Categorical | Categorical (Ordinal)                 | `'Low', 'Medium', 'High'`                                    |
| 32           | Overweight         |                                                              |             |                                       |                                                              |
| 33           | Arthritis          |                                                              |             |                                       |                                                              |
| 34           | Diabetes           |                                                              |             |                                       |                                                              |
| 35           | Hyperlipidemia     |                                                              |             |                                       |                                                              |
| 36           | BackPain           |                                                              |             |                                       |                                                              |
| 37           | Anxiety            |                                                              |             |                                       |                                                              |
| 38           | Allergic_rhinitis  |                                                              |             |                                       |                                                              |
| 39           | Reflux_esophagitis |                                                              |             |                                       |                                                              |
| 40           | Asthma             |                                                              |             |                                       |                                                              |



21  Gender              10000 non-null  object

23  VitD_levels         10000 non-null  float64 

26  VitD_supp           10000 non-null  int64 
27  Soft_drink          7533 non-null   object

29  HighBlood           10000 non-null  object
30  Stroke              10000 non-null  object
31  Complication_risk   10000 non-null  object 
32  Overweight          9018 non-null   float64
33  Arthritis           10000 non-null  object
34  Diabetes            10000 non-null  object
35  Hyperlipidemia      10000 non-null  object
36  BackPain            10000 non-null  object
37  Anxiety             9016 non-null   float64
38  Allergic_rhinitis   10000 non-null  object
39  Reflux_esophagitis  10000 non-null  object
40  Asthma              10000 non-null  object

#### Hospital Tracking

28  Initial_admin       10000 non-null  object

24  Doc_visits          10000 non-null  int64
25  Full_meals_eaten    10000 non-null  int64 

41  Services            10000 non-null  object
42  Initial_days        8944 non-null   float64
43  TotalCharge         10000 non-null  float64
44  Additional_charges  10000 non-null  float64

#### Survey responses

45  Item1               10000 non-null  int64
46  Item2               10000 non-null  int64 
47  Item3               10000 non-null  int64 
48  Item4               10000 non-null  int64 
49  Item5               10000 non-null  int64 
50  Item6               10000 non-null  int64 
51  Item7               10000 non-null  int64
52  Item8               10000 non-null  int64

#### Target

22  ReAdmis             10000 non-null  object
