#!/usr/bin/env python
# -*- coding: utf8 -*-

#Hippocampe: Intel aggregator
#@author 2015 CERT-BDF <cert@banque-france.fr>
#@see The GNU Public License (GPL)
#
#This file is part of Hippocampe.
#
#Hippocampe is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#
#Hippocampe is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#for more details.
#
#You should have received a copy of the GNU General Public License along
#with Hippocampe; if not, write to the Free Software Foundation, Inc.,
#59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#or see <http://www.gnu.org/licenses/>.
#

from modules.common.ES import getES
import sources
import logging
logger = logging.getLogger(__name__)
def main():
	logger.info('lastQuery.main launched')
	try:
		report = dict()
		#retrieving sources report
		sourcesReport = sources.main()
		#isolating lastQuery date for every type under hippocampe index
		for url, dictAttributes in sourcesReport.items():
			report[url] = dict()
			report[url]['lastQuery'] = dictAttributes['lastQuery']
		logger.info('lastQuery.main end')
		return report
	except Exception as e:
		logger.error('distinct.main failed, no idea where it came from...', exc_info = True)
		response = dict()
		response['error'] = str(e)
		return response

if __name__ == '__main__':
	main()