# Copyright 2021 Universität Tübingen, DKFZ and EMBL
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Config Parameter Modeling and Parsing"""

from typing import Literal, Optional

from ghga_service_chassis_lib.api import ApiConfigBase
from ghga_service_chassis_lib.config import config_from_yaml
from ghga_service_chassis_lib.postgresql import PostgresqlConfigBase
from ghga_service_chassis_lib.pubsub import PubSubConfigBase
from ghga_service_chassis_lib.s3 import S3ConfigBase

LogLevel = Literal["critical", "error", "warning", "info", "debug", "trace"]


@config_from_yaml(prefix="drs3")
class Config(ApiConfigBase, PubSubConfigBase, PostgresqlConfigBase, S3ConfigBase):
    """Config parameters and their defaults."""

    # Config parameter needed for:
    #   - the rabbitmq server
    #   - the web server
    #   - the PostgreSQL database
    #   - the S3 interface
    # are inherited.

    # Following config parameter are specifically needed for drs3:
    service_name: str = "drs3"

    api_route: str = "/ga4gh/drs/v1"
    drs_self_url: str = "drs://localhost:8080/"
    custom_spec_url: Optional[str] = None

    topic_name_download_requested: str = "download_request"

    s3_outbox_bucket_id: str


CONFIG = Config()
