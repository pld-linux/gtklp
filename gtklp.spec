# TODO:
# - icon from project page
# - .desktop file
# - integrate non english docs
Summary:	A gtk frontend to CUPS
Summary(pl):	Interfejs gtk do CUPS
Name:		gtklp
Version:	0.9r
Release:	2
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
# Source0-md5:	1dd7892666ae80ac45ac06813fca18b6
URL:		http://gtklp.sourceforge.net/
Patch0:		%{name}-locale_names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel >= 1.1.10
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A gtk frontend to CUPS.

%description -l pl
Interfejs gtk do CUPS.

%prep
%setup  -q
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

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS TODO USAGE README BUGS AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
