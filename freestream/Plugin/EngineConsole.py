#Embedded file name: freestream/Plugin/EngineConsole.py
import time
from freestream.GlobalConfig import globalConfig
from freestream.version import VERSION
from freestream.Plugin.BackgroundProcess import run_bgapp, stop_bgapp
from freestream.Core.Utilities.logger import log, log_exc

class AppWrapper:

    def __init__(self):
        self.bgapp = None

    def set_bgapp(self, bgapp):
        self.bgapp = bgapp

    def MainLoop(self):
        try:
            while True:
                time.sleep(10)

        except:
            log('appwrapper::MainLoop: exit')
            self.OnExit()

    def OnExit(self):
        if self.bgapp is not None:
            self.bgapp.OnExit()

    def set_icon_tooltip(self, txt):
        pass


def start(apptype, exec_dir):
    globalConfig.set_value('apptype', apptype)
    globalConfig.set_mode('client_console')
    wrapper = AppWrapper()
    bgapp = run_bgapp(wrapper, appname, VERSION)
    wrapper.set_bgapp(bgapp)
    wrapper.MainLoop()
    stop_bgapp(bgapp)