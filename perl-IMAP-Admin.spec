%define upstream_name    IMAP-Admin
%define upstream_version 1.6.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	IMAP-Admin Perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/IMAP/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A perl module to manage IMAP servers

%prep
%setup -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Changes examples
%defattr(-, root, root)
%{perl_vendorlib}/IMAP/*
%{_mandir}/*/*
