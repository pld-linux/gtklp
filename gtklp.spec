# TODO:
# - icon from project page
# - .desktop file
# - integrate non english docs
Summary:	a gtk frontend to CUPS
Summary(pl):	Interfejs gtk do CUPS
Name:		gtklp
Version:	0.9m
Release:	1
License:	GPL
Group:		Applications/Printing
URL:		http://www.stud.uni-hannover.de/~sirtobi/gtklp/
Source0:	http://www.stud.uni-hannover.de/~sirtobi/gtklp/files/%{name}-%{version}.src.tar.gz
BuildRequires:	cups-devel >= 1.1.10
BuildRequires:	gtk+-devel >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
a gtk frontend to CUPS.

%description -l pl
Interfejs gtk do CUPS.

%prep
%setup  -q

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

gzip -9fn NEWS TODO USAGE README BUGS AUTHORS ChangeLog

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
