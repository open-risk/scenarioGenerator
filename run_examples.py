# -*- coding: utf-8 -*-

# (c) 2019 - 2024 Open Risk (https://www.openriskmanagement.com), all rights reserved
#
# scenarioGenerator is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of scenarioGenerator. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.


""" Run all examples to test that everything is working with the current version

"""

from scenarioGenerator import source_path

examples_path = source_path + "examples/python/"
filelist = ['basic']

if __name__ == '__main__':

    for example in filelist:
        try:
            print('\nExecuting example file: ', example.upper())
            print('-----------------------' + '-' * len(example))
            exec(open(examples_path + example + ".py").read())
        except:
            print('**********************' + '*' * len(example))
            print('ERROR in example file', example)
            print('**********************' + '*' * len(example))
