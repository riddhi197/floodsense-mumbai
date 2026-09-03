import pickle
import os

base_dir = r"C:\Users\User\.gemini\antigravity\scratch\floodsense_mumbai"

# Inspect Mumbai Model
mumbai_path = os.path.join(base_dir, 'flood_model.pkl')
if os.path.exists(mumbai_path):
    with open(mumbai_path, 'rb') as f:
        mumbai_model = pickle.load(f)
    print("Mumbai Model Type:", type(mumbai_model))
    if hasattr(mumbai_model, 'feature_names_in_'):
        print("Mumbai Features:", mumbai_model.feature_names_in_)

# Inspect Konkan Model
konkan_path = os.path.join(base_dir, 'floodsense_final_model.pkl')
if os.path.exists(konkan_path):
    with open(konkan_path, 'rb') as f:
        konkan_bundle = pickle.load(f)
    print("\nKonkan Bundle Keys:", konkan_bundle.keys())
    print("Konkan Model Type:", type(konkan_bundle['model']))
    print("Konkan Features:", konkan_bundle['features'])
    
    # Check stacking estimators
    model = konkan_bundle['model']
    if hasattr(model, 'estimators_'):
        print("Stacking Estimators:", [type(e) for e in model.estimators_])
        print("Stacking Final Estimator:", type(model.final_estimator_))
