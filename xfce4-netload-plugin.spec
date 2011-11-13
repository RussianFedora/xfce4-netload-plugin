%global minor_version 1.0

Name:          xfce4-netload-plugin
Version:       1.0.0
Release:       3.1%{?dist}.R
Summary:       Network-load monitor for the Xfce panel

Group:         User Interface/Desktops
License:       GPLv2+
URL:           http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:       http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

# Resolve https://bugzilla.xfce.org/show_bug.cgi?id=7804 bug on 
Patch1:        xfce4-netload-plugin-show-values.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: xfce4-panel-devel >= 4.3.20, libxfcegui4-devel >= 4.3.20, libxml2-devel
BuildRequires: gettext, intltool
Requires:      xfce4-panel >= 4.4.0

%description
A network-load monitor plugin for the Xfce panel.

%prep
%setup -q
%patch1 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_libexecdir}/xfce4/panel-plugins/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel-plugins/*.desktop

%changelog
* Sun Nov 13 2011 Romanov Ivan <drizt@land.ru> - 1.0.0-3.1.R
- Added xfce4-netload-plugin-show-values patch
 
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-2
- Rebuild for xfce4-panel 4.7

* Fri Dec 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Remove all patches (upstreamed)

* Wed Sep 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-12
- Fix bar colors (#505214)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-10
- Bring back tooltips in GTK 2.16 with Dimitar Zhekov's patch (#508637)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-8
- Rebuild for Xfce 4.6 (Beta 3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-7
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-6
- Rebuild for BuildID feature
- Update license tag

* Sat Apr 28 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-5
- Rebuild for Xfce 4.4.1

* Mon Jan 22 2007 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-4
- Rebuild for Xfce 4.4.
- Patch to compile with -Wl,--as-needed (bugzilla.xfce.org #2782)

* Thu Oct 05 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-3
- Bump release for devel checkin.

* Wed Sep 13 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-2
- BR perl(XML::Parser).

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4 on XFCE 4.3.90.2.
- Remove bufsize-patch for now.

* Mon Sep 04 2006 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-7
- Mass rebuild for Fedora Core 6.

* Tue Apr 11 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-6
- Require xfce4-panel.

* Sat Feb 18 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-5
- Rebuild for Fedora Extras 5.
- Modify bufsize-patch.

* Thu Feb 02 2006 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-4
- Add bufsize-patch (#179686).

* Thu Dec 01 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-3
- Add libxfcegui4-devel BuildReqs.
- Fix %%defattr.

* Mon Nov 14 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-2
- Initial Fedora Extras version.
- Rebuild for XFCE 4.2.3.
- disable-static instead of removing .a files.

* Fri Sep 23 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.3-1.fc4.cw
- Updated to version 0.3.3.
- Add libxml2 BuildReqs.

* Sat Jul 09 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.2-1.fc4.cw
- Updated to version 0.3.2.
- Rebuild for Core 4.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.3.1-1.fc3.cw
- Updated to version 0.3.1.

* Wed Apr 13 2005 Christoph Wickert <fedora wickert at arcor de> - 0.2.3-1.fc3.cw
- Initial RPM release.
