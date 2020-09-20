%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}typelib\\((Gd|GdPrivate)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}typelib\\((Gd|GdPrivate)\\)

%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define	api	1.0

Name:		gnome-documents
Version:	3.34.0
Release:	3
License:	GPLv2+
Summary:	Document manager application for GNOME
Url:		http://www.gnome.org/
Group:		Graphical desktop/GNOME
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(evince-document-3.0) >= 3.3.0
BuildRequires:	pkgconfig(evince-view-3.0) >= 3.3.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(glib-2.0) >= 2.29.90
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.13
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(tracker-sparql-3.0)
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.90
BuildRequires:	pkgconfig(libgdata) >= 0.9.1
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.1
BuildRequires:	pkgconfig(webkit2gtk-4.0)
# gjs-1.0 is needed to get the path to gjs-console
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(zapojit-0.0)
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtds
BuildRequires:	docbook-utils
BuildRequires:	docbook-utils-pdf
BuildRequires:	docbook2x
BuildRequires:	librsvg2
BuildRequires:	meson
BuildRequires:	poppler
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libgepub-0.6)
BuildRequires:  inkscape

Requires:	gjs
Requires:	tracker
Recommends:	unoconv

Requires: typelib(Atk)
Requires: typelib(EvinceDocument)
Requires: typelib(EvinceView)
Requires: typelib(GData)
Requires: typelib(GDesktopEnums)
Requires: typelib(GLib)
Requires: typelib(GModule)
Requires: typelib(GObject)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GnomeDesktop)
Requires: typelib(Goa)
Requires: typelib(Gtk)
Requires: typelib(Json)
#Requires: typelib(LOKDocView)
Requires: typelib(Pango)
Requires: typelib(Rest)
Requires: typelib(Soup)
Requires: typelib(Tracker)
Requires: typelib(TrackerControl)
Requires: typelib(WebKit2)
Requires: typelib(Zpj)
Requires: typelib(cairo)
Requires: typelib(libxml2)
Requires: typelib(xlib)

Obsoletes:	%{_lib}gdprivate1.0_0 < 0.3.3
Obsoletes:	%{_lib}gdprivate1.0-devel < 0.3.3
Obsoletes:	%{_lib}gdprivate-gir1.0 < 3.6.0-2

%description
Documents is a document manager application for GNOME.

%prep
%setup -q

%build
%meson -Dgetting_started=false
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_libdir}/%{name}/libgd.so
%{_libdir}/%{name}/libgdprivate-%{api}.so
%{_datadir}/metainfo/org.gnome.Documents.appdata.xml
%{_datadir}/applications/org.gnome.Documents.desktop
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/org.gnome.Documents*
#{_iconsdir}/hicolor/*/apps/%{name}-symbolic.svg
%_mandir/man1/*
%{_libdir}/%{name}/girepository-1.0/Gd-1.0.typelib
%{_libdir}/%{name}/girepository-1.0/GdPrivate-1.0.typelib
