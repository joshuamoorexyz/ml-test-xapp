from os import getenv # Give access to get environmental variables

from ricxappframe.xapp_frame import * # Get access to the RIC xApp framework


class Oaict_xApp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(
            self._default_handler,
            config_handler=self.config_handler,
            rmr_port = 4560,
            post_init = self._post_init,
            use_fake_sdl = bool(fake_sdl)
            )

    def _default_handler(self):
        print("Default handler")

    def config_handler(self, rmr_xapp, config):
        print("Handle config change")

    def _post_init(self):
        print("Post init")

    def start(self):
        print("Start")
