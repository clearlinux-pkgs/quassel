#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : quassel
Version  : 0.13.rc1
Release  : 4
URL      : https://github.com/quassel/quassel/archive/0.13-rc1.tar.gz
Source0  : https://github.com/quassel/quassel/archive/0.13-rc1.tar.gz
Source1  : quassel.tmpfiles
Source2  : quasselcore.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 LGPL-3.0
Requires: quassel-bin
Requires: quassel-config
Requires: quassel-data
Requires: quassel-license
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Script)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(phonon4qt5)
BuildRequires : qtbase-extras
BuildRequires : zlib-dev

%description
We bundle some CMake scripts that are not part of CMake itself, for convenience
on platforms that do not have a standard location for packages to put their
CMake support into. Most of those scripts originate from the KDE community;
some are from other sources. Please see the files themselves for copyright
and license statements.

%package bin
Summary: bin components for the quassel package.
Group: Binaries
Requires: quassel-data
Requires: quassel-config
Requires: quassel-license

%description bin
bin components for the quassel package.


%package config
Summary: config components for the quassel package.
Group: Default

%description config
config components for the quassel package.


%package data
Summary: data components for the quassel package.
Group: Data

%description data
data components for the quassel package.


%package extras
Summary: extras components for the quassel package.
Group: Default

%description extras
extras components for the quassel package.


%package license
Summary: license components for the quassel package.
Group: Default

%description license
license components for the quassel package.


