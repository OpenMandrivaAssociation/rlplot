%define name 	rlplot
%define version 1.3
%define release %mkrel 3

Summary: 	Data Plotting and Graphing
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/%{name}/%{name}_%version.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL: 		http://rlplot.sourceforge.net
License: 	GPL
Group: 		Sciences/Other
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires: 	qt3-devel
Obsoletes:	RLPlot
Provides:	RLPlot

%description
RLPlot is is a plotting program to create high quality graphs from data. 
Based on values stored in a spreadsheet several menus help you to create 
graphs of your choice. The Graphs are displayed as you get them (Wysiwyg). 
Double click any element of the graph (or a single click with the right 
mouse button) to modify its properties.

%prep
%setup -q -n %{name}
perl -pi -e 's/\-O2/\$\(RPM_OPT_FLAGS\)/g' Makefile
perl -pi -e 's/QTDIR\)\/lib/QTDIR\)\/%{_lib}/g' Makefile
perl -pi -e 's/X11R6\/lib/X11R6\/%{_lib}/g' Makefile

%build
%make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m 755 rlplot $RPM_BUILD_ROOT/usr/bin
install -m 755 exprlp $RPM_BUILD_ROOT/usr/bin

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=RLPlot
Comment=Data plotting and graphing
Exec=rlplot
Icon=rlplot
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Other;Science;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post 
%{update_menus}
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus}
%endif

%files
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/exprlp
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/*
%defattr(644,root,root,0755)
%doc README gpl.txt


