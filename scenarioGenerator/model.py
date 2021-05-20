# encoding: utf-8

# (c) 2019 Open Risk (https://www.openriskmanagement.com)
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

""" This module provides the key scenarioGenerator classes


"""

import numpy as np


class scenarioGenerator:
    """ The _`scenarioGenerator` object implements a scenario generator
    Currently the only class of models supported is are Vector Autoregressions (VAR)

    """

    def __init__(self, dim=1, A=None, Omega=None, **kwargs):

        """ Create a new Scenario Generator.



        """

        if A is not None:
            # Initialize autoregression with given matrix
            self.A = np.asarray(A)
        else:
            self.A = np.ones(dim)

        if Omega is not None:
            # Initialize correlation with given matrix
            self.Omega = np.asarray(Omega)
        else:
            self.Omega = np.ones(dim)

        # temporary dimension assignment (must validated for squareness)
        self.dimension = dim
        self.L = np.asarray(Omega)

    def decompose(self):
        self.L = np.linalg.cholesky(self.Omega)
        print(self.L)

    def simulate(self, periods):
        """
        Simulate periods

        """
