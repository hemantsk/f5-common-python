# coding=utf-8
#
# Copyright 2017 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""BIG-IP® auth module

REST URI
    ``http://localhost/mgmt/tm/auth/tacacs``

GUI Path
    ``System --> Users --> Authentication``

REST Kind
    ``tm:auth:tacacs:*``
"""

from f5.bigip.resource import Collection
from f5.bigip.resource import Resource
from f5.sdk_exception import InvalidName


class Tacacs_s(Collection):
    """BIG-IP® tacacs server collection"""
    def __init__(self, auth):
        super(Tacacs_s, self).__init__(auth)
        self._meta_data['allowed_lazy_attributes'] = [Tacacs]
        self._meta_data['attribute_registry'] = \
            {'tm:auth:tacacs:tacacsstate': Tacacs}


class Tacacs(Resource):
    """BIG-IP® tacacs server resource"""
    def __init__(self, tacacs_s):
        super(Tacacs, self).__init__(tacacs_s)
        self._meta_data['required_json_kind'] = 'tm:auth:tacacs:tacacsstate'

    def create(self, **kwargs):
        """name has to be system-auth, raise error if not named correctly"""
        if 'name' in kwargs:
            if kwargs['name'] != 'system-auth':
                raise InvalidName("Name must be 'system-auth'")
        return self._create(**kwargs)
