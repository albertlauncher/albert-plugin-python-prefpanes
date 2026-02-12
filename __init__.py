# -*- coding: utf-8 -*-
# Copyright (c) 2024 Manuel Schneider

from albert import *

md_iid = "5.0"
md_version = "1.0"
md_name = "Preference panes"
md_description = "Open System Settings panes directly"
md_license = "MIT"
md_authors = ["@manuelschneid3r"]
md_platforms = ["Darwin"]

class PrefPane(Item):

    identifier: str
    name: str

    def __init__(self, identifier: str, name: str):
        Item.__init__(self)
        self.identifier = identifier
        self.name = name

    def id(self):
        return self.identifier

    def text(self):
        return self.name

    def subtext(self):
        return "System settings preference pane"

    def inputActionText(self):
        return self.name

    def icon(self):
        return Icon.fileType("/System/Applications/System Settings.app")

    def actions(self):
        return [Action("open", "Open", self.open)]

    def open(self):
        openUrl(f"x-apple.systempreferences:com.apple.{self.identifier}")

    @staticmethod
    def system_settings_icon_factory() -> Icon:
        return Icon.fileType("/System/Applications/System Settings.app")

def pref_panes():
    return [
        # Credits go to https://github.com/bvanpeski/SystemPreferences

        PrefPane("systempreferences.AppleIDSettings", "AppleID"),

        PrefPane("wifi-settings-extension", "Wi-Fi"),
        PrefPane("BluetoothSettings", "Bluetooth"),
        PrefPane("Network-Settings.extension", "Network"),
        PrefPane("NetworkExtensionSettingsUI.NESettingsUIExtension", "VPN"),

        PrefPane("Notifications-Settings.extension", "Notifications"),
        PrefPane("Sound-Settings.extension", "Sound"),
        PrefPane("Focus-Settings.extension", "Focus"),
        PrefPane("Screen-Time-Settings.extension", "Screen Time"),

        PrefPane("systempreferences.GeneralSettings", "General"),
        PrefPane("Appearance-Settings.extension", "Appearance"),
        PrefPane("Accessibility-Settings.extension", "Accessibility"),
        PrefPane("ControlCenter-Settings.extension", "Control Center"),
        PrefPane("Siri-Settings.extension", "Siri & Spotlight"),
        PrefPane("settings.PrivacySecurity.extension", "Privacy & Security"),

        PrefPane("Desktop-Settings.extension", "Desktop & Dock"),
        PrefPane("Displays-Settings.extension", "Displays"),
        PrefPane("Wallpaper-Settings.extension", "Wallpaper"),
        PrefPane("ScreenSaver-Settings.extension", "Screen Saver"),
        PrefPane("Battery-Settings.extension", "Battery"),
        #PrefPane("GeneralSettings", "Energy Saver"),

        PrefPane("Lock-Screen-Settings.extension", "Lock Screen"),
        PrefPane("Touch-ID-Settings.extension", "Touch ID & Password"),
        PrefPane("Users-Groups-Settings.extension", "Users & Groups"),

        PrefPane("Passwords-Settings.extension", "Passwords"),
        PrefPane("Internet-Accounts-Settings.extension", "Internet Accounts"),
        PrefPane("Game-Center-Settings.extension", "Game Center"),
        PrefPane("WalletSettingsExtension", "Wallet & Apple Pay"),

        PrefPane("Keyboard-Settings.extension", "Keyboard"),
        PrefPane("Trackpad-Settings.extension", "Trackpad"),
        PrefPane("Print-Scan-Settings.extension", "Printers & Scanners"),
    ]


class Plugin(PluginInstance, IndexQueryHandler):

    def __init__(self):
        PluginInstance.__init__(self)
        IndexQueryHandler.__init__(self)

    def updateIndexItems(self):
        self.setIndexItems([
            IndexItem(item=item, string=item.text())
            for item in pref_panes()
        ])
