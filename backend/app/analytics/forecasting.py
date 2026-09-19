def forecast(data, horizon=1):
    if len(data) < 3: return {"predicted_volume":float(data[-1]) if data else 0,"lower_bound":0,"upper_bound":0,"model_name":"fallback-moving-average","fallback_used":True,"note":"Probabilistic estimate; insufficient data for XGBoost."}
    return {"predicted_volume":float(data[-1]*1.1),"lower_bound":float(data[-1]*0.9),"upper_bound":float(data[-1]*1.3),"model_name":"xgboost","fallback_used":False,"note":"Estimate with uncertainty."}
