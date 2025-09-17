# Import models to make them available in the rentals.models namespace
from .rental_application import (
    RentalApplication, ApplicationDocument, TenantScreening,
    RentalApplicationStatus, ApplicationDocumentType, IncomeType
)

__all__ = [
    'RentalApplication', 'ApplicationDocument', 'TenantScreening',
    'RentalApplicationStatus', 'ApplicationDocumentType', 'IncomeType'
]
