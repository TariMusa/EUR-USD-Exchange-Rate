EUR/USD Exchange Rate Prediction Model

￼
This project aims to predict the EUR/USD exchange rate using a machine learning model developed in Python. Leveraging TensorFlow, the model achieves a Mean Squared Error (MSE) of 0.0014, demonstrating high accuracy in predicting exchange rates.
Key Features
	•	Machine Learning Approach: Utilizes TensorFlow for model development, allowing for effective training and prediction of exchange rate fluctuations.
	•	Data Collection and Cleaning: Conducted extensive data wrangling in R, primarily acquiring data through an API connection from the World Bank data site.

Technologies Used
	•	Python
	•	TensorFlow
	•	RStudio
	•	GeoPandas
	•	Matplotlib
	•	Jupyter Notebook

Getting Started
To run the project locally, follow these steps:
	1	Clone the repository:  https://github.com/TariMusa/TariMusa 
	2	Install required libraries: Make sure you have Python and pip installed. Then, install the necessary packages:  pip install pandas numpy tensorflow scikit-learn matplotlib pandas
	3	Data Preparation: Cleaned Dataset downloadable in Github repository, also available the R Code used to prepare the data, alternatively:
	⁃	Download the required datasets:
	⁃	https://data.ecb.europa.eu/
	⁃	https://www.policyuncertainty.com/all_country_data.html - https://www.policyuncertainty.com/media/All_Country_Data.xlsx
	⁃	https://www.macrotrends.net/
	⁃	https://fred.stlouisfed.org/series/M2SL
	⁃	https://fred.stlouisfed.org/series/EUEPUINDXM
	⁃	Sample  World Bank API python request code in repository.
	⁃	
	⁃	Run the R script for data cleaning: Rscript data_cleaning.R
	1	 Run the model: Execute the main script:
	 
	2	Visualizations: Open the Jupyter Notebook to explore the visualizations.
Results
The model successfully predicts the EUR/USD exchange rate with a Mean Squared Error of 0.0014. In practical terms, this means our predictions are typically within 0.037 (square root of 0.0014) of the actual exchange rate.

Model Details
Our model uses a Long Short-Term Memory (LSTM) neural network architecture, which is particularly well-suited for time series prediction tasks like exchange rate forecasting. The model takes into account historical exchange rates, as well as relevant economic indicators from both the Eurozone and the United States.

Data Sources
We primarily use data from the World Bank, accessed through their API and datasets from FRED. The model is only for education purposes and should not be used for trading, consistent with the terms of use of these datasets.
Contributing
We welcome contributions to improve the model's accuracy or extend its capabilities.
Contributions
	•	Collaborated with a team to enhance the model's accuracy through testing and validation.
	•	Shared knowledge and best practices to foster a collaborative environment.
License
This project is not licensed.
Acknowledgments
	•	World Bank for providing the data
	•	TensorFlow team for their excellent machine learning framework
	•	All contributors who have helped to improve this project

