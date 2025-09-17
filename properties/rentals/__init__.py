"""
Rental property management module for the GreenTech Africa platform.
"""

# Import models to make them available when importing the rentals package
from .models import (
    RentalProperty,
    LeaseAgreement,
    MaintenanceRequest,
    Payment,
    LeaseType,
    PaymentFrequency,
    MaintenanceStatus,
    MaintenancePriority
)

# Import serializers
from .serializers import (
    RentalPropertySerializer,
    LeaseAgreementSerializer,
    MaintenanceRequestSerializer,
    PaymentSerializer,
    LeaseAgreementCreateSerializer
)

# Import views
from .views import (
    RentalPropertyViewSet,
    LeaseAgreementViewSet,
    MaintenanceRequestViewSet,
    PaymentViewSet
)

# Import permissions
from .permissions import (
    IsPropertyOwnerOrAdmin,
    IsTenantOrAdmin,
    IsMaintenanceStaffOrAdmin,
    CanManageLease,
    CanManagePayment
)

__all__ = [
    # Models
    'RentalProperty',
    'LeaseAgreement',
    'MaintenanceRequest',
    'Payment',
    'LeaseType',
    'PaymentFrequency',
    'MaintenanceStatus',
    'MaintenancePriority',
    
    # Serializers
    'RentalPropertySerializer',
    'LeaseAgreementSerializer',
    'MaintenanceRequestSerializer',
    'PaymentSerializer',
    'LeaseAgreementCreateSerializer',
    
    # Views
    'RentalPropertyViewSet',
    'LeaseAgreementViewSet',
    'MaintenanceRequestViewSet',
    'PaymentViewSet',
    
    # Permissions
    'IsPropertyOwnerOrAdmin',
    'IsTenantOrAdmin',
    'IsMaintenanceStaffOrAdmin',
    'CanManageLease',
    'CanManagePayment'
]
