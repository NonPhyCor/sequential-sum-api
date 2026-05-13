# Sequential Sum API Project

A secure RESTful API built with Python and FastAPI that calculates the sequential sum of a list of numbers.

---

## 1. Setup Instructions

**Prerequisites:**
* Python
* Git

**Step 1: Clone the repository**
```bash
git clone https://github.com/NonPhyCor/sequential-sum-api.git
cd sequential-sum-api
```

**Step 2: Create and activate virtual environment**
*For Mac/Linux:*
```bash
python3.12 -m venv venv
source venv/bin/activate
```
*For Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run the API Server**
```bash
python -m uvicorn main:app --reload
```
The API will be available locally at `http://127.0.0.1:8000`.

---

## 2. API Documentation

### Endpoint
`POST /sum`

### Authentication
This API uses Header-based API Key authentication.
* **Header Key:** `x-api-key`
* **Header Value:** `super_secret_key_123`

### Request Payload
The endpoint expects a JSON body containing a list of numerical values.
```json
{
  "numbers": [5, 10, 15]
}
```

---

## 3. Usage & Testing

You can test the endpoints using `curl` from your terminal.

**Example 1: Successful Request (200 OK)**
```bash
curl -X POST [http://127.0.0.1:8000/sum](http://127.0.0.1:8000/sum) \
     -H "Content-Type: application/json" \
     -H "x-api-key: super_secret_key_123" \
     -d '{"numbers": [5, 10, 15]}'
```
*Expected output:* `{"total": 30.0}`

**Example 2: Missing or Invalid API Key (401 Unauthorized)**
```bash
curl -X POST [http://127.0.0.1:8000/sum](http://127.0.0.1:8000/sum) \
     -H "Content-Type: application/json" \
     -H "x-api-key: wrong_key" \
     -d '{"numbers": [1, 2, 3]}'
```
*Expected output:* `{"detail": "Invalid or missing API Key"}`