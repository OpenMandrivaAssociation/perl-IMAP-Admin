%define module  IMAP-Admin
%define name    perl-%{module}
%define version 1.6.6
%define release %mkrel 1

Name:		%name
Summary:	IMAP-Admin Perl module
Version:	%version
Release:	%release
License:	GPL or Artistic
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
URL:		http://search.cpan.org/dist/%{module}/
Buildarch:	noarch

%description
A perl module to manage IMAP servers

%prep
%setup -n %{module}-%{version}

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

