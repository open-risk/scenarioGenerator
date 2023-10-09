# encoding: utf-8

# (c) 2019 - 2023 Open Risk (https://www.openriskmanagement.com)
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


from codecs import open

from setuptools import setup

__version__ = '0.1.0'

ver = __version__

long_descr = open('description.rst', 'r', encoding='utf8').read()

setup(name='scenarioGenerator',
      version=ver,
      description='A Python powered library for the generation of economic scenarios',
      long_description=long_descr,
      author='Open Risk',
      author_email='info@openrisk.eu',
      packages=['scenarioGenerator', 'scenarioGenerator.utils', 'tests', 'datasets', 'examples.python'],
      include_package_data=True,
      url='https://github.com/open-risk/scenarioGenerator',
      install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'statsmodels',
          'sympy',
          'matplotlib'
      ],
      zip_safe=False,
      provides=['scenarioGenerator'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Financial and Insurance Industry',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.10',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis'
      ]

      )
