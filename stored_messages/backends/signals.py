from django.dispatch import Signal

# providing_args=["user", "message"]
inbox_stored = Signal()
# providing_args = ["user", "message_id"]
inbox_deleted = Signal()
# providing_args = ["user"]
inbox_purged = Signal()
# providing_args=["user", "message"]
archive_stored = Signal()
