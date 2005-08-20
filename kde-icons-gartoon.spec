%define		_name gartoon
Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.3
Release:	0.1
License:	DESIGN SCIENCE LICENSE
Group:		Themes
Source0:	%{_name}-%{version}.tar.bz2
# Source0-md5:	90ddfb75d023ffb1887c824f510c21b8
Source0:	http://www.nasland.nu/gartoon/ICONS-Gartoon-PNG-v%{version}.tar.bz2
# Source0-md5:	90ddfb75d023ffb1887c824f510c21b8
NoSource:	0
Source1:	http://www.nasland.nu/gartoon/ICONS-Gartoon.Blue-PNG-v%{version}.tar.bz2
# Source1-md5:	8f75478d3fdde9a04aeba5b448094b02
NoSource:	1
URL:		http://www.kde-look.org/content/show.php?content=17362
Requires:	kdelibs >= 9:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fun looking icons with bright colors and bold outlines.

%package blue
Summary:	KDE icons - %{_name} blue
Group:		Themes

%description blue
Fun looking icons with bright colors and bold outlines. Blue theme.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{_name}{,-blue}

%{__tar} xjf %{SOURCE0} --strip-components=1 -C $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
%{__tar} xjf %{SOURCE1} --strip-components=1 -C $RPM_BUILD_ROOT%{_iconsdir}/%{_name}-blue

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}

%files blue
%{_iconsdir}/%{_name}-blue
