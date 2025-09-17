""
Notifications app for the Green Tech Africa platform.

This app handles all notification-related functionality including:
- Email, SMS, push, and in-app notifications
- Notification templates
- User notification preferences
- Notification delivery and tracking
"""

# Make the following available at the package level
from .models import (
    Notification, NotificationTemplate, UserNotificationPreference,
    NotificationType, NotificationStatus, NotificationPriority
)
from .services import NotificationService, notify_user, notify_users

__all__ = [
    'Notification', 'NotificationTemplate', 'UserNotificationPreference',
    'NotificationType', 'NotificationStatus', 'NotificationPriority',
    'NotificationService', 'notify_user', 'notify_users'
]
