# TODO:
# - automake/autoconf/gettext support
# - icon from project page
# - .desktop file
# - integrate non english docs
# - send all this improvements to author
Summary:	a gtk frontend to CUPS
Name:		gtklp
Version:	0.9
Release:	0.1
License:	GPL
Group:		Applications/Printing
URL:		http://www.stud.uni-hannover.de/~sirtobi/gtklp/
Source0:	http://www.stud.uni-hannover.de/~sirtobi/gtklp/files/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-Makefile.patch
BuildRequires:	cups-devel >= 1.1.10
BuildRequires:	gtk+-devel >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
a gtk frontend to CUPS


%prep
%setup  -q
%patch0 -p1 -b .wiget

%build
%{__make} CC=%{__cc} EXTRA="%{rpmcflags} %{rpmldflags}" \
	DEBUG="" STRIP="true"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -c -m 0755  gtklp $RPM_BUILD_ROOT%{_bindir}
install -c -m 0755  gtklpq/gtklpq $RPM_BUILD_ROOT%{_bindir}
install -c -m 0444  man/gtklp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 0444  man/gtklpq.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
