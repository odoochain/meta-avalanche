################################################################################
# Copyright (c) 2020 ContinualAI Research                                      #
# Copyrights licensed under the MIT License.                                   #
# See the accompanying LICENSE file for terms.                                 #
#                                                                              #
# Date: 19-02-2020                                                             #
# Author(s): Vincenzo Lomonaco                                                 #
# E-mail: contact@continualai.org                                              #
# Website: clair.continualai.org                                               #
################################################################################

"""
This is a simple script to test if avalanche is installed correctly.
"""

import avalanche

def main():

    print("Avalanche Version:", avalanche.__version__)
    print("Everything looks fine here :-)")

if __name__ == '__main__':

    main()
