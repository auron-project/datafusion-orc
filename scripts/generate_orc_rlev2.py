# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import pyorc

dir = "tests/basic/data"

schema = pyorc.Struct(values=pyorc.SmallInt())

writer = pyorc.Writer(
    open(f"{dir}/pyorc_rlev2_patchedbase.orc", "wb"),
    schema,
)

for value in [
    -480,
    -480,
    -420,
    -420,
    -420,
    -360,
    -480,
    -420,
    -420,
    -420,
    -25080,
    -480,
    -420,
    -420,
    31080,
    0,
    0,
    -360,
    60,
    0,
    180,
    0,
    -240,
    -480,
    60,
    -480,
    -480,
    -180,
    -300,
    120,
    60,
]:
    writer.write((value,))

writer.close()
