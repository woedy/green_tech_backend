"""
Construction models package.
"""

# Import all models to ensure they are registered with Django
from .quote import Quote, QuoteItem, QuoteChangeLog, QuoteStatus
from .project import (
    Project, 
    ProjectStatus, 
    ProjectPhase, 
    ProjectMilestone, 
    MilestoneStatus
)

# Make models available at the package level
__all__ = [
    # Quote models
    'Quote',
    'QuoteItem',
    'QuoteChangeLog',
    'QuoteStatus',
    
    # Project models
    'Project',
    'ProjectStatus',
    'ProjectPhase',
    'ProjectMilestone',
    'MilestoneStatus',
]
