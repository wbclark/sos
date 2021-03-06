# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.plugins import Plugin, RedHatPlugin


class convert2rhel(Plugin, RedHatPlugin):
    """Convert2RHEL
    """
    plugin_name = 'convert2rhel'
    profiles = ('system')
    packages = ('convert2rhel')
    verify_packages = ('convert2rhel$',)

    def setup(self):

        self.add_copy_spec([
            "/var/log/convert2rhel/convert2rhel.log",
            "/var/log/convert2rhel/rpm_va.log"
        ])


# vim: set et ts=4 sw=4 :
