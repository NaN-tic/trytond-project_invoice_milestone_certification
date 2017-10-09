# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import doctest
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import doctest_setup, doctest_teardown
from trytond.tests.test_tryton import doctest_checker


class ProjectInvoiceMilestoneCertificationTestCase(ModuleTestCase):
    'Test Project Invoice Milestone module'
    module = 'project_invoice_milestone_certification'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProjectInvoiceMilestoneCertificationTestCase))
    return suite
