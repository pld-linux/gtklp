# TODO:
# - integrate non english docs

Summary:	A GTK+ frontend to CUPS
Summary(pl):	Interfejs GTK+ do CUPS
Name:		gtklp
Version:	1.0
%define		_pre 	pre3
Release:	0.%{_pre}.1
License:	GPL
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/gtklp/%{name}-%{version}%{_pre}.src.tar.gz
# Source0-md5:	5bf25637adac9bd716aa0f4337614da3
Source1:	http://prdownloads.sourceforge.net/gtklp/icons_n_logos.tar.gz
# Source1-md5:	e6e7f46c1b525c6993eaeee0c61fe5d1
Source3:	%{name}.desktop
URL:		http://gtklp.sourceforge.net/
Patch0:		%{name}-locale_names.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel >= 1.1.10
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_iconsrc icons_n_logos

%description
A GTK+ frontend to CUPS.

%description -l pl
Interfejs GTK+ do CUPS.

%prep
%setup -q -n %{name}-%{version}%{_pre}
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