%prep
%setup -q -n quassel-0.13-rc1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534184859
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1534184859
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/quassel
cp 3rdparty/icons/breeze-dark/COPYING-ICONS %{buildroot}/usr/share/doc/quassel/3rdparty_icons_breeze-dark_COPYING-ICONS
cp 3rdparty/icons/breeze-dark/LICENSE %{buildroot}/usr/share/doc/quassel/3rdparty_icons_breeze-dark_LICENSE
cp 3rdparty/icons/breeze/COPYING-ICONS %{buildroot}/usr/share/doc/quassel/3rdparty_icons_breeze_COPYING-ICONS
cp 3rdparty/icons/breeze/LICENSE %{buildroot}/usr/share/doc/quassel/3rdparty_icons_breeze_LICENSE
cp 3rdparty/icons/oxygen/COPYING %{buildroot}/usr/share/doc/quassel/3rdparty_icons_oxygen_COPYING
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/doc/quassel/cmake_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/quasselcore.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/quassel.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/quasselcore
/usr/bin/quassel
/usr/bin/quasselclient

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/quasselcore.service
/usr/lib/tmpfiles.d/quassel.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/quassel.desktop
/usr/share/applications/quasselclient.desktop
/usr/share/icons/hicolor/128x128/apps/quassel.png
/usr/share/icons/hicolor/16x16/apps/quassel.png
/usr/share/icons/hicolor/22x22/apps/quassel.png
/usr/share/icons/hicolor/32x32/apps/quassel.png
/usr/share/icons/hicolor/48x48/apps/quassel.png
/usr/share/icons/hicolor/64x64/apps/quassel.png
/usr/share/pixmaps/quassel.png
/usr/share/quassel/icons/breeze-dark/AUTHORS
/usr/share/quassel/icons/breeze-dark/COPYING-ICONS
/usr/share/quassel/icons/breeze-dark/LICENSE
/usr/share/quassel/icons/breeze-dark/actions/16/application-exit.svg
/usr/share/quassel/icons/breeze-dark/actions/16/configure-shortcuts.svg
/usr/share/quassel/icons/breeze-dark/actions/16/configure.svg
/usr/share/quassel/icons/breeze-dark/actions/16/dialog-cancel.svg
/usr/share/quassel/icons/breeze-dark/actions/16/dialog-close.svg
/usr/share/quassel/icons/breeze-dark/actions/16/document-edit.svg
/usr/share/quassel/icons/breeze-dark/actions/16/document-encrypt.svg
/usr/share/quassel/icons/breeze-dark/actions/16/document-open.svg
/usr/share/quassel/icons/breeze-dark/actions/16/download.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-clear.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-copy.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-delete.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-find.svg
/usr/share/quassel/icons/breeze-dark/actions/16/edit-rename.svg
/usr/share/quassel/icons/breeze-dark/actions/16/flag-blue.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-fill-color.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-list-unordered.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-text-bold.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-text-color.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-text-italic.svg
/usr/share/quassel/icons/breeze-dark/actions/16/format-text-underline.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-down.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-next-view.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-next.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-previous-view.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-previous.svg
/usr/share/quassel/icons/breeze-dark/actions/16/go-up.svg
/usr/share/quassel/icons/breeze-dark/actions/16/help-about.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-ban-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-user-away.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-user-offline.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-user-online.svg
/usr/share/quassel/icons/breeze-dark/actions/16/im-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/irc-channel-active.svg
/usr/share/quassel/icons/breeze-dark/actions/16/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze-dark/actions/16/irc-close-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/16/irc-join-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/16/list-add-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/list-add.svg
/usr/share/quassel/icons/breeze-dark/actions/16/list-remove-user.svg
/usr/share/quassel/icons/breeze-dark/actions/16/mail-message-new.svg
/usr/share/quassel/icons/breeze-dark/actions/16/media-playback-start.svg
/usr/share/quassel/icons/breeze-dark/actions/16/network-connect.svg
/usr/share/quassel/icons/breeze-dark/actions/16/network-disconnect.svg
/usr/share/quassel/icons/breeze-dark/actions/16/show-menu.svg
/usr/share/quassel/icons/breeze-dark/actions/16/tools-report-bug.svg
/usr/share/quassel/icons/breeze-dark/actions/16/view-fullscreen.svg
/usr/share/quassel/icons/breeze-dark/actions/16/view-refresh.svg
/usr/share/quassel/icons/breeze-dark/actions/16/zoom-in.svg
/usr/share/quassel/icons/breeze-dark/actions/16/zoom-original.svg
/usr/share/quassel/icons/breeze-dark/actions/16/zoom-out.svg
/usr/share/quassel/icons/breeze-dark/actions/22/application-exit.svg
/usr/share/quassel/icons/breeze-dark/actions/22/configure-shortcuts.svg
/usr/share/quassel/icons/breeze-dark/actions/22/configure.svg
/usr/share/quassel/icons/breeze-dark/actions/22/dialog-cancel.svg
/usr/share/quassel/icons/breeze-dark/actions/22/dialog-close.svg
/usr/share/quassel/icons/breeze-dark/actions/22/document-edit.svg
/usr/share/quassel/icons/breeze-dark/actions/22/document-encrypt.svg
/usr/share/quassel/icons/breeze-dark/actions/22/document-open.svg
/usr/share/quassel/icons/breeze-dark/actions/22/download.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-clear.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-copy.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-delete.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-find.svg
/usr/share/quassel/icons/breeze-dark/actions/22/edit-rename.svg
/usr/share/quassel/icons/breeze-dark/actions/22/flag-blue.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-fill-color.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-list-unordered.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-text-bold.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-text-color.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-text-italic.svg
/usr/share/quassel/icons/breeze-dark/actions/22/format-text-underline.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-down.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-next-view.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-next.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-previous-view.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-previous.svg
/usr/share/quassel/icons/breeze-dark/actions/22/go-up.svg
/usr/share/quassel/icons/breeze-dark/actions/22/help-about.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-ban-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-user-away.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-user-offline.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-user-online.svg
/usr/share/quassel/icons/breeze-dark/actions/22/im-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-channel-active.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-close-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-join-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-operator.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-remove-operator.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-unvoice.svg
/usr/share/quassel/icons/breeze-dark/actions/22/irc-voice.svg
/usr/share/quassel/icons/breeze-dark/actions/22/list-add-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/list-add.svg
/usr/share/quassel/icons/breeze-dark/actions/22/list-remove-user.svg
/usr/share/quassel/icons/breeze-dark/actions/22/mail-message-new.svg
/usr/share/quassel/icons/breeze-dark/actions/22/media-playback-start.svg
/usr/share/quassel/icons/breeze-dark/actions/22/network-connect.svg
/usr/share/quassel/icons/breeze-dark/actions/22/network-disconnect.svg
/usr/share/quassel/icons/breeze-dark/actions/22/show-menu.svg
/usr/share/quassel/icons/breeze-dark/actions/22/tools-report-bug.svg
/usr/share/quassel/icons/breeze-dark/actions/22/view-fullscreen.svg
/usr/share/quassel/icons/breeze-dark/actions/22/view-refresh.svg
/usr/share/quassel/icons/breeze-dark/actions/22/zoom-in.svg
/usr/share/quassel/icons/breeze-dark/actions/22/zoom-original.svg
/usr/share/quassel/icons/breeze-dark/actions/22/zoom-out.svg
/usr/share/quassel/icons/breeze-dark/actions/24/application-exit.svg
/usr/share/quassel/icons/breeze-dark/actions/24/configure-shortcuts.svg
/usr/share/quassel/icons/breeze-dark/actions/24/configure.svg
/usr/share/quassel/icons/breeze-dark/actions/24/connect-quassel.svg
/usr/share/quassel/icons/breeze-dark/actions/24/dialog-cancel.svg
/usr/share/quassel/icons/breeze-dark/actions/24/dialog-close.svg
/usr/share/quassel/icons/breeze-dark/actions/24/disconnect-quassel.svg
/usr/share/quassel/icons/breeze-dark/actions/24/document-edit.svg
/usr/share/quassel/icons/breeze-dark/actions/24/document-encrypt.svg
/usr/share/quassel/icons/breeze-dark/actions/24/document-open.svg
/usr/share/quassel/icons/breeze-dark/actions/24/download.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-clear.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-copy.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-delete.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-find.svg
/usr/share/quassel/icons/breeze-dark/actions/24/edit-rename.svg
/usr/share/quassel/icons/breeze-dark/actions/24/flag-blue.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-fill-color.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-list-unordered.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-text-bold.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-text-color.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-text-italic.svg
/usr/share/quassel/icons/breeze-dark/actions/24/format-text-underline.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-down.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-next-view.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-next.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-previous-view.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-previous.svg
/usr/share/quassel/icons/breeze-dark/actions/24/go-up.svg
/usr/share/quassel/icons/breeze-dark/actions/24/help-about.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-ban-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-kick-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-user-away.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-user-offline.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-user-online.svg
/usr/share/quassel/icons/breeze-dark/actions/24/im-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-channel-active.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-close-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-join-channel.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-operator.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-remove-operator.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-unvoice.svg
/usr/share/quassel/icons/breeze-dark/actions/24/irc-voice.svg
/usr/share/quassel/icons/breeze-dark/actions/24/list-add-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/list-add.svg
/usr/share/quassel/icons/breeze-dark/actions/24/list-remove-user.svg
/usr/share/quassel/icons/breeze-dark/actions/24/mail-message-new.svg
/usr/share/quassel/icons/breeze-dark/actions/24/media-playback-start.svg
/usr/share/quassel/icons/breeze-dark/actions/24/network-connect.svg
/usr/share/quassel/icons/breeze-dark/actions/24/network-disconnect.svg
/usr/share/quassel/icons/breeze-dark/actions/24/show-menu.svg
/usr/share/quassel/icons/breeze-dark/actions/24/tools-report-bug.svg
/usr/share/quassel/icons/breeze-dark/actions/24/view-fullscreen.svg
/usr/share/quassel/icons/breeze-dark/actions/24/view-refresh.svg
/usr/share/quassel/icons/breeze-dark/actions/24/zoom-in.svg
/usr/share/quassel/icons/breeze-dark/actions/24/zoom-original.svg
/usr/share/quassel/icons/breeze-dark/actions/24/zoom-out.svg
/usr/share/quassel/icons/breeze-dark/actions/32/application-exit.svg
/usr/share/quassel/icons/breeze-dark/actions/32/configure-shortcuts.svg
/usr/share/quassel/icons/breeze-dark/actions/32/configure.svg
/usr/share/quassel/icons/breeze-dark/actions/32/connect-quassel.svg
/usr/share/quassel/icons/breeze-dark/actions/32/dialog-cancel.svg
/usr/share/quassel/icons/breeze-dark/actions/32/disconnect-quassel.svg
/usr/share/quassel/icons/breeze-dark/actions/32/document-edit.svg
/usr/share/quassel/icons/breeze-dark/actions/32/document-open.svg
/usr/share/quassel/icons/breeze-dark/actions/32/edit-delete.svg
/usr/share/quassel/icons/breeze-dark/actions/32/go-down.svg
/usr/share/quassel/icons/breeze-dark/actions/32/go-next.svg
/usr/share/quassel/icons/breeze-dark/actions/32/go-previous.svg
/usr/share/quassel/icons/breeze-dark/actions/32/go-up.svg
/usr/share/quassel/icons/breeze-dark/actions/32/help-about.svg
/usr/share/quassel/icons/breeze-dark/actions/32/mail-message-new.svg
/usr/share/quassel/icons/breeze-dark/actions/32/media-playback-start.svg
/usr/share/quassel/icons/breeze-dark/actions/32/view-refresh.svg
/usr/share/quassel/icons/breeze-dark/actions/32/zoom-in.svg
/usr/share/quassel/icons/breeze-dark/actions/32/zoom-original.svg
/usr/share/quassel/icons/breeze-dark/actions/32/zoom-out.svg
/usr/share/quassel/icons/breeze-dark/apps/32/quassel.svg
/usr/share/quassel/icons/breeze-dark/apps/48/quassel.svg
/usr/share/quassel/icons/breeze-dark/apps/64/quassel.svg
/usr/share/quassel/icons/breeze-dark/devices/16/network-wired.svg
/usr/share/quassel/icons/breeze-dark/devices/22/network-wired.svg
/usr/share/quassel/icons/breeze-dark/index.theme
/usr/share/quassel/icons/breeze-dark/preferences/32/help-about.svg
/usr/share/quassel/icons/breeze-dark/scalable/actions/connect-quassel.svg
/usr/share/quassel/icons/breeze-dark/scalable/actions/disconnect-quassel.svg
/usr/share/quassel/icons/breeze-dark/scalable/apps/quassel.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/active-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/inactive-quassel.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/message-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/scalable/status/message-quassel.svg
/usr/share/quassel/icons/breeze-dark/status/16/dialog-information.svg
/usr/share/quassel/icons/breeze-dark/status/16/security-high.svg
/usr/share/quassel/icons/breeze-dark/status/16/security-low.svg
/usr/share/quassel/icons/breeze-dark/status/16/user-available.svg
/usr/share/quassel/icons/breeze-dark/status/16/user-away.svg
/usr/share/quassel/icons/breeze-dark/status/16/user-offline.svg
/usr/share/quassel/icons/breeze-dark/status/22/dialog-information.svg
/usr/share/quassel/icons/breeze-dark/status/22/dialog-password.svg
/usr/share/quassel/icons/breeze-dark/status/22/network-wired.svg
/usr/share/quassel/icons/breeze-dark/status/22/security-high.svg
/usr/share/quassel/icons/breeze-dark/status/22/security-low.svg
/usr/share/quassel/icons/breeze-dark/status/22/user-available.svg
/usr/share/quassel/icons/breeze-dark/status/22/user-away.svg
/usr/share/quassel/icons/breeze-dark/status/22/user-offline.svg
/usr/share/quassel/icons/breeze-dark/status/24/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/24/active-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/24/dialog-information.svg
/usr/share/quassel/icons/breeze-dark/status/24/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/24/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/24/inactive-quassel.svg
/usr/share/quassel/icons/breeze-dark/status/24/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/24/message-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/24/message-quassel.svg
/usr/share/quassel/icons/breeze-dark/status/64/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/64/active-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/64/dialog-information.svg
/usr/share/quassel/icons/breeze-dark/status/64/dialog-password.svg
/usr/share/quassel/icons/breeze-dark/status/64/dialog-warning.svg
/usr/share/quassel/icons/breeze-dark/status/64/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/64/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/64/inactive-quassel.svg
/usr/share/quassel/icons/breeze-dark/status/64/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze-dark/status/64/message-quassel-tray.svg
/usr/share/quassel/icons/breeze-dark/status/64/message-quassel.svg
/usr/share/quassel/icons/breeze-dark/status/64/security-high.svg
/usr/share/quassel/icons/breeze-dark/status/64/security-low.svg
/usr/share/quassel/icons/breeze/AUTHORS
/usr/share/quassel/icons/breeze/COPYING-ICONS
/usr/share/quassel/icons/breeze/LICENSE
/usr/share/quassel/icons/breeze/actions/16/application-exit.svg
/usr/share/quassel/icons/breeze/actions/16/configure-shortcuts.svg
/usr/share/quassel/icons/breeze/actions/16/configure.svg
/usr/share/quassel/icons/breeze/actions/16/dialog-cancel.svg
/usr/share/quassel/icons/breeze/actions/16/dialog-close.svg
/usr/share/quassel/icons/breeze/actions/16/document-edit.svg
/usr/share/quassel/icons/breeze/actions/16/document-encrypt.svg
/usr/share/quassel/icons/breeze/actions/16/document-open.svg
/usr/share/quassel/icons/breeze/actions/16/download.svg
/usr/share/quassel/icons/breeze/actions/16/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze/actions/16/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze/actions/16/edit-clear.svg
/usr/share/quassel/icons/breeze/actions/16/edit-copy.svg
/usr/share/quassel/icons/breeze/actions/16/edit-delete.svg
/usr/share/quassel/icons/breeze/actions/16/edit-find.svg
/usr/share/quassel/icons/breeze/actions/16/edit-rename.svg
/usr/share/quassel/icons/breeze/actions/16/flag-blue.svg
/usr/share/quassel/icons/breeze/actions/16/format-fill-color.svg
/usr/share/quassel/icons/breeze/actions/16/format-list-unordered.svg
/usr/share/quassel/icons/breeze/actions/16/format-text-bold.svg
/usr/share/quassel/icons/breeze/actions/16/format-text-color.svg
/usr/share/quassel/icons/breeze/actions/16/format-text-italic.svg
/usr/share/quassel/icons/breeze/actions/16/format-text-underline.svg
/usr/share/quassel/icons/breeze/actions/16/go-down.svg
/usr/share/quassel/icons/breeze/actions/16/go-next-view.svg
/usr/share/quassel/icons/breeze/actions/16/go-next.svg
/usr/share/quassel/icons/breeze/actions/16/go-previous-view.svg
/usr/share/quassel/icons/breeze/actions/16/go-previous.svg
/usr/share/quassel/icons/breeze/actions/16/go-up.svg
/usr/share/quassel/icons/breeze/actions/16/help-about.svg
/usr/share/quassel/icons/breeze/actions/16/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze/actions/16/im-ban-user.svg
/usr/share/quassel/icons/breeze/actions/16/im-kick-user.svg
/usr/share/quassel/icons/breeze/actions/16/im-user-away.svg
/usr/share/quassel/icons/breeze/actions/16/im-user-offline.svg
/usr/share/quassel/icons/breeze/actions/16/im-user-online.svg
/usr/share/quassel/icons/breeze/actions/16/im-user.svg
/usr/share/quassel/icons/breeze/actions/16/irc-channel-active.svg
/usr/share/quassel/icons/breeze/actions/16/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze/actions/16/irc-close-channel.svg
/usr/share/quassel/icons/breeze/actions/16/irc-join-channel.svg
/usr/share/quassel/icons/breeze/actions/16/list-add-user.svg
/usr/share/quassel/icons/breeze/actions/16/list-add.svg
/usr/share/quassel/icons/breeze/actions/16/list-remove-user.svg
/usr/share/quassel/icons/breeze/actions/16/mail-message-new.svg
/usr/share/quassel/icons/breeze/actions/16/media-playback-start.svg
/usr/share/quassel/icons/breeze/actions/16/network-connect.svg
/usr/share/quassel/icons/breeze/actions/16/network-disconnect.svg
/usr/share/quassel/icons/breeze/actions/16/show-menu.svg
/usr/share/quassel/icons/breeze/actions/16/tools-report-bug.svg
/usr/share/quassel/icons/breeze/actions/16/view-fullscreen.svg
/usr/share/quassel/icons/breeze/actions/16/view-refresh.svg
/usr/share/quassel/icons/breeze/actions/16/zoom-in.svg
/usr/share/quassel/icons/breeze/actions/16/zoom-original.svg
/usr/share/quassel/icons/breeze/actions/16/zoom-out.svg
/usr/share/quassel/icons/breeze/actions/22/application-exit.svg
/usr/share/quassel/icons/breeze/actions/22/configure-shortcuts.svg
/usr/share/quassel/icons/breeze/actions/22/configure.svg
/usr/share/quassel/icons/breeze/actions/22/dialog-cancel.svg
/usr/share/quassel/icons/breeze/actions/22/dialog-close.svg
/usr/share/quassel/icons/breeze/actions/22/document-edit.svg
/usr/share/quassel/icons/breeze/actions/22/document-encrypt.svg
/usr/share/quassel/icons/breeze/actions/22/document-open.svg
/usr/share/quassel/icons/breeze/actions/22/download.svg
/usr/share/quassel/icons/breeze/actions/22/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze/actions/22/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze/actions/22/edit-clear.svg
/usr/share/quassel/icons/breeze/actions/22/edit-copy.svg
/usr/share/quassel/icons/breeze/actions/22/edit-delete.svg
/usr/share/quassel/icons/breeze/actions/22/edit-find.svg
/usr/share/quassel/icons/breeze/actions/22/edit-rename.svg
/usr/share/quassel/icons/breeze/actions/22/flag-blue.svg
/usr/share/quassel/icons/breeze/actions/22/format-fill-color.svg
/usr/share/quassel/icons/breeze/actions/22/format-list-unordered.svg
/usr/share/quassel/icons/breeze/actions/22/format-text-bold.svg
/usr/share/quassel/icons/breeze/actions/22/format-text-color.svg
/usr/share/quassel/icons/breeze/actions/22/format-text-italic.svg
/usr/share/quassel/icons/breeze/actions/22/format-text-underline.svg
/usr/share/quassel/icons/breeze/actions/22/go-down.svg
/usr/share/quassel/icons/breeze/actions/22/go-next-view.svg
/usr/share/quassel/icons/breeze/actions/22/go-next.svg
/usr/share/quassel/icons/breeze/actions/22/go-previous-view.svg
/usr/share/quassel/icons/breeze/actions/22/go-previous.svg
/usr/share/quassel/icons/breeze/actions/22/go-up.svg
/usr/share/quassel/icons/breeze/actions/22/help-about.svg
/usr/share/quassel/icons/breeze/actions/22/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze/actions/22/im-ban-user.svg
/usr/share/quassel/icons/breeze/actions/22/im-kick-user.svg
/usr/share/quassel/icons/breeze/actions/22/im-user-away.svg
/usr/share/quassel/icons/breeze/actions/22/im-user-offline.svg
/usr/share/quassel/icons/breeze/actions/22/im-user-online.svg
/usr/share/quassel/icons/breeze/actions/22/im-user.svg
/usr/share/quassel/icons/breeze/actions/22/irc-channel-active.svg
/usr/share/quassel/icons/breeze/actions/22/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze/actions/22/irc-close-channel.svg
/usr/share/quassel/icons/breeze/actions/22/irc-join-channel.svg
/usr/share/quassel/icons/breeze/actions/22/irc-operator.svg
/usr/share/quassel/icons/breeze/actions/22/irc-remove-operator.svg
/usr/share/quassel/icons/breeze/actions/22/irc-unvoice.svg
/usr/share/quassel/icons/breeze/actions/22/irc-voice.svg
/usr/share/quassel/icons/breeze/actions/22/list-add-user.svg
/usr/share/quassel/icons/breeze/actions/22/list-add.svg
/usr/share/quassel/icons/breeze/actions/22/list-remove-user.svg
/usr/share/quassel/icons/breeze/actions/22/mail-message-new.svg
/usr/share/quassel/icons/breeze/actions/22/media-playback-start.svg
/usr/share/quassel/icons/breeze/actions/22/network-connect.svg
/usr/share/quassel/icons/breeze/actions/22/network-disconnect.svg
/usr/share/quassel/icons/breeze/actions/22/show-menu.svg
/usr/share/quassel/icons/breeze/actions/22/tools-report-bug.svg
/usr/share/quassel/icons/breeze/actions/22/view-fullscreen.svg
/usr/share/quassel/icons/breeze/actions/22/view-refresh.svg
/usr/share/quassel/icons/breeze/actions/22/zoom-in.svg
/usr/share/quassel/icons/breeze/actions/22/zoom-original.svg
/usr/share/quassel/icons/breeze/actions/22/zoom-out.svg
/usr/share/quassel/icons/breeze/actions/24/application-exit.svg
/usr/share/quassel/icons/breeze/actions/24/configure-shortcuts.svg
/usr/share/quassel/icons/breeze/actions/24/configure.svg
/usr/share/quassel/icons/breeze/actions/24/connect-quassel.svg
/usr/share/quassel/icons/breeze/actions/24/dialog-cancel.svg
/usr/share/quassel/icons/breeze/actions/24/dialog-close.svg
/usr/share/quassel/icons/breeze/actions/24/disconnect-quassel.svg
/usr/share/quassel/icons/breeze/actions/24/document-edit.svg
/usr/share/quassel/icons/breeze/actions/24/document-encrypt.svg
/usr/share/quassel/icons/breeze/actions/24/document-open.svg
/usr/share/quassel/icons/breeze/actions/24/download.svg
/usr/share/quassel/icons/breeze/actions/24/edit-clear-locationbar-ltr.svg
/usr/share/quassel/icons/breeze/actions/24/edit-clear-locationbar-rtl.svg
/usr/share/quassel/icons/breeze/actions/24/edit-clear.svg
/usr/share/quassel/icons/breeze/actions/24/edit-copy.svg
/usr/share/quassel/icons/breeze/actions/24/edit-delete.svg
/usr/share/quassel/icons/breeze/actions/24/edit-find.svg
/usr/share/quassel/icons/breeze/actions/24/edit-rename.svg
/usr/share/quassel/icons/breeze/actions/24/flag-blue.svg
/usr/share/quassel/icons/breeze/actions/24/format-fill-color.svg
/usr/share/quassel/icons/breeze/actions/24/format-list-unordered.svg
/usr/share/quassel/icons/breeze/actions/24/format-text-bold.svg
/usr/share/quassel/icons/breeze/actions/24/format-text-color.svg
/usr/share/quassel/icons/breeze/actions/24/format-text-italic.svg
/usr/share/quassel/icons/breeze/actions/24/format-text-underline.svg
/usr/share/quassel/icons/breeze/actions/24/go-down.svg
/usr/share/quassel/icons/breeze/actions/24/go-next-view.svg
/usr/share/quassel/icons/breeze/actions/24/go-next.svg
/usr/share/quassel/icons/breeze/actions/24/go-previous-view.svg
/usr/share/quassel/icons/breeze/actions/24/go-previous.svg
/usr/share/quassel/icons/breeze/actions/24/go-up.svg
/usr/share/quassel/icons/breeze/actions/24/help-about.svg
/usr/share/quassel/icons/breeze/actions/24/im-ban-kick-user.svg
/usr/share/quassel/icons/breeze/actions/24/im-ban-user.svg
/usr/share/quassel/icons/breeze/actions/24/im-kick-user.svg
/usr/share/quassel/icons/breeze/actions/24/im-user-away.svg
/usr/share/quassel/icons/breeze/actions/24/im-user-offline.svg
/usr/share/quassel/icons/breeze/actions/24/im-user-online.svg
/usr/share/quassel/icons/breeze/actions/24/im-user.svg
/usr/share/quassel/icons/breeze/actions/24/irc-channel-active.svg
/usr/share/quassel/icons/breeze/actions/24/irc-channel-inactive.svg
/usr/share/quassel/icons/breeze/actions/24/irc-close-channel.svg
/usr/share/quassel/icons/breeze/actions/24/irc-join-channel.svg
/usr/share/quassel/icons/breeze/actions/24/irc-operator.svg
/usr/share/quassel/icons/breeze/actions/24/irc-remove-operator.svg
/usr/share/quassel/icons/breeze/actions/24/irc-unvoice.svg
/usr/share/quassel/icons/breeze/actions/24/irc-voice.svg
/usr/share/quassel/icons/breeze/actions/24/list-add-user.svg
/usr/share/quassel/icons/breeze/actions/24/list-add.svg
/usr/share/quassel/icons/breeze/actions/24/list-remove-user.svg
/usr/share/quassel/icons/breeze/actions/24/mail-message-new.svg
/usr/share/quassel/icons/breeze/actions/24/media-playback-start.svg
/usr/share/quassel/icons/breeze/actions/24/network-connect.svg
/usr/share/quassel/icons/breeze/actions/24/network-disconnect.svg
/usr/share/quassel/icons/breeze/actions/24/show-menu.svg
/usr/share/quassel/icons/breeze/actions/24/tools-report-bug.svg
/usr/share/quassel/icons/breeze/actions/24/view-fullscreen.svg
/usr/share/quassel/icons/breeze/actions/24/view-refresh.svg
/usr/share/quassel/icons/breeze/actions/24/zoom-in.svg
/usr/share/quassel/icons/breeze/actions/24/zoom-original.svg
/usr/share/quassel/icons/breeze/actions/24/zoom-out.svg
/usr/share/quassel/icons/breeze/actions/32/application-exit.svg
/usr/share/quassel/icons/breeze/actions/32/configure-shortcuts.svg
/usr/share/quassel/icons/breeze/actions/32/configure.svg
/usr/share/quassel/icons/breeze/actions/32/connect-quassel.svg
/usr/share/quassel/icons/breeze/actions/32/dialog-cancel.svg
/usr/share/quassel/icons/breeze/actions/32/disconnect-quassel.svg
/usr/share/quassel/icons/breeze/actions/32/document-edit.svg
/usr/share/quassel/icons/breeze/actions/32/document-open.svg
/usr/share/quassel/icons/breeze/actions/32/edit-delete.svg
/usr/share/quassel/icons/breeze/actions/32/go-down.svg
/usr/share/quassel/icons/breeze/actions/32/go-next.svg
/usr/share/quassel/icons/breeze/actions/32/go-previous.svg
/usr/share/quassel/icons/breeze/actions/32/go-up.svg
/usr/share/quassel/icons/breeze/actions/32/help-about.svg
/usr/share/quassel/icons/breeze/actions/32/mail-message-new.svg
/usr/share/quassel/icons/breeze/actions/32/media-playback-start.svg
/usr/share/quassel/icons/breeze/actions/32/view-refresh.svg
/usr/share/quassel/icons/breeze/actions/32/zoom-in.svg
/usr/share/quassel/icons/breeze/actions/32/zoom-original.svg
/usr/share/quassel/icons/breeze/actions/32/zoom-out.svg
/usr/share/quassel/icons/breeze/apps/32/quassel.svg
/usr/share/quassel/icons/breeze/apps/48/quassel.svg
/usr/share/quassel/icons/breeze/apps/64/quassel.svg
/usr/share/quassel/icons/breeze/devices/16/network-wired.svg
/usr/share/quassel/icons/breeze/devices/22/network-wired.svg
/usr/share/quassel/icons/breeze/index.theme
/usr/share/quassel/icons/breeze/preferences/32/help-about.svg
/usr/share/quassel/icons/breeze/scalable/actions/connect-quassel.svg
/usr/share/quassel/icons/breeze/scalable/actions/disconnect-quassel.svg
/usr/share/quassel/icons/breeze/scalable/apps/quassel.svg
/usr/share/quassel/icons/breeze/scalable/status/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/scalable/status/active-quassel-tray.svg
/usr/share/quassel/icons/breeze/scalable/status/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/scalable/status/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze/scalable/status/inactive-quassel.svg
/usr/share/quassel/icons/breeze/scalable/status/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/scalable/status/message-quassel-tray.svg
/usr/share/quassel/icons/breeze/scalable/status/message-quassel.svg
/usr/share/quassel/icons/breeze/status/16/dialog-information.svg
/usr/share/quassel/icons/breeze/status/16/security-high.svg
/usr/share/quassel/icons/breeze/status/16/security-low.svg
/usr/share/quassel/icons/breeze/status/16/user-available.svg
/usr/share/quassel/icons/breeze/status/16/user-away.svg
/usr/share/quassel/icons/breeze/status/16/user-offline.svg
/usr/share/quassel/icons/breeze/status/22/dialog-information.svg
/usr/share/quassel/icons/breeze/status/22/dialog-password.svg
/usr/share/quassel/icons/breeze/status/22/network-wired.svg
/usr/share/quassel/icons/breeze/status/22/security-high.svg
/usr/share/quassel/icons/breeze/status/22/security-low.svg
/usr/share/quassel/icons/breeze/status/22/user-available.svg
/usr/share/quassel/icons/breeze/status/22/user-away.svg
/usr/share/quassel/icons/breeze/status/22/user-offline.svg
/usr/share/quassel/icons/breeze/status/24/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/24/active-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/24/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/24/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/24/inactive-quassel.svg
/usr/share/quassel/icons/breeze/status/24/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/24/message-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/24/message-quassel.svg
/usr/share/quassel/icons/breeze/status/64/active-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/64/active-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/64/dialog-information.svg
/usr/share/quassel/icons/breeze/status/64/dialog-password.svg
/usr/share/quassel/icons/breeze/status/64/dialog-warning.svg
/usr/share/quassel/icons/breeze/status/64/inactive-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/64/inactive-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/64/inactive-quassel.svg
/usr/share/quassel/icons/breeze/status/64/message-quassel-tray-inverted.svg
/usr/share/quassel/icons/breeze/status/64/message-quassel-tray.svg
/usr/share/quassel/icons/breeze/status/64/message-quassel.svg
/usr/share/quassel/icons/breeze/status/64/security-high.svg
/usr/share/quassel/icons/breeze/status/64/security-low.svg
/usr/share/quassel/networks.ini
/usr/share/quassel/scripts/inxi
/usr/share/quassel/scripts/mpris
/usr/share/quassel/stylesheets/LinuxDolt-bluestheme.qss
/usr/share/quassel/stylesheets/default.qss
/usr/share/quassel/stylesheets/jussi01-darktheme.qss
/usr/share/quassel/stylesheets/m4yer.qss

%files extras
%defattr(-,root,root,-)
/usr/bin/quasselcore

%files license
%defattr(-,root,root,-)
/usr/share/doc/quassel/3rdparty_icons_breeze-dark_COPYING-ICONS
/usr/share/doc/quassel/3rdparty_icons_breeze-dark_LICENSE
/usr/share/doc/quassel/3rdparty_icons_breeze_COPYING-ICONS
/usr/share/doc/quassel/3rdparty_icons_breeze_LICENSE
/usr/share/doc/quassel/3rdparty_icons_oxygen_COPYING
/usr/share/doc/quassel/cmake_COPYING-CMAKE-SCRIPTS
