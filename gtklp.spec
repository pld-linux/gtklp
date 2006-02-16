# TODO:
# - integrate non english docs

%define	_iconsrc icons_n_logos

Summary:	A GTK+ frontend to CUPS
Summary(pl):	Interfejs GTK+ do CUPS
Name:		gtklp
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
# Source0-md5:	39db061d51c9962e4d55cd68b787a3f2
Source1:	http://dl.sourceforge.net/gtklp/%{_iconsrc}.tar.gz
# Source1-md5:	e6e7f46c1b525c6993eaeee0c61fe5d1
Source3:	%{name}.desktop
URL:		http://gtklp.sourceforge.net/
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-man_ru.patch
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
%setup -q -a1
%patch0 -p1
%patch1 -p1

mv -f po/{cz,cs}.po

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_mandir}/ru/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this is bogus zh_CN:
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/chs

mv $RPM_BUILD_ROOT%{_mandir}/man1/gtklp-ru.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1/gtklp.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/gtklpq-ru.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1/gtklpq.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{_iconsrc}/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS TODO USAGE README BUGS AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
