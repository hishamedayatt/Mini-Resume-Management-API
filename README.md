# Mini Resume Management API

A FastAPI-based REST API for managing candidate resumes with CRUD operations and filtering capabilities.

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd mini_resume_management
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, access the interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health Check
```
GET /health
```
Returns the API health status.

### Upload Candidate
```
POST /candidates/
```
Upload a new candidate with resume file.

**Form Data:**
- `full_name` (string): Candidate's full name
- `dob` (date): Date of birth (YYYY-MM-DD)
- `contact_number` (string): Phone number
- `contact_address` (string): Address
- `education` (string): Educational background
- `graduation_year` (integer): Year of graduation
- `years_experience` (integer): Years of work experience
- `skills` (string): Comma-separated skills
- `resume` (file): Resume file (PDF, DOC, or DOCX)

**Response:**
```json
{
  "message": "Candidate uploaded successfully",
  "candidate_id": "uuid"
}
```

### List Candidates
```
GET /candidates/
```
Retrieve all candidates with optional filters.

**Query Parameters:**
- `skill` (optional): Filter by skill
- `min_experience` (optional): Minimum years of experience
- `graduation_year` (optional): Filter by graduation year

**Response:**
```json
[
  {
    "id": "uuid",
    "full_name": "John Doe",
    "dob": "1990-01-01",
    "contact_number": "+1234567890",
    "contact_address": "123 Main St",
    "education": "Bachelor's in Computer Science",
    "graduation_year": 2012,
    "years_experience": 5,
    "skills": ["Python", "FastAPI", "Docker"],
    "resume_filename": "john_doe_resume.pdf"
  }
]
```

### Get Candidate by ID
```
GET /candidates/{candidate_id}
```
Retrieve a specific candidate's details.

**Response:**
```json
{
  "id": "uuid",
  "full_name": "John Doe",
  "dob": "1990-01-01",
  "contact_number": "+1234567890",
  "contact_address": "123 Main St",
  "education": "Bachelor's in Computer Science",
  "graduation_year": 2012,
  "years_experience": 5,
  "skills": ["Python", "FastAPI", "Docker"],
  "resume_filename": "john_doe_resume.pdf"
}
```

### Delete Candidate
```
DELETE /candidates/{candidate_id}
```
Delete a candidate record.

**Response:**
```json
{
  "message": "Candidate deleted successfully"
}
```

## Project Structure

```
mini_resume_management/
├── app/
│   ├── api/
│   │   └── candidates.py       # Candidate endpoints
│   ├── schemas/
│   │   └── candidate_schema.py # Pydantic models
│   └── storage/
│       └── candidate_storage.py # In-memory storage
├── main.py                      # Application entry point
├── requirements.txt             # Dependencies
└── README.md                    # Documentation
```



## Notes

- This application uses in-memory storage. Data will be lost when the server restarts.
- Resume files are validated but not actually stored in this implementation.
- For production use, consider implementing persistent storage and actual file storage.


