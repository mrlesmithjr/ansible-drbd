import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_drbd_overview_command(host):
    with host.sudo():
        f = host.check_output('/usr/sbin/drbd-overview').strip()

        assert f.startswith('0:r0/0  Connected')
        assert 'Primary/Secondary' in f or 'Secondary/Primary' in f
        assert 'UpToDate/UpToDate' in f


def test_cl_status(host):
    with host.sudo():
        f = host.check_output('/usr/bin/cl_status hblinkstatus $(hostname) eth1').strip()

        assert 'up' in f
