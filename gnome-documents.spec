%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define	api	1.0

Name:		gnome-documents
Version:	3.8.3
Release:	1
License:	GPLv2+
Summary:	Document manager application for GNOME
Url:		http://www.gnome.org/
Group:		Graphical desktop/GNOME
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(evince-document-3.0) >= 3.3.0
BuildRequires:	pkgconfig(evince-view-3.0) >= 3.3.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:	pkgconfig(glib-2.0) >= 2.29.90
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.13
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(tracker-sparql-0.16) >= 0.13.1
BuildRequires:	pkgconfig(goa-1.0) >= 3.1.90
BuildRequires:	pkgconfig(libgdata) >= 0.9.1
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.1
# gjs-1.0 is needed to get the path to gjs-console
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(zapojit-0.0)
Requires:	gjs
Requires:	tracker

Obsoletes:	%{_lib}gdprivate1.0_0 < 0.3.3
Obsoletes:	%{_lib}gdprivate1.0-devel < 0.3.3
Obsoletes:	%{_lib}gdprivate-gir1.0 < 3.6.0-2

%description
Documents is a document manager application for GNOME.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_libexecdir}/gd-tracker-gdata-miner
%{_libexecdir}/gnome-documents-search-provider
%{_libexecdir}/gd-tracker-zpj-miner
%{_libdir}/%{name}/girepository-1.0/Gd-%{api}.typelib
%{_libdir}/%{name}/girepository-1.0/GdPrivate-%{api}.typelib
%{_libdir}/%{name}/libgd.so
%{_libdir}/%{name}/libgdprivate-%{api}.so
%{_libdir}/%{name}/libgdminer-%{api}.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/dbus-1/services/org.gnome.Documents.ZpjMiner.service
%{_datadir}/dbus-1/services/org.gnome.Documents.GDataMiner.service
%{_datadir}/dbus-1/services/org.gnome.Documents.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-documents-search-provider.ini
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

