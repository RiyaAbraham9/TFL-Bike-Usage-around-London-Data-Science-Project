# TFL-Bike-Usage-around-London-Data-Science-Project
This project analyses TfL cycling volume data from three selected monitoring sites across London (ML0012, ML0036, ML0040) to investigate usage patterns and suggest possible peak charging periods.
The analysis follows a structured, step-by-step approach, from data aggregation to visualisation and machine learning modelling using a Decision Tree Regressor. The results aim to answer the question:
"If TfL were to introduce a charging regime for peak cycle traffic, when should it apply?"

## Objectives
- Aggregate TfL cycle traffic data for three specific monitoring sites.
- Explore traffic patterns by time of day and overall trends.
- Calculate average usage per timeslot to simplify visual interpretation.
- Apply machine learning to identify potential peak periods for charging.
- Assess whether the results could realistically inform a TfL charging policy.

## Tools and Technologies
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- Jupyter Notebook for analysis and visualisation
- TfL Excel/CSV datasets for real-time and historical bike usage
- Git & GitHub for version control

## Dataset
Data Sourced from (Transport for London open data)[https://cycling.data.tfl.gov.uk/]

## Methodology
### Step 1 - Data Preperation:
- Selected monitoring stations: ML0012, ML0036, ML0040.
- Combined CSV files from 2014 Q1 to 2019 Q4 into a single dataset.
- Added a Quarter column (YYYYQX format) and a row counter.
- Removed irrelevant columns (Drop1, Drop2).
- Created a Full_time column by merging Date + Time.
- Output: CycleData.xlsx
  <img width="965" height="102" alt="image" src="https://github.com/user-attachments/assets/51b136a4-dfef-46b7-8baf-79065a0137dd" />
### Step 2 - Data Filtering and visualisation:
Generated Seaborn scatter plots for:
- All cycles at a station
- Private cycles only
- Filtered by direction (Inbound/Outbound)
Options for plotting:
- X-axis: Time or Full_time
- Hue (colour): Weather, Direction, or Mode
  <img width="683" height="182" alt="image" src="https://github.com/user-attachments/assets/b6c55ecd-80a1-4fba-b23d-3f48bf650e54" />
  - This plot was generated for station ML0036, direction eastbound, restricted to private cycles only, and hue is determined by weather conditions.
### Step 3 - Aggregation
- Used groupby to calculate average number of cycles per timeslot regardless of date.
- Simplified scatterplots to one point per time of day, making peak periods clear.
  <img width="684" height="199" alt="image" src="https://github.com/user-attachments/assets/907bd1cb-a171-457e-8f56-8fe46992f5a8" />
  - This plot was generated for station ML0036 and direction eastbound just like previous plot. But this is much simpler as it is taking the avergae of each time, making it easier to view trends.
### Step 4 - Machine Learning
- Restricted to Private cycles only.
- Converted Time to datetime format (RealTime) for modelling.
- Split data into train and test sets (random_state=1).
- Fitted a DecisionTreeRegressor to predict usage by time.
- Predicted values overlaid on scatterplot to highlight peak times.
<img width="686" height="369" alt="image" src="https://github.com/user-attachments/assets/21e3b531-0c2d-4d8b-a2f0-39ad3fa36a46" />
<img width="689" height="362" alt="image" src="https://github.com/user-attachments/assets/258f9acf-8a80-4b6b-82fc-32a8e138630a" />

## Key Findings
- Morning peak: ~08:00–09:00, strong commuter traffic.
- Evening peak: ~17:00–18:30, post-work travel.
- Weekends show flatter demand curves, with midday leisure peaks.
- Weather impacts: Dry days see up to 2× more trips than wet days.
- Decision tree modelling successfully highlights two daily charging windows for maximum revenue with minimal disruption.

## Future Improvements
- Create a streamlit dashboard for better visualisations
- Use other machine learning models such as XG Boost for more accurate results.




