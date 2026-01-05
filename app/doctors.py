from fastapi import APIRouter

router = APIRouter()

DOCTORS = [
    {
        "id": "doc1",
        "name": "Dr. Ahmed Khan",
        "specialty": "General Physician",
        "fee_pkr": 300,
        "languages": ["English", "Urdu"],
        "city": "Islamabad"
    },
    {
        "id": "doc2",
        "name": "Dr. Sara Ali",
        "specialty": "Internal Medicine",
        "fee_pkr": 500,
        "languages": ["Urdu"],
        "city": "Rawalpindi"
    }
]

@router.get("/doctors")
def list_doctors():
    return DOCTORS
