# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from test_case import *



class test(base_test):

    def __init__(self, app):
        base_test.__init__(self, app)
        base_test.set_image_path(self, os.path.split(__file__)[0])
        self.assets = os.path.join(os.path.split(__file__)[0], "assets")
        self.meta = "This is a test of the library window controls"


    def maximize_library_osx(self):
        library_controls = "library_controls.png"

        # Set target to the maximize button
        maximize_button = Pattern(library_controls).targetOffset(21, 0)

        # We must hover the controls so the ALT key can take effect there.
        hover(library_controls)

        # Alt key changes maximize button from full screen to maximize window.
        keyDown(Key.ALT)
        click(maximize_button)
        keyUp(Key.ALT)


    def run(self):
        open_library()
        time.sleep(1)

        if exists("library_title.png", 10):
            print "The library was opened successfully"

            if get_os() == "linux":
                if exists("maximize_button.png", 10):
                    click("maximize_button.png")
                    time.sleep(1)

                    if exists("restore_button.png", 10):
                        print "The library was maximized successfully"
                    else:
                        print "The library was not maximized"
                        result = "FAIL"
                        return

                    click("restore_button.png")
                    time.sleep(1)

                    if exists("maximize_button.png", 10):
                        print "The library was restored successfully"
                    else:
                        print "The library was not restored"
                        result = "FAIL"
                        return

                    click("minimize_button.png")
                    time.sleep(1)

                else:
                    print "Maximize button was not found"
                    result = "FAIL"
                    return

            elif get_os() == "win":
                maximize_window()
                time.sleep(1)
            
                if exists("library_restore_button.png", 10):
                    print "The library was maximized successfully"
                else:
                    print "The library was not maximized"
                    result = "FAIL"
                    return

                minimize_window()
                time.sleep(1)

                if exists("library_maximize_button.png", 10):
                    print "The library was restored successfully"
                else:
                    print "The library was not restored"
                    result = "FAIL"
                    return

                minimize_window()
                time.sleep(1)

            else:
                self.maximize_library_osx()
                time.sleep(1)

                self.maximize_library_osx()
                time.sleep(1)

                minimize_window()
                time.sleep(1)

            if waitVanish("library_title.png", 10):
                logger.debug("window successfully minimized")
            else:
                result = "FAIL"
                logger.error("window not minimized, aborting test")
                return

            if get_os() == "osx":
                type(text=Key.DOWN, modifier=KeyModifier.CTRL)
                time.sleep(0.5)
                keyDown(Key.DOWN)
                keyUp(Key.DOWN)
                keyDown(Key.ENTER)
                keyUp(Key.ENTER)

            else:
                restore_window_from_taskbar()

            if exists("library_title.png", 10):
                print "The library was restored successfully"
            else:
                print "The library was not restored"
                result = "FAIL"
                return

        else:
            print "The library was not opened"
            result = "FAIL"

        close_auxiliary_window()
        if waitVanish("library_title.png", 10):
            result = "PASS"

        print result