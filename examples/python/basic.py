# encoding: utf-8

# (c) 2019 - 2023 Open Risk, all rights reserved
#
# scenarioGenerator is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of correlationMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.


"""
Basic Example


"""

import json

import numpy as np

import scenarioGenerator as sg
from scenarioGenerator import source_path

input_dataset_path = source_path + "datasets/"
output_dataset_path = source_path + "datasets/"

print("> Load a correlation matrix")
input_filename = output_dataset_path + 'correlation_data.json'
Omega = np.array(json.load(open(input_filename))['correlation_matrix'])
print(Omega)

myESG = sg.scenarioGenerator(dim=Omega.shape[0], Omega=Omega)
myESG.decompose()
print(np.dot(myESG.L, myESG.L.T))
