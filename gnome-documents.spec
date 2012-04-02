%define api	1.0
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Document manager application for GNOME
Name:		gnome-documents
Version:	0.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(evince-document-3.0)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(tracker-sparql-0.12)

Requires:	gjs

%description
Documents is a document manager application for GNOME.

%prep
%setup -q
%apply_patches

%build
# remove disable shared with 0.4.x
%configure2_5x \
	--disable-shared
%make

%install
%makeinstall_std

%find_lang %{name}

#we don't want these
find %{buildroot} -name "*.la" -delete

# just for now b/c in 0.4.x the lib turns into a plugin
rm -f %{buildroot}%{_libdir}/libgdprivate-1.0.a \
	%{buildroot}%{_datadir}/gir-1.0/Gd-1.0.gir

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/girepository-1.0/Gd-%{api}.typelib
#{_libdir}/%{name}/libgdprivate-%{api}.so
%{_libexecdir}/gd-tracker-gdata-miner
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Documents.GDataMiner.service

