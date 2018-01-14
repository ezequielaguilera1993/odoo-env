# -*- coding: utf-8 -*-
import unittest
from scripts.odooenv import OdooEnv


class TestRepository(unittest.TestCase):
    def test_test(self):
        options = {}
        oe = OdooEnv(options)
        cmds = oe.install_client('test_client')
        self.assertEqual(cmds[0].args, ['/odoo_ar/'])
        self.assertEqual(cmds[0]._check, 'path.isdir')
        self.assertEqual(cmds[0].command, 'sudo mkdir {}')
        self.assertEqual(cmds[0].usr_msg, 'Installing client test_client')

        self.assertEqual(cmds[2].args, ['/odoo_ar/odoo-9.0/test_client/postgresql'])
        self.assertEqual(cmds[2]._check, 'path.isdir')
        self.assertEqual(cmds[2].command, 'mkdir -p {}')
        self.assertEqual(cmds[2].usr_msg, False)

