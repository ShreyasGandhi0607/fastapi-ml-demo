## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
````

### 2. Start FastAPI Backend

```bash
uvicorn main:app --reload
```

### 3. Start Streamlit Frontend

```bash
streamlit run app.py
```

---

## API Endpoint

**POST** `/predict`

**Request Body (JSON):**

```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response (JSON):**

```json
{
  "predicted_category": "high"
}
```

---

## Project Structure

```
ml-model-inferencing/
├── app.py
├── main.py
├── model/
│   └── model.pkl
├── data/
│   └── insurance.csv
├── notebook/
│   └── fastapi_ml_model.ipynb
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```


