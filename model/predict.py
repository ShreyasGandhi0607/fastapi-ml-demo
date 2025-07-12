import pickle 
import pandas as pd


# Import ML model
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0' # in ideal scenario we use ml flow to check the model version

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()


def predict_output(user_input : dict):

    input_df = pd.DataFrame([user_input])

    # predict the class
    predicted_class = model.predict(input_df)[0]

    # get probablities of all the classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # create a mapping  : {class_name : probablity}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
