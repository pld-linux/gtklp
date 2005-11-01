# TODO:
# - integrate non english docs

%define	_iconsrc icons_n_logos

Summary:	A GTK+ frontend to CUPS
Summary(pl):	Interfejs GTK+ do CUPS
Name:		gtklp
Version:	1.0d
Release:	2
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
# Source0-md5:	eacea48c91360bb20133238ce1377359
Source1:	http://dl.sourceforge.net/gtklp/%{_iconsrc}.tar.gz
# Source1-md5:	e6e7f46c1b525c6993eaeee0c61fe5d1
Source3:	%{name}.desktop
URL:		http://gtklp.sourceforge.net/
Patch0:		%{name}-locale_names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel >= 1.1.10
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A GTK+ frontend to CUPS.

%description -l pl
Interfejs GTK+ do CUPS.

%prep
%setup -q
%patch0 -p1

mv -f po/{cz,cs}.po

%build
rm -r missing
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{_iconsrc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this is bogus zh_CN:
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/chs

%find_lang %{name}

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
tar zxf %{SOURCE1} -C $RPM_BUILD_DIR
cd $RPM_BUILD_DIR/%{_iconsrc}
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS TODO USAGE README BUGS AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
