%define		_name gartoon
Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.3
Release:	0.2
License:	Design Science
Group:		Themes
Source0:	http://www.nasland.nu/gartoon/ICONS-Gartoon-SVG-v%{version}.tar.bz2
# NoSource0-md5:	6b9453198ca1e29fbd52b033fa9fd82a
NoSource:	0
Source1:	http://www.nasland.nu/gartoon/ICONS-Gartoon.Blue-SVG-v%{version}.tar.bz2
# NoSource1-md5:	4081cce286fc3bf21886001d47e6eb22
NoSource:	1
URL:		http://www.kde-look.org/content/show.php?content=17362
Requires:	kdelibs >= 9:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fun looking icons with bright colors and bold outlines.

%description -l pl
¦miesznie wygl±daj±ce ikony z jasnymi kolorami i grubymi liniami
otaczaj±cymi.

%package blue
Summary:	KDE icons - %{_name} blue
Summary(pl):	Motyw ikon do KDE - %{_name} blue
Group:		Themes

%description blue
Fun looking icons with bright colors and bold outlines. Blue theme.

%description blue -l pl
¦miesznie wygl±daj±ce ikony z jasnymi kolorami i grubymi liniami
otaczaj±cymi. Motyw niebieski.

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
%defattr(644,root,root,755)
%{_iconsdir}/%{_name}-blue
