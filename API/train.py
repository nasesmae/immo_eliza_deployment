import joblib
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import xgboost as xgb

def train():
    # Load the data
    data = pd.read_csv("data/properties.csv")

    # Define features to use
    num_features = [
        "construction_year",
        "total_area_sqm",
        "surface_land_sqm",
        "nbr_frontages",
        "nbr_bedrooms",
        "terrace_sqm",
        "garden_sqm",
        "zip_code",
    ]

    fl_features = [
        "fl_terrace",
        "fl_open_fire",
        "fl_swimming_pool",
        "fl_garden",
        "fl_double_glazing",
    ]

    cat_features = [
        "property_type",
        "subproperty_type",
        "locality",
        "kitchen_clusterized",
        "state_building_clusterized",
        "epc",
    ]

    # Split the data into features and target
    X = data[num_features + fl_features + cat_features]
    y = data["price"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=405
    )

    # Impute numerical features missing values using SimpleImputer
    imputer = SimpleImputer(strategy="mean")
    X_train[num_features] = imputer.fit_transform(X_train[num_features])
    X_test[num_features] = imputer.transform(X_test[num_features])

    # Convert categorical columns with one-hot encoding using OneHotEncoder
    enc = OneHotEncoder()
    X_train_cat = enc.fit_transform(X_train[cat_features]).toarray()
    X_test_cat = enc.transform(X_test[cat_features]).toarray()

    # Combine the numerical and one-hot encoded categorical columns
    X_train_prepared = pd.concat(
        [
            pd.DataFrame(X_train[num_features + fl_features].reset_index(drop=True)),
            pd.DataFrame(X_train_cat, columns=enc.get_feature_names_out()),
        ],
        axis=1,
    )

    X_test_prepared = pd.concat(
        [
            pd.DataFrame(X_test[num_features + fl_features].reset_index(drop=True)),
            pd.DataFrame(X_test_cat, columns=enc.get_feature_names_out()),
        ],
        axis=1,
    )

    # Instantiate and train the XGBoost Regressor
    model = xgb.XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=555)
    model.fit(X_train_prepared, y_train)

    # Evaluate the model
    y_pred_train = model.predict(X_train_prepared)
    y_pred_test = model.predict(X_test_prepared)

    print("Train set R² score:", r2_score(y_train, y_pred_train))
    print("Test set R² score:", r2_score(y_test, y_pred_test))
    print("Train set MAE:", mean_absolute_error(y_train, y_pred_train))
    print("Test set MAE:", mean_absolute_error(y_test, y_pred_test))
    print("Train set MSE:", mean_squared_error(y_train, y_pred_train))
    print("Test set MSE:", mean_squared_error(y_test, y_pred_test))

    # Save the model and preprocessing objects
    artifacts = {
        "features": {
            "num_features": num_features,
            "fl_features": fl_features,
            "cat_features": cat_features,
        },
        "imputer": imputer,
        "enc": enc,
        "model": model,
    }
    
    joblib.dump(artifacts, "API/XGBoost_artifacts.pkl")

# Ensure you have the correct file path and data format for 'data/properties.csv'
train()
