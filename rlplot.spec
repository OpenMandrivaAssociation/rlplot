%define name 	rlplot
%define version 1.5
%define release %mkrel 1

Summary: 	Data Plotting and Graphing
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://prdownloads.sourceforge.net/%{name}/%{name}_%version.tar.gz
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL: 		http://rlplot.sourceforge.net
License: 	GPLv2+
Group: 		Sciences/Other
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires: 	qt4-devel
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
perl -pi -e 's/bin\/moc-qt4/bin\/moc/g' Makefile
perl -pi -e 's/usr\/include\/Qt/usr\/lib\/qt4\/include \-I\/usr\/lib\/qt4\/include\/Qt/g' Makefile
perl -pi -e 's/X11R6\/lib/%{_lib}/g' Makefile

# fix overlinking
perl -pi -e 's/\-lX11//g' Makefile

%build
%make

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 755 rlplot %{buildroot}%{_bindir}
install -m 755 exprlp %{buildroot}%{_bindir}

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
mkdir -p %{buildroot}%{_liconsdir}
cat %{SOURCE1} > %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
cat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
cat %{SOURCE3} > %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

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
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%defattr(644,root,root,0755)
%doc README gpl.txt


