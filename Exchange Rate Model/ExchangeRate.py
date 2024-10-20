import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error



data = pd.read_csv('Exchange_clean.csv')
print(data.head())  # View the first few rows of the dataset
# Use forward fill (fill) directly
data = data.bfill()
data = data.dropna()
print(data.head())

print(data.isnull().sum())

X = data[['US_Supply', 'ECB_Supply', 'US_EPU', 'ECB_EPU', 'FDI_Euro area_EMU',
          'FDI_United States_USA', 'GDP_Euro area_EMU', 'GDP_United States_USA',
          'Infl_Euro area_EMU', 'Infl_United States_USA', 'BOP_Euro area_EMU',
          'BOP_United States_USA', 'UnEmp_Euro area_EMU', 'UnEmp_United States_USA',
          'HI_Eurozone', 'HI_USA']]
y = data['hist_rate']

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.Input(shape=(X_train.shape[1],)),  # Use Input layer to define input shape
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer with one neuron for regression
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.show()

test_loss, test_mae = model.evaluate(X_test, y_test)
print(f'Test MAE: {test_mae:.4f}')

y_pred = model.predict(X_test)

# Plot Actual vs Predicted Exchange Rates
plt.scatter(range(len(y_test)), y_test, label='Actual', color='blue')
plt.scatter(range(len(y_pred)), y_pred, label='Predicted', color='red')

plt.xlabel('Index')  # Label for the x-axis
plt.ylabel('Exchange Rate')  # Label for the y-axis
plt.title('Actual vs Predicted Exchange Rate')

plt.legend()
plt.show()

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.4f}')












