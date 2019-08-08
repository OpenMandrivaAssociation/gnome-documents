%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define		gi_libname	%mklibname gdprivate-gir %{api}
%define	api	1.0

Name:		gnome-documents
Version:	3.32.0
Release:	1
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
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.90
BuildRequires:	pkgconfig(libgdata) >= 0.9.1
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.1
BuildRequires:	pkgconfig(webkit2gtk-4.0)
# gjs-1.0 is needed to get the path to gjs-console
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(zapojit-0.0)
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	librsvg2
BuildRequires:	meson
BuildRequires:	poppler
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libgepub-0.6)
BuildRequires:  inkscape

Requires:	gjs
Requires:	tracker
Requires: typelib(EvinceDocument)
Requires: typelib(GdPrivate)
Recommends:	unoconv

Obsoletes:	%{_lib}gdprivate1.0_0 < 0.3.3
Obsoletes:	%{_lib}gdprivate1.0-devel < 0.3.3
Obsoletes:	%{_lib}gdprivate-gir1.0 < 3.6.0-2

%description
Documents is a document manager application for GNOME.

%package -n %{gi_libname}
Summary:	GObject introspection interface for %{name}
Group:		System/Libraries

%description -n %{gi_libname}
GObject introspection interface for %{name}.

%prep
%setup -q

%build
%meson -Dgetting_started=true
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

%files -n %{gi_libname}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Gd-%{api}.typelib
%{_libdir}/%{name}/girepository-1.0/GdPrivate-%{api}.typelib
