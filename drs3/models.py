from datetime import datetime

from ghga_service_chassis_lib.object_storage_dao import (
    ObjectIdValidationError,
    validate_object_id,
)
from pydantic import UUID4, BaseModel, validator


class DrsObjectExternal(BaseModel):
    """
    A model for communicating DrsObject metadata to external services.
    This is missing the internal objerct ID `id` as well as the registration date as
    this information shouldn't be shared with other services.
    """

    external_id: str
    md5_checksum: str
    size: int

    # pylint: disable=no-self-argument,no-self-use
    @validator("external_id")
    def check_external_id(cls, value: str):
        """Checks if the external_id is valid for use as a s3 object id."""

        try:
            validate_object_id(value)
        except ObjectIdValidationError as error:
            raise ValueError(
                f"External ID '{value}' cannot be used as a (S3) object id."
            ) from error

        return value

    class Config:
        """Additional pydantic configs."""

        orm_mode = True


class DrsObjectComplete(DrsObjectExternal):
    """
    A model for describing the complete DrsObject metadata.
    Only intended for service-internal use.
    """

    id: UUID4
    registration_date: datetime
