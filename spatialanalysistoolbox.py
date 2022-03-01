# -*- coding: utf-8 -*-

"""
/***************************************************************************
 SpatialAnalysisToolbox
                                 A QGIS plugin
This plugin adds some useful algorithms for Spatial Analysis. Some of them are: Moran's I, Local Moran's I, GWR.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-03-01
        copyright            : (C) 2020 by Parmenion Delialis
        email                : parmeniondelialis@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Parmenion Delialis'
__date__ = '2022-03-01'
__copyright__ = '(C) 2022 by Parmenion Delialis'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .spatialanalysistoolbox_provider import SpatialAnalysisToolboxProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class SpatialAnalysisToolboxPlugin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = SpatialAnalysisToolboxProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
