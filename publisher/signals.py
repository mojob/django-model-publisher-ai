from django.dispatch import Signal


def publisher_pre_delete(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if not instance:
        return

    # If the draft record is deleted, the published object should be as well
    if instance.is_draft and instance.publisher_linked:
        instance.unpublish()


# Sent when a model is about to copy draft data into the linked model (the draft is sent).
publisher_pre_submit_changes = Signal()

# Sent when a model changes is submitted to the linked model (the draft is sent).
publisher_post_submit_changes = Signal()

# Sent when a model is about to be published (the draft is sent).
publisher_pre_publish = Signal()


# Sent when a model is being published, before the draft is saved (the draft is sent).
publisher_publish_pre_save_draft = Signal()


# Sent when a model is published (the draft is sent)
publisher_post_publish = Signal()


# Sent when a model is about to be unpublished (the draft is sent).
publisher_pre_unpublish = Signal()


# Sent when a model is unpublished (the draft is sent).
publisher_post_unpublish = Signal()
