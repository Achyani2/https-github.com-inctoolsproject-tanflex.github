# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' INDEXBOTS\n")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('Open this link ' + notice + 'INDEXBOTS\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
