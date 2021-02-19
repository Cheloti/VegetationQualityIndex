# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VQI
                                 A QGIS plugin
 VQI = (fire risk * erosion protection * drought resistance * vegetation cover )1/4
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-02-19
        copyright            : (C) 2021 by Brian Cheloti
        email                : chelotibrian2016@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VQI class from file VQI.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Vegetation_Index import VQI
    return VQI(iface)
