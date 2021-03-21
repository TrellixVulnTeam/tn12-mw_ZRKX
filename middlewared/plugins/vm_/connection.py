import libvirt

from middlewared.service import CallError


LIBVIRT_URI = 'bhyve+unix:///system'


class LibvirtConnectionMixin:

    LIBVIRT_CONNECTION = None

    def _open(self):
        try:
            # We want to do this before initializing libvirt connection
            libvirt.virEventRegisterDefaultImpl()
            LibvirtConnectionMixin.LIBVIRT_CONNECTION = libvirt.open(LIBVIRT_URI)
        except libvirt.libvirtError as e:
            raise CallError(f'Failed to open libvirt connection: {e}')

    def _close(self):
        try:
            LibvirtConnectionMixin.LIBVIRT_CONNECTION.close()
        except libvirt.libvirtError as e:
            raise CallError(f'Failed to close libvirt connection: {e}')
        else:
            LibvirtConnectionMixin.LIBVIRT_CONNECTION = None

    def _is_connection_alive(self):
        return LibvirtConnectionMixin.LIBVIRT_CONNECTION and LibvirtConnectionMixin.LIBVIRT_CONNECTION.isAlive()

    def _check_connection_alive(self):
        if not self._is_connection_alive():
            raise CallError('Failed to connect to libvirt')

    def _check_setup_connection(self):
        if not self._is_connection_alive():
            self.middleware.call_sync('vm.wait_for_libvirtd', 10)
        self._check_connection_alive()
