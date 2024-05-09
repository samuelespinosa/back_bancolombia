class ImmutableModelMixin:
    def save(self, *args, **kwargs):
        if self.pk:
            raise NotImplementedError("Instances of this model are immutable and cannot be edited.")
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise NotImplementedError("Instances of this model are immutable and cannot be deleted.")

    def update(self, *args, **kwargs):
        raise NotImplementedError("Instances of this model are immutable and cannot be updated.")
